#!/usr/bin/env bash
# =============================================================================
# conferir-landing.sh — trava de segurança antes de publicar
#
# Roda sozinho, sem instalar nada. Confere que a pasta landing/ continua
# sendo o que a gente combinou que ela é: uma página estática, sem nenhuma
# dependência de terceiro, sem nenhum ponto onde texto vira HTML, sem
# documentação interna e sem arquivo nenhum sobrando.
#
#   bash scripts/conferir-landing.sh
#
# Sai com código 0 se estiver tudo certo, 1 se achar qualquer problema.
# Vale rodar toda vez que mexer na página, principalmente depois de colar
# algum script novo (pixel de anúncio, ferramenta de análise).
# =============================================================================
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE="$RAIZ/landing"

# O domínio do site. Referência a qualquer outro host é apontada.
DOMINIO_PROPRIO="${DOMINIO_PROPRIO:-seudominio.com.br}"

falhas=0
avisos=0

ok()    { printf '  \033[32mok\033[0m    %s\n' "$1"; }
falha() { printf '  \033[31mFALHA\033[0m %s\n' "$1"; falhas=$((falhas + 1)); }
aviso() { printf '  \033[33maviso\033[0m %s\n' "$1"; avisos=$((avisos + 1)); }
titulo(){ printf '\n\033[1m%s\033[0m\n' "$1"; }

[ -d "$SITE" ] || { echo "Pasta landing/ não encontrada em $RAIZ"; exit 1; }

# -----------------------------------------------------------------------------
titulo "1. Dependências de terceiros"
# -----------------------------------------------------------------------------
externos=$(grep -rhoE "https?://[a-zA-Z0-9._-]+" "$SITE" \
  --include=*.html --include=*.css --include=*.js --include=*.json 2>/dev/null \
  | sed -E 's#https?://##' | sort -u \
  | grep -vE "^(${DOMINIO_PROPRIO//./\\.}|openapi\.vercel\.sh|securityheaders\.com)$" || true)

if [ -z "$externos" ]; then
  ok "nenhum host externo referenciado — a página carrega 100% do próprio domínio"
else
  falha "host externo encontrado (cada um é um terceiro que enxerga seu visitante):"
  printf '        %s\n' $externos
fi

if [ -e "$SITE/package.json" ] || [ -d "$SITE/node_modules" ]; then
  falha "existe package.json ou node_modules em landing/ — a página não deve ter dependências"
else
  ok "sem package.json e sem node_modules — não há o que escanear nem o que atualizar"
fi

# -----------------------------------------------------------------------------
titulo "2. Pontos onde texto poderia virar HTML ou código"
# -----------------------------------------------------------------------------
sinks=$(grep -rnE "\.(innerHTML|outerHTML)[[:space:]]*=|insertAdjacentHTML|document\.write|[^a-zA-Z](eval|Function)[[:space:]]*\(" \
  "$SITE"/assets/js/*.js 2>/dev/null | grep -vE "^\s*[0-9]+:\s*(//|\*)" || true)
if [ -z "$sinks" ]; then
  ok "nenhum innerHTML, eval, document.write ou insertAdjacentHTML no JavaScript"
else
  falha "sink de HTML/código no JavaScript:"
  printf '        %s\n' "$sinks"
fi

# Duas buscas separadas de propósito: juntar as duas em um grep só exigiria
# misturar -E com -P, e o grep recusa os dois ao mesmo tempo. Quando isso
# acontece a saída vem vazia e a checagem passa sem ter rodado.
script_inline=$(grep -rn "<script" "$SITE"/*.html 2>/dev/null | grep -v "src=" || true)
if [ -z "$script_inline" ]; then
  ok "nenhum <script> inline no HTML — todo JavaScript vem de arquivo próprio"
else
  falha "script inline no HTML (a CSP vai bloquear em produção):"
  printf '        %s\n' "$script_inline"
fi

estilo_inline=$(grep -rnE "<style|[[:space:]]style=" "$SITE"/*.html 2>/dev/null || true)
if [ -z "$estilo_inline" ]; then
  ok "nenhum estilo inline no HTML — a CSP bloqueia <style> e style=, então isso apareceria sem formatação no ar"
else
  falha "estilo inline no HTML (a CSP vai bloquear e a página aparece torta):"
  printf '        %s\n' "$estilo_inline"
fi

handlers=$(grep -rnE "[[:space:]]on[a-z]+[[:space:]]*=" "$SITE"/*.html 2>/dev/null || true)
if [ -z "$handlers" ]; then
  ok "nenhum manipulador onclick=/onload= no HTML"
else
  falha "atributo on...= no HTML (a CSP vai bloquear em produção):"
  printf '        %s\n' "$handlers"
fi

# -----------------------------------------------------------------------------
titulo "3. Arquivos que não podem ser publicados"
# -----------------------------------------------------------------------------
vazamentos=$(find "$SITE" \( -name "*.md" -o -name "*.markdown" -o -name "*.env*" \
  -o -name "*.pem" -o -name "*.key" -o -name "*.map" -o -name "*.sql" \
  -o -name "*.bak" -o -name "*~" -o -name ".DS_Store" \) 2>/dev/null || true)
if [ -z "$vazamentos" ]; then
  ok "nenhuma documentação interna, chave, sourcemap ou arquivo temporário na pasta publicada"
else
  falha "arquivo que ficaria público na internet:"
  printf '        %s\n' $vazamentos
fi

segredos=$(grep -rnIE "(api[_-]?key|client[_-]?secret|bearer |AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,})" \
  "$SITE" 2>/dev/null || true)
if [ -z "$segredos" ]; then
  ok "nenhum padrão de chave ou token no conteúdo publicado"
else
  falha "possível segredo na pasta publicada:"
  printf '        %s\n' "$segredos"
fi

# -----------------------------------------------------------------------------
titulo "4. Política de segurança consistente"
# -----------------------------------------------------------------------------
politicas=$(grep -rhoE "default-src 'self'[^\"]*" "$SITE"/*.html 2>/dev/null | sort -u | wc -l)
paginas=$(ls "$SITE"/*.html 2>/dev/null | wc -l)
com_csp=$(grep -lE "Content-Security-Policy" "$SITE"/*.html 2>/dev/null | wc -l)

if [ "$com_csp" -eq "$paginas" ] && [ "$politicas" -eq 1 ]; then
  ok "as $paginas páginas carregam a mesma CSP, também no <meta> (vale mesmo sem os cabeçalhos do servidor)"
else
  falha "CSP ausente ou diferente entre páginas ($com_csp de $paginas páginas, $politicas políticas distintas)"
fi

for cabecalho in Content-Security-Policy X-Frame-Options X-Content-Type-Options \
                 Referrer-Policy Permissions-Policy Strict-Transport-Security \
                 Cross-Origin-Opener-Policy; do
  if grep -q "$cabecalho" "$SITE/_headers" && grep -q "$cabecalho" "$SITE/vercel.json"; then
    ok "$cabecalho presente nos dois arquivos de hospedagem"
  else
    falha "$cabecalho faltando em _headers ou em vercel.json"
  fi
done

# -----------------------------------------------------------------------------
titulo "5. Arquivos que a página pede e precisam existir"
# -----------------------------------------------------------------------------
faltando=0
while read -r ref; do
  [ -z "$ref" ] && continue
  case "$ref" in http*|//*|\#*|mailto:*|data:*) continue ;; esac
  alvo="$SITE/${ref%%\?*}"
  if [ ! -e "$alvo" ]; then
    falha "referenciado no HTML mas não existe: $ref"
    faltando=$((faltando + 1))
  fi
done < <(grep -rhoE '(href|src)="[^"]+"' "$SITE"/*.html | sed -E 's/^(href|src)="//; s/"$//' | sort -u)
[ "$faltando" -eq 0 ] && ok "todo arquivo pedido pelo HTML existe — nenhum 404 de imagem, css ou fonte"

# -----------------------------------------------------------------------------
titulo "6. Pendências antes de publicar"
# -----------------------------------------------------------------------------
if grep -rq "seudominio.com.br" "$SITE" 2>/dev/null; then
  aviso "ainda existe 'seudominio.com.br' na pasta — trocar pelo domínio real antes de publicar"
else
  ok "domínio real já preenchido"
fi

if grep -qE "checkoutUrl: *''" "$SITE/assets/js/main.js" 2>/dev/null; then
  aviso "checkoutUrl vazio — os botões estão levando para a seção de preço, não para o pagamento"
else
  ok "checkoutUrl preenchido"
fi

# -----------------------------------------------------------------------------
printf '\n'
if [ "$falhas" -eq 0 ]; then
  printf '\033[32m%s\033[0m\n' "Nenhuma falha. $avisos aviso(s) para resolver antes de publicar."
  exit 0
else
  printf '\033[31m%s\033[0m\n' "$falhas falha(s) e $avisos aviso(s). Resolva as falhas antes de publicar."
  exit 1
fi
