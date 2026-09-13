# Imagens da página — o que já tem e o que falta

## ⬇️ Baixe tudo de uma vez

As oito imagens estão prontas, num único zip:

**https://d2ol7oe51mr4n9.cloudfront.net/user_3Gz71cp9ZtxZzUxgVU953G5NBJr/83f26861-68cc-4204-be18-2a03270ddddb.zip**

Descompacte e arraste os arquivos (menos o `LEIA-ME.txt`) para
`landing/assets/img/`. Os nomes já estão como a página espera — os retângulos
tracejados somem sozinhos. A sua foto (`autor.jpg`) já está na pasta e não
vem no zip.

**O fundo do `hero-book` já foi recortado** — ele vem transparente, não
precisa passar por removedor.


Onde falta arte, a página mostra um **retângulo tracejado** com o nome do
arquivo e o tamanho. Salve a imagem com o nome exato em
`landing/assets/img/` e o placeholder some sozinho.

**Atenção:** o fundo da página é quase-preto quente. Arte clara ou azulada
não casa — tudo tem que ser escuro e de luz quente.

**Paleta:** void `#08080A` · âmbar `#E0A53F` · esmeralda `#4FBE87`

---

## Resumo — 8 arquivos

| # | Arquivo | Tamanho | Formato | Onde | Prioridade |
|---|---------|---------|---------|------|------------|
| 1 | `hero-book.webp` | 900 px larg. | WebP transparente | Palco do topo | ✅ **pronta, já recortada** |
| 2 | `livro-aberto.webp` | 1800 × 1150 | WebP | "Mais sobre o Volume 1" | ✅ pronta |
| 3 | `retrato-01.webp` | 700 × 700 | WebP (fundo preto serve) | Perfil Marina | ✅ pronta |
| 4 | `retrato-02.webp` | 700 × 700 | WebP (fundo preto serve) | Perfil Rafael | ✅ pronta |
| 5 | `retrato-03.webp` | 700 × 700 | WebP (fundo preto serve) | Perfil Célia | ✅ pronta |
| 6 | `autor.jpg` | 800 × 800 | JPG | "Oi, eu sou o Gui" | ✅ **pronta, já na pasta** |
| 7 | `og-image.jpg` | 1200 × 630 | JPG | Prévia no WhatsApp | ⚠️ base pronta, **falta o texto** |
| 8 | `favicon.png` | 256 × 256 | PNG | Ícone da aba | ✅ pronta |

---

## 1. `hero-book.png` — o livro no palco · 1200 × 1500 · PNG **transparente**

Aqui o livro é iluminado como joia em vitrine: fundo quase-preto, luz âmbar
vindo de cima. Quanto mais contraste e brilho especular na capa, melhor.

```
A 3D book mockup floating at a slight three-quarter angle, front cover facing
the viewer. Dramatic studio lighting: a warm amber key light from the upper
left, a soft cool rim light on the right edge, deep falloff into darkness.
Glossy cover with visible specular highlights. Isolated on a fully transparent
background. Premium product photography, sharp focus, high contrast,
cinematic.
```

> ⚠️ **Fundo transparente é obrigatório.** Fundo branco vira um retângulo
> branco no meio do preto.

---

## 2. `livro-aberto.jpg` — o livro aberto · 1800 × 1150 · JPG (bem horizontal)

Esta é a imagem mais importante da versão 2. Ela recebe dois painéis por cima
(o argumento à esquerda, o sumário dourado à direita), então precisa ser
**escura e vazia no meio**, com o livro ocupando a largura toda.

```
An open book photographed from directly above, lying on a dark walnut surface.
Warm amber light falling across the pages from the left, deep shadows at the
edges. A dried palm leaf and a small brass compass resting beside it.
Very dark, moody, cinematic, high contrast. The pages are warm cream. Wide
horizontal framing with the book filling the frame edge to edge.
```

**Se ficar clara demais**, escureça no Canva (brilho −20, contraste +15) ou
peça "darker, more shadow, low key lighting" no prompt. Os painéis brancos e
dourados precisam de fundo escuro pra respirar.

---

## 3, 4, 5. `retrato-01/02/03.png` — os três perfis · 700 × 700 · PNG **transparente**

Diferente da v1 (que pedia foto), aqui são **ilustrações em linha**, como na
referência que você me mandou: traço fino, contínuo, sobre transparente.
Fica muito mais coeso com o preto brilhante do que foto de banco de imagem.

**Base de prompt** (troque só a descrição):
```
A single-line contour illustration of a person's head and shoulders in
profile, drawn with one continuous thin white line. Minimalist, elegant,
no shading, no fill. Fully transparent background. Modern editorial
illustration style, clean and confident linework.
```

- **`retrato-01`** — Marina, 27 anos, mulher jovem de perfil, cabelo preso,
  mochila na alça do ombro
- **`retrato-02`** — Rafael, 34 anos, homem de perfil, barba curta, fone de
  ouvido no pescoço
- **`retrato-03`** — Célia, 58 anos, mulher de perfil, cabelo curto, óculos
  de leitura

> Peça **três de uma vez, no mesmo prompt-base**, pra o traço ficar igual nas
> três. Traço diferente entre os cards estraga o conjunto.
>
> Se a IA insistir em colocar fundo, gere em branco sobre preto e remova o
> fundo depois (o Canva faz, e o remove.bg também).

---

## 6. `autor.jpg` — sua foto · 800 × 800 · JPG ✅ **feita**

Já está em `assets/img/autor.jpg`. O que foi feito com a foto que você mandou:

- Recorte quadrado de 1530 × 1530 da original (1932 × 2576), do topo da
  cabeça até o peito, com o rosto centralizado
- Redimensionada para 800 × 800
- JPEG progressivo, qualidade 88 — **112 KB**, bem abaixo do limite de 300 KB

**Ela caiu bem por acaso:** a luz âmbar do ambiente onde a foto foi tirada é
quase a mesma cor do acento da marca (`#E0A53F`). Foto de luz fria ou de
fundo branco teria brigado com a página; essa conversa com ela.

A moldura de vidro — fio de luz no topo e sombra profunda — vem do CSS, na
regra `.author__grid .slot`. É a mesma dos outros cards, pra foto não ficar
um retângulo solto no meio da página.

> **Se um dia trocar a foto:** mantenha o nome `autor.jpg`, corte em quadrado
> e prefira ambiente de luz quente com fundo escuro. Fundo branco estourado
> vai brigar com o resto.

---

## 7. `og-image.jpg` — prévia de compartilhamento · 1200 × 630 · JPG

O cartãozinho que aparece quando colam o link no WhatsApp. Monte no Canva
com fundo `#08080A`:
- Capa do livro à direita, com um brilho âmbar atrás
- À esquerda: **REAL-LIFE ENGLISH** em caixa alta, larga e pesada +
  *Histórias para aprender inglês de verdade* + selo `VOLUME 1 · A1–A2`
- Nada de texto pequeno — no WhatsApp isso vira miniatura

---

## 8. `favicon.png` — ícone da aba · 512 × 512 · PNG

As iniciais **GJ** em âmbar sobre o quase-preto, no mesmo desenho do marcador
redondo do menu. Legível a 16 px.

---

## Como salvar

```
landing/assets/img/
├── hero-book.png
├── livro-aberto.jpg
├── retrato-01.png
├── retrato-02.png
├── retrato-03.png
├── autor.jpg
├── og-image.jpg
└── favicon.png
```

Nome exato, minúsculo, sem acento e sem espaço. Depois comprima tudo em
[squoosh.app](https://squoosh.app) — mire em menos de 300 KB por imagem.
