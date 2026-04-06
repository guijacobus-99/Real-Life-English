import pandas as pd
import re
import json
from datetime import datetime
from collections import defaultdict

VALID_TIPOS = {"crédito", "débito", "pix", "boleto"}
VALID_STATUS = {"aprovado", "reprovado", "pendente", "cancelado"}
VALID_CANAIS = {"app", "web", "loja física", "telefone"}
CPF_FORMATTED = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
CPF_INVALID_KNOWN = {
    "000.000.000-00",
    "111.111.111-11",
    "222.222.222-22",
    "333.333.333-33",
    "444.444.444-44",
    "555.555.555-55",
    "666.666.666-66",
    "777.777.777-77",
    "888.888.888-88",
    "999.999.999-99",
}


def validate_date(val):
    if pd.isna(val) or val == "":
        return False
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            datetime.strptime(str(val), fmt)
            return True
        except:
            pass
    return False


def run_validation(filepath):
    df = pd.read_excel(filepath, dtype=str)
    df.columns = df.columns.str.strip()
    issues = defaultdict(list)

    dupes = df[df.duplicated(keep=False)]
    for idx in dupes.index:
        issues["linha_duplicada"].append(idx + 2)

    id_dupes = df[df.duplicated(subset=["id_transacao"], keep=False)]
    for idx in id_dupes.index:
        issues["id_transacao_duplicado"].append(idx + 2)

    for idx, row in df.iterrows():
        line = idx + 2
        cpf = str(row.get("cpf_cliente", "")).strip()
        if not CPF_FORMATTED.match(cpf):
            issues["cpf_sem_formatacao"].append(line)
        elif cpf in CPF_INVALID_KNOWN:
            issues["cpf_invalido"].append(line)

        valor = row.get("valor", "")
        if pd.isna(valor) or str(valor).strip() in ("", "nan", "None"):
            issues["valor_nulo"].append(line)
        else:
            try:
                v = float(valor)
                if v < 0:
                    issues["valor_negativo"].append(line)
                if v == 0:
                    issues["valor_zero"].append(line)
            except:
                issues["valor_invalido"].append(line)

        if not validate_date(row.get("data", "")):
            issues["data_invalida"].append(line)

        status = str(row.get("status", "")).strip()
        if status.lower() in VALID_STATUS and status != status.lower():
            issues["status_capitalizacao"].append(line)
        elif status.lower() not in VALID_STATUS:
            issues["status_fora_padrao"].append(line)

        tipo = str(row.get("tipo", "")).strip().lower()
        if tipo not in VALID_TIPOS:
            issues["tipo_fora_padrao"].append(line)

        nome = str(row.get("nome_cliente", "")).strip()
        if nome in ("", "nan", "None"):
            issues["nome_vazio"].append(line)

    return df, issues


labels = {
    "linha_duplicada": ("Linhas Duplicadas", "Registros completamente idênticos", "🔁"),
    "id_transacao_duplicado": (
        "ID Duplicado",
        "Mesmo id_transacao em linhas diferentes",
        "🆔",
    ),
    "cpf_sem_formatacao": (
        "CPF Sem Formatação",
        "CPF fora do padrão 000.000.000-00",
        "📋",
    ),
    "cpf_invalido": ("CPF Inválido", "CPF com sequência inválida conhecida", "❌"),
    "valor_nulo": ("Valor Nulo", "Campo valor vazio ou ausente", "🚫"),
    "valor_negativo": ("Valor Negativo", "Transação com valor menor que zero", "📉"),
    "valor_zero": ("Valor Zerado", "Transação com valor igual a zero", "0️⃣"),
    "valor_invalido": ("Valor Inválido", "Campo valor não é numérico", "⚠️"),
    "data_invalida": ("Data Inválida", "Formato ou data inexistente", "📅"),
    "status_capitalizacao": (
        "Status Capitalização",
        "Status em formato inconsistente (ex: APROVADO)",
        "🔤",
    ),
    "status_fora_padrao": (
        "Status Fora do Padrão",
        "Valor não está na lista de status válidos",
        "⛔",
    ),
    "tipo_fora_padrao": ("Tipo Inválido", "Tipo de transação não reconhecido", "💳"),
    "nome_vazio": ("Nome Vazio", "Cliente sem nome preenchido", "👤"),
}

severity = {
    "linha_duplicada": "high",
    "id_transacao_duplicado": "high",
    "cpf_invalido": "high",
    "valor_nulo": "high",
    "valor_negativo": "medium",
    "valor_zero": "low",
    "data_invalida": "medium",
    "cpf_sem_formatacao": "medium",
    "valor_invalido": "high",
    "status_capitalizacao": "low",
    "status_fora_padrao": "medium",
    "tipo_fora_padrao": "medium",
    "nome_vazio": "low",
}

df, issues = run_validation("data/transacoes_ficticias_raw.xlsx")
total = len(df)
total_issues = sum(len(v) for v in issues.items())
affected_rows = len(set(r for rows in issues.values() for r in rows))
total_problems = sum(len(v) for v in issues.values())
quality_score = round((1 - affected_rows / total) * 100, 1)

cards = []
for key, rows in issues.items():
    lbl, desc, icon = labels.get(key, (key, "", "⚠️"))
    sev = severity.get(key, "medium")
    cards.append(
        {
            "key": key,
            "label": lbl,
            "desc": desc,
            "icon": icon,
            "count": len(rows),
            "lines": rows[:8],
            "severity": sev,
        }
    )

cards.sort(key=lambda x: {"high": 0, "medium": 1, "low": 2}[x["severity"]])

sev_counts = {
    "high": sum(1 for c in cards if c["severity"] == "high"),
    "medium": sum(1 for c in cards if c["severity"] == "medium"),
    "low": sum(1 for c in cards if c["severity"] == "low"),
}

now = datetime.now().strftime("%d/%m/%Y às %H:%M")

cards_html = ""
for c in cards:
    lines_str = ", ".join(str(l) for l in c["lines"])
    if len(c["lines"]) < c["count"]:
        lines_str += "..."
    sev_label = {"high": "Alto", "medium": "Médio", "low": "Baixo"}[c["severity"]]
    cards_html += f"""
    <div class="issue-card sev-{c["severity"]}">
      <div class="card-header">
        <span class="card-icon">{c["icon"]}</span>
        <div class="card-title-group">
          <h3>{c["label"]}</h3>
          <p>{c["desc"]}</p>
        </div>
        <div class="card-badge">
          <span class="count-badge">{c["count"]}</span>
          <span class="sev-badge sev-{c["severity"]}">{sev_label}</span>
        </div>
      </div>
      <div class="card-lines">
        <span class="lines-label">Linhas afetadas:</span> {lines_str}
      </div>
    </div>"""

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Relatório de Qualidade — Transações</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Instrument+Serif:ital@0;1&family=Syne:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0a0a0b;
    --surface: #141416;
    --surface-elevated: #1a1a1d;
    --border: #2a2a2e;
    --border-light: #3a3a40;
    --accent: #ff6b35;
    --accent-secondary: #00d4aa;
    --text: #f0f0f2;
    --text-secondary: #8a8a92;
    --high: #ff3b3b;
    --medium: #ffb84d;
    --low: #00d4aa;
    --high-bg: rgba(255,59,59,0.1);
    --medium-bg: rgba(255,184,77,0.1);
    --low-bg: rgba(0,212,170,0.1);
  }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
  }}

  body::before {{
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    opacity: 0.03;
    pointer-events: none;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  }}

  body::after {{
    content: '';
    position: fixed;
    inset: 0;
    z-index: 0;
    opacity: 0.4;
    pointer-events: none;
    background-image:
      linear-gradient(90deg, var(--border) 1px, transparent 1px),
      linear-gradient(var(--border) 1px, transparent 1px);
    background-size: 60px 60px;
    mask-image: radial-gradient(ellipse at center, black 0%, transparent 70%);
  }}

  .page {{
    position: relative;
    z-index: 1;
    max-width: 1200px;
    margin: 0 auto;
    padding: 60px 40px;
  }}

  .header {{
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 40px;
    margin-bottom: 80px;
    align-items: start;
  }}

  .header-main {{
    position: relative;
  }}

  .header-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    color: var(--accent);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 12px;
  }}

  .header-tag::before {{
    content: '';
    width: 24px;
    height: 1px;
    background: var(--accent);
  }}

  .header h1 {{
    font-family: 'Syne', sans-serif;
    font-size: clamp(48px, 8vw, 96px);
    font-weight: 800;
    line-height: 0.9;
    letter-spacing: -0.03em;
    margin-bottom: 20px;
  }}

  .header h1 span {{
    color: var(--accent);
    font-style: italic;
  }}

  .header-meta {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-secondary);
    display: flex;
    gap: 24px;
  }}

  .header-meta span {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .header-meta span::before {{
    content: '';
    width: 4px;
    height: 4px;
    background: var(--border-light);
    border-radius: 50%;
  }}

  .score-section {{
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 0;
    margin-bottom: 80px;
    position: relative;
  }}

  .score-section::before {{
    content: '';
    position: absolute;
    left: 280px;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--border);
  }}

  .score-left {{
    padding-right: 40px;
    position: sticky;
    top: 40px;
    height: fit-content;
  }}

  .score-display {{
    position: relative;
    padding: 40px;
    background: var(--surface);
    border: 1px solid var(--border);
    clip-path: polygon(0 0, 100% 0, 100% calc(100% - 20px), calc(100% - 20px) 100%, 0 100%);
  }}

  .score-display::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: {{'var(--high-bg)' if quality_score < 70 else 'var(--medium-bg)' if quality_score < 90 else 'var(--low-bg)'}};
    opacity: 0.5;
  }}

  .score-number {{
    position: relative;
    font-family: 'Syne', sans-serif;
    font-size: 72px;
    font-weight: 800;
    line-height: 1;
    color: {{'var(--high)' if quality_score < 70 else 'var(--medium)' if quality_score < 90 else 'var(--low)'}};
    margin-bottom: 8px;
  }}

  .score-label {{
    position: relative;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--text-secondary);
  }}

  .score-status {{
    position: relative;
    margin-top: 24px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
    font-family: 'Instrument Serif', serif;
    font-size: 18px;
    font-style: italic;
    color: {{'var(--high)' if quality_score < 70 else 'var(--medium)' if quality_score < 90 else 'var(--low)'}};
  }}

  .score-right {{
    padding-left: 40px;
  }}

  .score-description {{
    font-family: 'Instrument Serif', serif;
    font-size: 22px;
    line-height: 1.6;
    color: var(--text);
    margin-bottom: 40px;
  }}

  .score-description em {{
    color: var(--accent);
    font-style: normal;
  }}

  .stats-container {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: var(--border);
    margin-bottom: 80px;
  }}

  .stat-item {{
    background: var(--surface);
    padding: 32px;
    position: relative;
    overflow: hidden;
  }}

  .stat-item::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    background: var(--accent);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .stat-item:hover::before {{
    transform: scaleX(1);
  }}

  .stat-value {{
    font-family: 'Syne', sans-serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 1;
    color: var(--accent);
    margin-bottom: 8px;
  }}

  .stat-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-secondary);
  }}

  .severity-bar {{
    display: flex;
    gap: 1px;
    margin-bottom: 80px;
    background: var(--border);
  }}

  .severity-item {{
    flex: 1;
    background: var(--surface);
    padding: 24px;
    text-align: center;
    position: relative;
  }}

  .severity-count {{
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 4px;
  }}

  .severity-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text-secondary);
  }}

  .severity-item.sev-high .severity-count {{ color: var(--high); }}
  .severity-item.sev-medium .severity-count {{ color: var(--medium); }}
  .severity-item.sev-low .severity-count {{ color: var(--low); }}

  .issues-section {{
    position: relative;
  }}

  .issues-header {{
    display: flex;
    align-items: baseline;
    gap: 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 20px;
  }}

  .issues-title {{
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: var(--text);
  }}

  .issues-count {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--accent);
  }}

  .issues-list {{
    display: flex;
    flex-direction: column;
    gap: 16px;
  }}

  .issue-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 28px 32px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .issue-card::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    background: var(--border);
    transition: background 0.3s;
  }}

  .issue-card:hover {{
    border-color: var(--border-light);
    transform: translateX(8px);
  }}

  .issue-card.sev-high::before {{ background: var(--high); }}
  .issue-card.sev-medium::before {{ background: var(--medium); }}
  .issue-card.sev-low::before {{ background: var(--low); }}

  .issue-card.sev-high:hover {{ border-color: var(--high); }}
  .issue-card.sev-medium:hover {{ border-color: var(--medium); }}
  .issue-card.sev-low:hover {{ border-color: var(--low); }}

  .issue-header {{
    display: flex;
    align-items: start;
    gap: 20px;
    margin-bottom: 16px;
  }}

  .issue-icon {{
    font-size: 28px;
    flex-shrink: 0;
    line-height: 1;
  }}

  .issue-content {{
    flex: 1;
  }}

  .issue-title {{
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 4px;
  }}

  .issue-desc {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.5;
  }}

  .issue-meta {{
    display: flex;
    align-items: center;
    gap: 20px;
  }}

  .issue-count {{
    font-family: 'Syne', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: var(--text);
  }}

  .issue-severity {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 12px;
    border-radius: 2px;
  }}

  .issue-severity.sev-high {{ background: var(--high-bg); color: var(--high); }}
  .issue-severity.sev-medium {{ background: var(--medium-bg); color: var(--medium); }}
  .issue-severity.sev-low {{ background: var(--low-bg); color: var(--low); }}

  .issue-lines {{
    margin-top: 16px;
    padding: 12px 16px;
    background: var(--surface-elevated);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--text-secondary);
  }}

  .issue-lines span {{
    color: var(--accent);
  }}

  .footer {{
    margin-top: 100px;
    padding-top: 40px;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .footer-brand {{
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
  }}

  .footer-tech {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--text-secondary);
  }}

  @keyframes fadeInUp {{
    from {{
      opacity: 0;
      transform: translateY(20px);
    }}
    to {{
      opacity: 1;
      transform: translateY(0);
    }}
  }}

  .page > * {{
    animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    opacity: 0;
  }}

  .page > *:nth-child(1) {{ animation-delay: 0.1s; }}
  .page > *:nth-child(2) {{ animation-delay: 0.2s; }}
  .page > *:nth-child(3) {{ animation-delay: 0.3s; }}
  .page > *:nth-child(4) {{ animation-delay: 0.4s; }}
  .page > *:nth-child(5) {{ animation-delay: 0.5s; }}

  .issue-card {{
    animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    opacity: 0;
  }}

  @media (max-width: 768px) {{
    .header {{
      grid-template-columns: 1fr;
      gap: 24px;
    }}

    .score-section {{
      grid-template-columns: 1fr;
    }}

    .score-section::before {{
      display: none;
    }}

    .score-left {{
      padding-right: 0;
      position: static;
    }}

    .score-right {{
      padding-left: 0;
    }}

    .stats-container {{
      grid-template-columns: 1fr;
    }}

    .severity-bar {{
      flex-direction: column;
    }}

    .issue-header {{
      flex-wrap: wrap;
    }}
  }}
</style>
</head>
<body>
<div class="page">

  <header class="header">
    <div class="header-main">
      <div class="header-tag">Data Quality Report</div>
      <h1>Validação de<br><span>Transações</span></h1>
      <div class="header-meta">
        <span>Gerado em {now}</span>
        <span>data/transacoes_ficticias_raw.xlsx</span>
      </div>
    </div>
  </header>

  <section class="score-section">
    <div class="score-left">
      <div class="score-display">
        <div class="score-number">{quality_score}%</div>
        <div class="score-label">Quality Score</div>
        <div class="score-status">{"Crítica" if quality_score < 70 else "Moderada" if quality_score < 90 else "Boa"}</div>
      </div>
    </div>
    <div class="score-right">
      <p class="score-description">
        <em>{affected_rows}</em> de {total} registros apresentam problemas de qualidade.
        {total_problems} ocorrências distribuídas em {len(issues)} categorias.
      </p>
    </div>
  </section>

  <div class="stats-container">
    <div class="stat-item">
      <div class="stat-value">{total}</div>
      <div class="stat-label">Registros</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">{affected_rows}</div>
      <div class="stat-label">Com Problemas</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">{total_problems}</div>
      <div class="stat-label">Ocorrências</div>
    </div>
  </div>

  <div class="severity-bar">
    <div class="severity-item sev-high">
      <div class="severity-count">{sev_counts["high"]}</div>
      <div class="severity-label">Alta</div>
    </div>
    <div class="severity-item sev-medium">
      <div class="severity-count">{sev_counts["medium"]}</div>
      <div class="severity-label">Média</div>
    </div>
    <div class="severity-item sev-low">
      <div class="severity-count">{sev_counts["low"]}</div>
      <div class="severity-label">Baixa</div>
    </div>
  </div>

  <section class="issues-section">
    <div class="issues-header">
      <h2 class="issues-title">Problemas</h2>
      <span class="issues-count">{len(cards)} categorias</span>
    </div>
    <div class="issues-list">
"""

for i, c in enumerate(cards):
    lines_str = ", ".join(str(l) for l in c["lines"])
    if len(c["lines"]) < c["count"]:
        lines_str += "..."
    sev_label = {"high": "Alta", "medium": "Média", "low": "Baixa"}[c["severity"]]
    html += f"""
    <div class="issue-card sev-{c["severity"]}" style="animation-delay: {0.1 + i * 0.05}s">
      <div class="issue-header">
        <span class="issue-icon">{c["icon"]}</span>
        <div class="issue-content">
          <h3 class="issue-title">{c["label"]}</h3>
          <p class="issue-desc">{c["desc"]}</p>
        </div>
        <div class="issue-meta">
          <span class="issue-count">{c["count"]}</span>
          <span class="issue-severity sev-{c["severity"]}">{sev_label}</span>
        </div>
      </div>
      <div class="issue-lines">
        <span>Linhas:</span> {lines_str}
      </div>
    </div>"""

html += """
    </div>
  </section>

  <footer class="footer">
    <span class="footer-brand">transaction-validator v2.0</span>
    <span class="footer-tech">python · pandas · openpyxl</span>
  </footer>

</div>
</body>
</html>"""

with open("output/relatorio_qualidade.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Relatório gerado com sucesso!")
