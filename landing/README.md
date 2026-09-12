# Real-Life English — Volume 1 · Landing page

Página de vendas do ebook, no registro "Vitrine": escuro, brilhante, pesado —
produto em exposição. HTML, CSS e JavaScript puros, sem build, sem npm. Você
abre o `index.html` no navegador e ela funciona.

```
landing/
├── index.html            ← a página
├── termos.html           ← modelo a preencher
├── privacidade.html      ← modelo a preencher
├── assets/
│   ├── css/styles.css    ← o visual
│   ├── css/motion.css    ← a camada de movimento
│   ├── js/main.js        ← configuração + interações
│   ├── js/motion.js      ← movimento que o CSS não faz sozinho
│   └── img/              ← as imagens (ver IMAGENS.md)
├── IMAGENS.md            ← o que ainda falta gerar
└── README.md             ← este arquivo
```

---

## Histórico: houve uma primeira versão

Antes desta, existiu uma versão "Diário de viagem" — azul-noite, tipografia
serifada, oferta em formato de cartão de embarque. Ela foi descartada em
favor desta, mas **continua no histórico do Git** e pode ser recuperada a
qualquer momento:

```bash
git checkout 7018664 -- landing/     # traz a v1 de volta como pasta
```

O que mudou de uma pra outra:

| | v1 — "Diário de viagem" (descartada) | Esta — "Vitrine" |
|---|---|---|
| **Fundo** | azul-noite `#0D1826` | quase-preto quente `#08080A` |
| **Sensação** | íntimo, artesanal, editorial | caro, brilhante, produto em exposição |
| **Tipos** | Fraunces (serifada) + Karla | Geist + Geist Mono |
| **Menu** | barra colada no topo | pílula de vidro flutuante |
| **Botões** | gradiente suave | verniz especular, brilho âmbar |
| **Peça central** | história em papel creme | livro aberto com painéis sobrepostos |
| **Sumário** | lista de capítulos escura | painel dourado em cima da foto |
| **Perfis** | fotos de pessoas | ilustrações em linha |
| **Oferta** | cartão de embarque com picote | cartão de vidro com lateral iluminada |
| **Bônus** | não tinha | bloco de bônus de lançamento |
| **Movimento** | transições de hover | camada de movimento presa ao scroll |

**O que se manteve:** a copy, os 7 capítulos, os 3 perfis, a garantia de
7 dias, o FAQ, e a demonstração ao vivo do toque-pra-traduzir.

---

## Antes de publicar — checklist

### 1. Link do checkout — **obrigatório**

`assets/js/main.js`, primeiras linhas:

```js
var CONFIG = {
  checkoutUrl: '',   // ← cole aqui o link da Hotmart/Kiwify
```

Vazio, os botões levam pra seção de preço. Preenchido, abrem o checkout numa
aba nova. Um lugar só — os cinco botões puxam daqui.

### 2. Preço — **obrigatório**

`index.html`, procure por `EDITAR: preço`. O `47` é exemplo. A barra fixa do
celular copia esse valor sozinha.

### 3. Bloco de bônus — **decida antes de publicar**

O contador de vagas foi removido. Sobrou só a frase do bônus de lançamento,
no topo:

> As primeiras 50 compras levam uma conversa de 15 min comigo.

**Se você não vai dar esse bônus, apague a `<div class="bonus">` inteira.**
Promessa de bônus é oferta: uma vez publicada, quem comprar pode cobrar.

### 4. Imagens — **obrigatório**

Veja o `IMAGENS.md` — ele lista o que já foi gerado e o que ainda falta.

### 5. Domínio e e-mail — **obrigatório**

No `<head>` e no rodapé: `seudominio.com.br` → seu domínio real (aparece 2×),
`contato@seudominio.com.br` → seu e-mail real.

### 6. Termos e privacidade

`termos.html` e `privacidade.html` são **esqueletos com lacunas marcadas em
âmbar**, não texto jurídico pronto. Preencha antes de publicar — Hotmart e
Kiwify exigem as duas páginas.

### 7. Depoimentos

A seção `#depoimentos` está reservada. Ou você troca pelos depoimentos reais,
ou apaga a `<section id="depoimentos">` inteira.

---

## Onde hospedar

Qualquer hospedagem estática. A mais rápida: arraste a pasta `landing/` em
[app.netlify.com/drop](https://app.netlify.com/drop). Vercel e Cloudflare
Pages também servem, de graça.

Testar local, dentro de `landing/`:

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

---

## Como a página está montada

| # | Seção | O que faz |
|---|-------|-----------|
| 1 | Palco (hero) | Logotipo grande, 3 checks, botão brilhante, bloco de vagas, livro iluminado com os cartões "antes/depois" |
| 2 | Números | 40 · 7 · A1–A2 · 7 dias |
| 3 | Problema | "Você sabe as regras, mas trava" |
| 4 | **Mais sobre o Volume 1** | Foto do livro aberto com o argumento à esquerda e o sumário dourado à direita |
| 5 | **Experimente** | Demonstração ao vivo do toque-pra-traduzir |
| 6 | Pra quem é | Os 3 perfis com ilustração, dados e objetivo |
| 7 | O que vem dentro | 7 peças em grade |
| 8 | Tutor de IA | Prompt real com botão de copiar |
| 9 | Depoimentos | (reservado) |
| 10 | Autor | Sua história |
| 11 | Oferta | Preço, o que inclui, garantia |
| 12 | Dúvidas | 7 perguntas |
| 13 | Fechamento | Última chamada |

### Os dois momentos que carregam a página

**O palco do livro (seção 1).** O livro é iluminado por baixo com uma luz
âmbar difusa, e dois cartões flutuam ao redor mostrando a mesma pergunta —
*"What can I get you?"* — com duas respostas: a de antes (você trava) e a de
depois (você responde). É a promessa inteira em dois cartões, sem precisar
ler nada.

**O livro aberto (seção 4).** A foto recebe dois painéis por cima: à esquerda
o argumento de por que história funciona, à direita os 7 capítulos num painel
dourado com os números grandes e os vistos verdes. É a peça que você apontou
na referência, adaptada pra sua marca.

---

## Identidade visual

| | |
|---|---|
| Void (fundo) | `#08080A` |
| Painel | `#0B0B0E` |
| Vidro | branco a 4–8% sobre o fundo |
| Âmbar (acento) | `#E0A53F` |
| Esmeralda (confirmação) | `#4FBE87` |
| Texto secundário | `#A8A29B` |

**Tipografia: Geist e Geist Mono** — uma família só, para texto e títulos,
com a monoespaçada irmã nos rótulos. É a mesma lógica da Apple, que usa
SF Pro no texto e SF Mono nos dados: em vez de casar duas fontes de origens
diferentes, você usa dois membros da mesma casa e o conjunto fica coeso
sozinho.

A Geist é uma grotesca suíça de formas quadradas e terminais retos —
corporativa sem ser dura. O que faz ela parecer Apple não é o desenho da
letra, é o **tracking negativo nos títulos** (`-.032em`, e `-.045em` no
logotipo): título grande com letra apertada é a assinatura das páginas de
produto da Apple.

Também não tem mais nenhum `font-stretch`: era a largura esticada da fonte
anterior que dava aquele ar de gerador automático.

**Como o brilho é feito:** todo card de vidro tem um fio de luz de 1 px no
topo (`inset 0 1px 0 rgba(255,255,255,.1)`) e sombra profunda embaixo. O botão
tem um verniz especular na metade de cima. É essa dupla que dá o aspecto de
objeto físico em vez de retângulo colorido.

Pra mudar as cores, mexa só no bloco `:root` do `styles.css`.

---

## A camada de movimento

Vive em dois arquivos separados do resto, pra ser fácil de ajustar ou
desligar: `assets/css/motion.css` e `assets/js/motion.js`. **Pra desligar
tudo, apague as duas linhas que carregam esses arquivos no `index.html`** —
a página continua funcionando inteira, só parada.

**O conceito:** a luz percorre a página. Nada voa, nada pula, nada gira. O
que se move é a luz, a profundidade e o foco — mesmo princípio das páginas
de produto da Apple, onde o movimento dirige o olhar e você não consegue
apontar onde ele começa.

### O que acontece, na ordem

| Momento | O que se move |
|---|---|
| **Ao abrir** | Cascata curta: logotipo, frase, checks, botão e bônus entram em sequência; o livro sobe enquanto a luz acende atrás dele; os cartões "antes/depois" chegam por último, já inclinados |
| **Ao rolar o topo** | O livro sobe mais devagar que o texto e a luz atrás se abre — dois planos, duas velocidades, é isso que dá profundidade |
| **Em cada bloco** | Os elementos assentam ao entrar na tela, com cascata entre irmãos |
| **No livro aberto** | A foto entra, depois o painel do argumento, depois o sumário — e os sete vistos verdes acendem um a um conforme você desce |
| **O tempo todo** | Barra de progresso âmbar no topo e um fio de luz descendo pela lateral esquerda, ligando um bloco ao outro |
| **No cursor** | Um holofote suave segue o mouse dentro dos cards; o verniz do botão varre quando você passa por cima |

### Por que não trava a rolagem

O movimento por scroll usa **animação nativa presa ao scroll**
(`animation-timeline`), não JavaScript escutando evento de rolagem. Roda na
GPU, acompanha o dedo, e não dá aquele arrasto de página com parallax mal
feito.

### As três garantias

1. **Nada pode esconder conteúdo.** Todo o movimento de scroll está dentro de
   um `@supports`. Navegador que não entende recebe zero animação e mostra a
   página inteira montada. O padrão é "visível"; movimento é acréscimo.
2. **Quem pediu menos movimento não recebe nenhum.** Tudo está sob
   `prefers-reduced-motion: no-preference`. Quem liga a redução de movimento
   no sistema vê a página estática.
3. **Firefox não fica de fora.** Ele ainda não tem animação presa ao scroll,
   então a barra de progresso e o fio lateral caem num fallback em
   JavaScript. A abertura do topo e as interações de cursor funcionam em
   todos os navegadores de qualquer jeito.

Isso foi testado varrendo a página em 25 posições de parada, em três alturas
de tela (desktop, tela baixa e celular), conferindo se algum elemento ficava
semitransparente parado na frente do leitor. Nenhum ficou.

---

## Detalhes já resolvidos

- Responsivo de 320 px a telona, com barra fixa de compra no celular
- No celular os cartões "antes/depois" saem de cima do livro e viram uma
  linha embaixo; o sumário dourado sai de cima da foto e vira um painel
- Acessível: navegação por teclado, foco visível, `prefers-reduced-motion`
- Sem dependência externa além das fontes do Google
- Placeholders de imagem que somem sozinhos quando o arquivo aparece
- Movimento que respeita `prefers-reduced-motion` e nunca esconde conteúdo
- Tags de compartilhamento prontas — falta só o domínio
