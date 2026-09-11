# Real-Life English — Volume 1 · Landing page de vendas

Página de vendas pronta pra lançar. HTML, CSS e JavaScript puros: sem build,
sem npm, sem framework. Você abre o `index.html` no navegador e ela funciona.

```
landing/
├── index.html            ← a página
├── termos.html           ← modelo a preencher
├── privacidade.html      ← modelo a preencher
├── assets/
│   ├── css/styles.css    ← todo o visual
│   ├── js/main.js        ← configuração + interações
│   └── img/              ← suas imagens (ver IMAGENS.md)
├── IMAGENS.md            ← o que eu preciso que você gere
└── README.md             ← este arquivo
```

---

## Antes de publicar — checklist

Quatro coisas são obrigatórias. O resto é melhoria.

### 1. Link do checkout — **obrigatório**

`assets/js/main.js`, primeiras linhas:

```js
var CONFIG = {
  checkoutUrl: '',   // ← cole aqui o link da Hotmart/Kiwify
```

Enquanto estiver vazio, todos os botões de compra levam pra seção de preço (a
página não quebra). Com o link preenchido, eles abrem o checkout numa aba nova.
**Um lugar só** — os cinco botões da página pegam daqui.

### 2. Preço — **obrigatório**

`index.html`, procure por `EDITAR: preço`:

```html
<div class="price__now" data-price><small>R$</small>47</div>
```

O `47` é valor de exemplo — troque pelo seu. A barra fixa do celular copia esse
valor sozinha, não precisa editar em dois lugares.

> Se você quiser mostrar preço riscado ("de R$ 97 por R$ 47"), só use um valor
> que você **realmente praticou** antes. Preço-âncora inventado é infração ao
> Código de Defesa do Consumidor, e as plataformas derrubam página por isso.
> Por padrão deixei sem, justamente pra não te expor.

### 3. Imagens — **obrigatório**

Veja o `IMAGENS.md`. São 9 arquivos, com prompt pronto pra cada um. Sem eles a
página mostra retângulos tracejados escrito "IMAGEM" — funciona, mas não vende.

As duas essenciais são a **capa em mockup 3D** e o **livro aberto**.

### 4. Domínio e e-mail — **obrigatório**

`index.html`, no `<head>` e no rodapé, troque:

- `https://seudominio.com.br` → seu domínio real (aparece 2×, nas tags de
  compartilhamento)
- `contato@seudominio.com.br` → seu e-mail real

### 5. Termos e privacidade

`termos.html` e `privacidade.html` são **esqueletos com os títulos certos e
lacunas marcadas** — não são texto jurídico pronto. Preencha antes de
publicar; Hotmart e Kiwify exigem as duas páginas.

### 6. Depoimentos

A seção `#depoimentos` está com espaço reservado. Duas opções:

- **Tem depoimento real?** Substitua o texto, o nome e a cidade, remova a
  classe `quote--empty` de cada card e apague o parágrafo `editor-note`.
- **Não tem ainda?** Apague a `<section id="depoimentos">` inteira. Melhor
  nenhuma prova social do que prova social falsa.

---

## Onde hospedar

Qualquer hospedagem de site estático serve. Do mais fácil pro mais controlado:

| Opção | Como | Custo |
|-------|------|-------|
| **Netlify Drop** | Arraste a pasta `landing/` em [app.netlify.com/drop](https://app.netlify.com/drop) | grátis |
| **Vercel** | `vercel` na pasta, ou conecte o GitHub | grátis |
| **Cloudflare Pages** | Conecte o repositório, pasta raiz `landing` | grátis |
| **Hospedagem própria** | Suba os arquivos por FTP na pasta pública | varia |
| **Página da Hotmart** | Só se você não quiser domínio próprio — você perde o controle do visual | incluso |

Depois, aponte seu domínio e ative o HTTPS (todas as três primeiras fazem isso
sozinhas).

**Testar antes:** abra o `index.html` com dois cliques. Pra testar igual ao
servidor de verdade, rode na pasta `landing/`:

```bash
python3 -m http.server 8000
# depois abra http://localhost:8000
```

---

## Como a página está montada

A ordem das seções segue a lógica de uma página de vendas: dor → solução →
prova → oferta → objeção → fechamento.

| # | Seção | O que faz |
|---|-------|-----------|
| 1 | Topo (hero) | Promessa + 3 benefícios + dois botões |
| 2 | Problema | "Você sabe as regras, mas trava" — identificação |
| 3 | **A história** | Demonstração ao vivo do toque-pra-traduzir |
| 4 | Diferenciais | Os 4 motivos de não ser mais um material |
| 5 | O que vem dentro | Lista dos 7 entregáveis |
| 6 | Capítulos | Os 7 capítulos, 40 histórias |
| 7 | Pra quem é | Os 3 perfis de leitor |
| 8 | Tutor de IA | Como funciona + prompt de exemplo |
| 9 | Depoimentos | (espaço reservado) |
| 10 | Autor | Sua história em 3 parágrafos |
| 11 | Oferta | Preço, o que inclui, garantia |
| 12 | Dúvidas | 7 perguntas frequentes |
| 13 | Fechamento | Última chamada |

### A demonstração ao vivo (seção 3)

É a peça mais importante da página. Em vez de *dizer* que tem tradução em um
toque, ela **deixa a pessoa experimentar** ali mesmo: duas histórias reais do
livro em que qualquer palavra é clicável, com tradução e classe gramatical.

O dicionário está em `assets/js/main.js`, no objeto `DICT`:

```js
'coffee': ['café', 'substantivo'],
```

Pra trocar as histórias da demonstração: edite os parágrafos
`.story__text` no HTML e acrescente ao `DICT` as palavras novas. Palavra que
não estiver no dicionário fica como texto comum, sem quebrar nada. Expressões
de mais de uma palavra (`boarding pass`, `thank you`) precisam ser envolvidas
em `<span data-ph>` no HTML.

> **Grave essa tela em vídeo.** Você mesmo escreveu que o toque-pra-traduzir é
> o conteúdo mais forte pras redes. Um Reels de 8 segundos tocando nas palavras
> desta seção explica o produto inteiro sem uma palavra de narração.

---

## Identidade visual

| | |
|---|---|
| Azul-noite (fundo) | `#0D1826` |
| Azul elevado (cards) | `#132234` |
| Âmbar (acento) | `#E0A53F` |
| Papel quente (faixa clara) | `#F3EADA` |
| Texto secundário | `#9DAFC6` |

**Tipografia:** Fraunces (títulos, serifada com um toque de imperfeição
proposital) · Karla (texto) · IBM Plex Mono (rótulos, códigos, dados do
"bilhete"). Todas do Google Fonts, já carregadas.

**Conceito:** diário de viagem à noite. O fundo é o voo; a seção da história é
a página de papel do diário aberto no colo; a oferta é um cartão de embarque
com picote e perfuração. Os números dos capítulos são carimbos de passaporte.

Pra mudar as cores, mexa só no bloco `:root` do `styles.css` — a página inteira
puxa de lá.

---

## Detalhes que já estão resolvidos

- **Responsivo** de 320 px a telona, com barra fixa de compra no celular
- **Acessível**: navegação por teclado, foco visível, `prefers-reduced-motion`
- **Sem dependência externa** além das fontes do Google
- **Carrega rápido**: zero framework, zero biblioteca
- **Placeholders inteligentes**: os retângulos de imagem somem sozinhos quando
  o arquivo com o nome certo aparece na pasta
- **Tags de compartilhamento** (Open Graph) prontas — falta só o domínio

---

## O que ainda falta (fora desta página)

Da sua lista original, o que não é trabalho de landing page:

- [ ] Revisar o Volume 1 completo e testar os cliques no celular
- [ ] Gerar as ilustrações internas dos capítulos
- [ ] Montar a versão PDF
- [ ] Conferir os direitos de uso das imagens de IA nos termos vigentes
- [ ] Criar a comunidade (Hotmart Club / Circle / Kiwify)
- [ ] Definir o preço final
- [ ] Subir o produto na Hotmart e/ou Kiwify
