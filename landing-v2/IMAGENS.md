# Imagens da versão 2 — o que eu preciso de você

Onde falta arte, a página mostra um **retângulo tracejado** com o nome do
arquivo e o tamanho. Salve a imagem com o nome exato em
`landing-v2/assets/img/` e o placeholder some sozinho.

**Atenção:** esta versão pede imagens **diferentes** da v1. O fundo aqui é
quase-preto quente, não azul-noite — arte clara ou azulada não casa.

**Paleta:** void `#08080A` · âmbar `#E0A53F` · esmeralda `#4FBE87`

---

## Resumo — 8 arquivos

| # | Arquivo | Tamanho | Formato | Onde | Prioridade |
|---|---------|---------|---------|------|------------|
| 1 | `hero-book.png` | 1200 × 1500 | PNG transparente | Palco do topo | **essencial** |
| 2 | `livro-aberto.jpg` | 1800 × 1150 | JPG | "Mais sobre o Volume 1" | **essencial** |
| 3 | `retrato-01.png` | 700 × 700 | PNG transparente | Perfil Marina | alta |
| 4 | `retrato-02.png` | 700 × 700 | PNG transparente | Perfil Rafael | alta |
| 5 | `retrato-03.png` | 700 × 700 | PNG transparente | Perfil Célia | alta |
| 6 | `autor.jpg` | 800 × 800 | JPG | "Oi, eu sou o Gui" | alta |
| 7 | `og-image.jpg` | 1200 × 630 | JPG | Prévia no WhatsApp | média |
| 8 | `favicon.png` | 512 × 512 | PNG | Ícone da aba | média |

Se você já gerou as imagens da v1, o `hero-book.png`, o `autor.jpg`, o
`og-image.jpg` e o `favicon.png` **servem nas duas** — é só copiar.

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

## 6. `autor.jpg` — sua foto · 800 × 800 · JPG

**Foto sua de verdade**, nada de IA — é a seção de confiança.

Nesta versão o fundo da página é escuro, então **prefira uma foto com fundo
escuro** ou escurecido: parede em sombra, ambiente noturno, luz lateral.
Foto com fundo branco estourado vai brigar com o resto da página.

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
landing-v2/assets/img/
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
