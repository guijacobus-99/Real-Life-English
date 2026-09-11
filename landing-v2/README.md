# Real-Life English — Volume 1 · Landing page **versão 2 "Vitrine"**

Segunda versão da página de vendas, no registro que você pediu: escuro,
brilhante, pesado — vitrine de produto. HTML, CSS e JavaScript puros, sem
build.

> A versão 1 continua em `landing/`. **As duas são completas e independentes.**
> Escolha uma e apague a outra antes de publicar — ou teste as duas e veja
> qual converte melhor.

---

## O que muda da v1 pra v2

| | v1 — "Diário de viagem" | v2 — "Vitrine" |
|---|---|---|
| **Fundo** | azul-noite `#0D1826` | quase-preto quente `#08080A` |
| **Sensação** | íntimo, artesanal, editorial | caro, brilhante, produto em exposição |
| **Tipos** | Fraunces (serifada) + Karla | Archivo expandida + Manrope |
| **Menu** | barra colada no topo | pílula de vidro flutuante |
| **Botões** | gradiente suave | verniz especular, brilho âmbar |
| **Peça central** | história em papel creme | livro aberto com painéis sobrepostos |
| **Sumário** | lista de capítulos escura | painel dourado em cima da foto |
| **Perfis** | fotos de pessoas | ilustrações em linha |
| **Oferta** | cartão de embarque com picote | cartão de vidro com lateral iluminada |
| **Bônus/vagas** | não tem | bloco de vagas com barra |

**O que é igual nas duas:** a copy, os 7 capítulos, os 3 perfis, a garantia de
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

### 3. Bloco de vagas — **decida antes de publicar**

O topo tem um bloco de bônus com contador de vagas, igual à referência que
você mandou. Ele é controlado em `assets/js/main.js`:

```js
spotsTotal: 50,
spotsLeft: 50
```

**Três caminhos honestos:**

- **Vai mesmo dar a conversa de 15 min pras 50 primeiras?** Deixe o bloco e
  atualize o `spotsLeft` de verdade conforme as vagas forem indo.
- **Vai dar o bônus, mas sem contador?** Apague a `<div class="bonus__count">`
  e a `<div class="bonus__bar">`, mantenha o texto.
- **Não vai dar bônus nenhum?** Apague a `<div class="bonus">` inteira.

O que não dá é deixar um número parado fingindo que está acabando. Escassez
falsa é infração ao CDC, as plataformas derrubam a página, e o público sente.

### 4. Imagens — **obrigatório**

Veja o `IMAGENS.md`. **São diferentes das da v1**: o livro aberto precisa ser
horizontal e escuro, e os perfis são ilustrações em linha, não fotos. Quatro
arquivos servem nas duas versões e podem ser copiados.

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

Qualquer hospedagem estática. A mais rápida: arraste a pasta `landing-v2/` em
[app.netlify.com/drop](https://app.netlify.com/drop). Vercel e Cloudflare
Pages também servem, de graça.

Testar local, dentro de `landing-v2/`:

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

**Tipografia:** Archivo em largura expandida (títulos e logotipo — é ela que
dá o peso) · Manrope (texto) · IBM Plex Mono (rótulos e dados).

**Como o brilho é feito:** todo card de vidro tem um fio de luz de 1 px no
topo (`inset 0 1px 0 rgba(255,255,255,.1)`) e sombra profunda embaixo. O botão
tem um verniz especular na metade de cima. É essa dupla que dá o aspecto de
objeto físico em vez de retângulo colorido.

Pra mudar as cores, mexa só no bloco `:root` do `styles.css`.

---

## Detalhes já resolvidos

- Responsivo de 320 px a telona, com barra fixa de compra no celular
- No celular os cartões "antes/depois" saem de cima do livro e viram uma
  linha embaixo; o sumário dourado sai de cima da foto e vira um painel
- Acessível: navegação por teclado, foco visível, `prefers-reduced-motion`
- Sem dependência externa além das fontes do Google
- Placeholders de imagem que somem sozinhos quando o arquivo aparece
- Tags de compartilhamento prontas — falta só o domínio
