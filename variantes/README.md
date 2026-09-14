# Três variantes visuais — para escolher uma

Mesmo produto, mesma copy, mesma animação do livro. O que muda é a pele.
Abra as três, veja qual te agrada, e me diga: **eu promovo a escolhida a
`landing/` e completo o que faltar**. As outras duas somem.

| Pasta | Registro | Vem de |
|---|---|---|
| `claro/` | Fundo lilás-claro, acento roxo com botão lima. Trilho de ícones na lateral, cartões brancos, faixa escura de destaques. | referência Nexora |
| `brasa/` | Quase-preto quente, brasa laranja atrás do produto, composição centrada, planos lado a lado com o do meio aceso. | referência Velocity |
| `neon/` | Preto com verde-limão. A abertura acontece dentro de um bloco branco arredondado; títulos com marca-texto verde e fita rolante. | referência Creatix |

Para ver: abra `claro/index.html`, `brasa/index.html` ou `neon/index.html`.
Se quiser servir local (recomendado, por causa das fontes):

```bash
cd variantes && python3 -m http.server 8000
# http://localhost:8000/claro/
```

---

## Como estão montadas

```
variantes/
├── compartilhado/     ← o que é igual nas três
│   ├── fonts/         ← Geist e Geist Mono, servidas daqui
│   ├── img/           ← as imagens do produto
│   ├── css/fonts.css
│   ├── css/motion.css     ← a camada de movimento
│   ├── css/opening.css    ← a sequência do livro que gira e abre
│   └── js/                ← toque-pra-traduzir, abas, FAQ, checkout
├── claro/  ├── index.html  └── styles.css
├── brasa/  ├── index.html  └── styles.css
└── neon/   ├── index.html  └── styles.css
```

**Cada variante são só dois arquivos.** Todo o resto é compartilhado — inclusive
a animação do livro, que roda igual nas três.

Isso foi possível porque `motion.css` e `opening.css` são escritos em cima de
**tokens**, não de cores fixas. Cada `styles.css` define os seus valores e
faz o apelido para os nomes que os arquivos compartilhados esperam:

```css
--roxo: #6C5CE7;
--amber: var(--roxo);   /* o compartilhado pede "amber"; aqui ele é roxo */
```

As quatro cores do livro 3D também são tokens (`--capa-fundo`,
`--capa-verso`, `--lombada`, `--pagina-fundo`), e é por isso que o mesmo
livro funciona tanto num fundo preto quanto dentro do bloco branco da `neon`.

---

## O que mudou de conteúdo

Todas as três já trazem **os três volumes com preço em pacote**:

| | |
|---|---|
| Volume 1 | R$ 60 |
| Volumes 1 + 2 | R$ 90 |
| Volumes 1 + 2 + 3 | R$ 110 |

Isso resolve a matemática que travava o tráfego pago: com ticket médio perto
de R$ 90, um anúncio tem margem para se pagar — coisa que R$ 47 não permitia.

> ⚠️ **Os níveis dos Volumes 2 e 3 são suposição minha** (A2–B1 e B1–B2), assim
> como o número de 120 histórias na coleção. Me passe os dados reais e eu
> acerto nas três de uma vez.

---

## Quando você escolher

Diga qual e eu:

1. Promovo a pasta escolhida a `landing/`, com a estrutura definitiva
2. Trago o que hoje só existe na versão atual: seção do tutor de IA, autor
   completo, depoimentos, termos e privacidade
3. Levo junto a segurança que já está pronta: CSP, cabeçalhos, robots.txt,
   fontes próprias
4. Ligo os três botões de compra aos três links de checkout

O que **não** muda com a escolha: a copy, a animação do livro, o
toque-pra-traduzir e a estrutura de preço.
