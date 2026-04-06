# transaction-validator

Pipeline de validação de qualidade de dados transacionais, com implementações paralelas em **Python** e **Excel**.

O projeto parte de uma base fictícia com problemas intencionalmente inseridos, aplica regras de validação por ambas as abordagens e gera um relatório comparativo de qualidade.

---

## Contexto

Dados transacionais são frequentemente recebidos com inconsistências: campos nulos, formatos incorretos, registros duplicados, valores inválidos. Este projeto simula esse cenário e demonstra como identificar, classificar e reportar esses problemas de forma estruturada.

---

## Estrutura do projeto

```
transaction-validator/
├── data/
│   └── transacoes_ficticias_raw.xlsx     # Base original com problemas inseridos
├── scripts/
│   ├── validate_transactions.py          # Validação via Python — saída em terminal
│   └── generate_report.py               # Geração do relatório HTML
├── output/
│   └── relatorio_qualidade.html         # Relatório de qualidade
└── README.md
```

---

## Problemas inseridos na base

A base contém 200 registros com 10 tipos de problema distribuídos propositalmente:

| Linha | Problema                          | Categoria       |
|-------|-----------------------------------|-----------------|
| 11-12 | Linha completamente duplicada     | Integridade     |
| 11-12, 101-102 | ID de transação duplicado | Integridade  |
| 22    | CPF inválido (000.000.000-00)     | Conformidade    |
| 32    | Valor negativo                    | Regra de negócio|
| 42    | Data inválida (32/13/2024)        | Formato         |
| 52    | Status com capitalização incorreta| Padronização    |
| 62    | Valor nulo                        | Completude      |
| 72    | CPF sem formatação padrão         | Formato         |
| 82    | Nome do cliente vazio             | Completude      |
| 92    | Tipo de transação fora do padrão  | Conformidade    |

---

## Abordagem Python

### Execução

```bash
pip install pandas openpyxl
python scripts/validate_transactions.py data/transacoes_ficticias_raw.xlsx
```

### Lógica de validação

O script percorre os registros aplicando regras independentes por campo. Cada problema é registrado com a linha correspondente. Ao final, registros únicos afetados são consolidados para o cálculo do score.

**Duplicatas** — detectadas antes do loop com `DataFrame.duplicated()`, operando sobre a tabela inteira:

```python
df[df.duplicated(keep=False)]                          # linha completa
df[df.duplicated(subset=["id_transacao"], keep=False)] # somente ID
```

**CPF** — duas verificações em camadas:

```python
CPF_FORMATTED = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")  # estrutura
CPF_INVALID_KNOWN = {"000.000.000-00", ...}                   # conteúdo
```

**Data** — tentativa de parse em múltiplos formatos:

```python
for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
    datetime.strptime(str(val), fmt)
```

**Status** — separação entre capitalização incorreta e valor fora do padrão:

```python
if status.lower() in VALID_STATUS and status != status.lower():
    # ex: "APROVADO" — valor correto, formato incorreto
elif status.lower() not in VALID_STATUS:
    # ex: "aprovado123" — valor inexistente
```

### Resultado

| Métrica                  | Valor  |
|--------------------------|--------|
| Total de registros       | 200    |
| Registros com problema   | 12     |
| Score de qualidade       | 94.0%  |
| Categorias identificadas | 10     |

---

## Relatório

O arquivo `output/relatorio_qualidade.html` apresenta os resultados de forma visual, com detalhamento por categoria, severidade e linhas afetadas.

Abrir diretamente no navegador — não requer servidor.

---

## Tecnologias

- Python 3.x
- pandas
- openpyxl
- re (stdlib)
- datetime (stdlib)
- Microsoft Excel / LibreOffice Calc

---

## Autor

Gui Jacobus - [github.com/guijacobus-99](https://github.com/guijacobus-99)