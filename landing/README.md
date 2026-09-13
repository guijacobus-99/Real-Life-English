# Real-Life English — Volume 1 · Landing page

Página de vendas do ebook, no registro "Vitrine": escuro, brilhante, pesado —
produto em exposição. HTML, CSS e JavaScript puros, sem build, sem npm. Você
abre o `index.html` no navegador e ela funciona.

```
landing/
├── index.html            ← a página
├── termos.html           ← modelo a preencher
├── privacidade.html      ← modelo a preencher
├── robots.txt            ← o que buscador e raspador podem fazer
├── _headers              ← cabeçalhos de segurança (Netlify/Cloudflare)
├── vercel.json           ← os mesmos, para a Vercel
├── assets/
│   ├── fonts/            ← fontes servidas daqui, não do Google
│   ├── css/fonts.css     ← as declarações delas
│   ├── css/styles.css    ← o visual
│   ├── css/motion.css    ← a camada de movimento
│   ├── css/opening.css   ← a sequência do livro no topo
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

Veja o `IMAGENS.md`. As duas essenciais (capa em 3D e livro aberto) já foram
geradas pelo Higgsfield e estão na sua galeria em higgsfield.ai — baixe de lá
e salve na pasta `assets/img/` com o nome exato. O arquivo traz também os
prompts que funcionaram e os limites da conta free.

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

---

## Ligar a página ao pagamento (Hotmart / Kiwify)

**A página não processa pagamento nenhum.** Ela é uma vitrine com um link. A
pessoa clica, vai para o checkout da plataforma, paga lá, e a plataforma
entrega o acesso e cuida de nota fiscal, antifraude, parcelamento e reembolso.

Isso significa que você **não precisa** de servidor, banco de dados, certificado
de pagamento nem integração de código. Precisa de **um link**, colado em um
lugar só.

### O fluxo, igual nas duas plataformas

1. Cadastra o produto e sobe o arquivo do ebook
2. Define o preço e publica
3. A plataforma gera um **link de checkout**
4. Você cola esse link no `assets/js/main.js`

### Onde colar

`assets/js/main.js`, primeiras linhas:

```js
var CONFIG = {
  checkoutUrl: 'https://pay.hotmart.com/SEU-CODIGO',   // ← aqui
```

Um lugar só. Não procure link em outro arquivo — não tem.

### Como os botões se comportam

A página tem seis botões de compra, e eles **não fazem a mesma coisa**:

| Botão | Para onde vai |
|---|---|
| Menu do topo | rola até a seção de preço |
| Abertura ("Quero o Volume 1") | rola até a seção de preço |
| Dentro do livro aberto | rola até a seção de preço |
| Fechamento da página | rola até a seção de preço |
| **Cartão da oferta** | **checkout**, em aba nova |
| **Barra fixa do celular** | **checkout**, em aba nova |

É de propósito: quem clica lá em cima ainda não leu o que está incluído nem a
garantia. Mandar essa pessoa direto para o checkout derruba a conversão. Os
quatro primeiros levam ela até a oferta; só ali ela sai da página.

Se você quiser que **todos** vão direto ao checkout, troque o `href="#oferta"`
por `href="#"` nos botões correspondentes do `index.html` — o script converte
todo `href="#"` em link de checkout.

### Hotmart

1. Crie o produto em **Produtos → Cadastrar produto**, tipo **ebook / arquivo
   digital**
2. Suba o PDF (ou use o Hotmart Club se quiser área de membros)
3. Defina o preço e envie para análise — **a Hotmart revisa antes de liberar**,
   e isso leva algumas horas ou alguns dias
4. Depois de aprovado, o link de checkout aparece na área de **Checkout /
   Links** do produto, no formato `pay.hotmart.com/XXXXXXXX`
5. Cole no `checkoutUrl`

Se você criar mais de uma oferta (preço promocional, preço cheio), cada uma tem
seu próprio código, e o link muda com o parâmetro de oferta. Use o link da
oferta que a página anuncia — senão o preço do checkout não bate com o preço
escrito na página, e isso derruba a venda na hora.

### Kiwify

1. Crie o produto em **Produtos → Novo produto**, tipo **digital**
2. Suba o arquivo e defina o preço
3. O link de checkout sai no formato `pay.kiwify.com.br/XXXXXXXX`
4. Cole no `checkoutUrl`

A aprovação costuma ser mais rápida que a da Hotmart.

### Use uma, não as duas

Dá para cadastrar o produto nas duas, mas a página só aponta para um link. Ter
as duas ao mesmo tempo divide seu histórico de vendas, duplica o trabalho de
suporte e não traz vantagem nenhuma no começo.

Critério prático para escolher:

- **Hotmart** se você quer **afiliados**. Ela tem marketplace, onde afiliado
  encontra seu produto sozinho e vende por comissão. É a maior vantagem dela, e
  a Kiwify não tem equivalente com o mesmo alcance.
- **Kiwify** se você quer **subir rápido e sozinho**. Interface mais simples,
  aprovação mais rápida, menos burocracia.

Confira as taxas atuais na própria plataforma antes de decidir — elas mudam, e
a diferença muda conforme o preço do produto.

### Saber de onde veio cada venda

Se você anunciar ou postar em vários lugares, vai querer saber o que gerou
venda. As duas plataformas leem parâmetros na URL do checkout:

```js
// Hotmart usa 'src' para marcar a origem
checkoutUrl: 'https://pay.hotmart.com/SEU-CODIGO?src=landing'

// Kiwify lê os UTMs de sempre
checkoutUrl: 'https://pay.kiwify.com.br/SEU-CODIGO?utm_source=landing'
```

Com isso, uma venda que veio desta página aparece marcada no relatório, separada
das que vieram do Instagram ou do WhatsApp. Vale conferir na documentação da
plataforma como o parâmetro aparece no relatório — os nomes mudam de tempos em
tempos.

### Depois da compra

As duas deixam você escolher para onde a pessoa vai depois de pagar. Aponte para
uma página de obrigado sua — pode ser um `obrigado.html` nesta mesma pasta, no
mesmo visual. Serve para duas coisas: confirmar que deu certo (reduz o e-mail de
"comprei e não recebi") e marcar a conversão, se você estiver anunciando.

### Antes de considerar pronto

- [ ] Comprar o próprio produto, de verdade, com cartão real
- [ ] Conferir se o e-mail com o acesso chegou, e em quanto tempo
- [ ] Conferir se o preço no checkout é **exatamente** o que está na página
- [ ] Testar o botão no celular, não só no computador
- [ ] Pedir o reembolso dessa compra teste, para ver o fluxo que seu aluno veria

---

---

## Segurança

Esta página foi revisada com ela em mente: dinheiro passa perto, e o comprador
precisa confiar no que vê. O resumo é que **a superfície de ataque aqui é
minúscula**, e por um motivo estrutural.

### Por que o risco é baixo por natureza

Os vazamentos que se ouve falar acontecem onde há **dado guardado** e **código
rodando no servidor**. Esta página não tem nem um nem outro:

| | |
|---|---|
| Servidor com código | não existe — são arquivos estáticos |
| Banco de dados | não existe |
| Formulário, login, senha | não existe |
| Cookie, localStorage, rastreador | não usa |
| Dado de cartão | **nunca toca nesta página** — quem processa é a Hotmart/Kiwify |

Não há como "roubar o banco de dados" de uma página que não tem banco. Não há
sessão para sequestrar, porque não há login. Os dados do comprador — nome,
CPF, cartão — são digitados no checkout da plataforma, num domínio que não é o
seu, sob a responsabilidade e a certificação deles.

### O que foi feito

**Nada carrega de fora.** A página não faz uma única requisição a outro
domínio. As fontes, que antes vinham do Google, agora são servidas daqui
(`assets/fonts/`). Isso fecha uma porta real: quando o navegador busca fonte no
Google, ele entrega a um terceiro o IP e o navegador de quem está lendo — dado
pessoal, coletado sem consentimento e sem constar na sua política de
privacidade. Sob a LGPD isso é um problema evitável, e evitamos.

**Política de segurança de conteúdo (CSP).** O navegador recebe uma regra
explícita: só execute script, só carregue estilo, fonte e imagem que venham
deste domínio. Se alguém conseguisse injetar um `<script>` de fora, o navegador
recusaria. Para a regra ser estrita de verdade, **todo estilo inline foi
removido** do HTML — sem isso, seria preciso permitir `unsafe-inline`, que é
justamente a folga que um ataque de injeção usa.

**Cabeçalhos de proteção**, em `_headers` (Netlify, Cloudflare Pages) e
`vercel.json` (Vercel):

- `X-Frame-Options: DENY` e `frame-ancestors 'none'` — impedem que golpista
  embuta sua página num iframe e sobreponha um botão falso por cima
  (*clickjacking*). Para uma página que leva ao pagamento, isso importa.
- `X-Content-Type-Options: nosniff` — o navegador não "adivinha" o tipo de um
  arquivo, o que impede que uma imagem seja tratada como script.
- `Referrer-Policy` — sites de destino não recebem o caminho completo de onde
  a pessoa veio.
- `Strict-Transport-Security` — depois da primeira visita, o navegador se
  recusa a abrir seu site sem HTTPS.

**JavaScript auditado.** Os dois pontos que montam HTML por string foram
conferidos: um insere um número inteiro (a contagem de palavras), o outro
limpa um elemento. Todo texto que vem da página é inserido com `textContent`,
que não interpreta marcação. **A página não lê nada da URL, de cookie ou de
storage** — não existe entrada por onde injetar.

### O que não dá para impedir, e por que tudo bem

**Copiar o visual da página.** Não existe forma de impedir, em site nenhum:
HTML, CSS e JavaScript são entregues ao navegador de quem visita, senão a
página não aparece. Bloquear botão direito ou F12 não protege nada e só irrita
quem é honesto.

Mas repare no que um clone *não* consegue fazer:

- **Não desvia sua venda.** O link de checkout aponta para o *seu* produto. Se
  o golpista copiar a página inteira e não trocar o link, ele vende para você.
- **Não rouba dado seu.** Não há dado nesta página além do que já é público.

O risco real de um clone é outro: alguém copia sua página, **troca o link de
checkout** e aplica golpe nos *seus* compradores, sujando seu nome. Contra isso
não existe defesa técnica no código — a defesa é ter **domínio próprio
reconhecível**, dizer nas suas redes qual é o endereço oficial, e acionar
remoção por direito autoral se aparecer um clone. Domínio próprio é, aqui, uma
medida de segurança, não só de estética.

### O que muda se você adicionar coisas depois

- **Pixel do Facebook, Google Analytics ou qualquer rastreador**: vai quebrar
  na CSP, de propósito. Para liberar, acrescente o domínio dele em `script-src`
  e `connect-src` nos dois arquivos de cabeçalho e no `<meta>` do HTML. E aí
  passa a valer o outro lado: rastreador coleta dado pessoal, e isso precisa
  estar na sua política de privacidade e, dependendo do que você usar, num
  aviso de cookies.
- **Formulário de e-mail**: hoje `form-action` está em `'none'`. Se colocar
  captura de lead, libere o destino.
- **Vídeo do YouTube ou Vimeo**: precisa liberar `frame-src`.

Em todos os casos, o princípio é o mesmo: libere **o domínio específico**, não
`*`.

### Robôs e tráfego de anúncio

Quem vai anunciar naturalmente se pergunta se não deveria colocar um
reCAPTCHA. A resposta aqui é **não**, e vale entender o porquê antes de
decidir o contrário.

#### Por que reCAPTCHA não funciona nesta página

O reCAPTCHA v3 — o invisível, que dá uma nota de 0 a 1 para o visitante —
trabalha em cinco passos:

1. O script do Google observa o comportamento na página
2. Gera um token
3. A página manda esse token **para o seu servidor**
4. **Seu servidor** pergunta ao Google, com sua chave secreta, quanto vale o token
5. **Seu servidor** decide: passa ou bloqueia

**Os passos 3, 4 e 5 precisam de um servidor seu, e esta página não tem** —
são arquivos estáticos num CDN. Sem eles, a nota é calculada e jogada fora.
Um robô simplesmente não executa o script, e nada acontece: não há nada para
bloquear, porque não há nada acontecendo depois.

Verificação feita só no navegador nunca protege. O navegador é do visitante;
quem quer burlar, burla.

#### E o que ele custaria

Não é neutro instalar mesmo assim:

- **Devolve o Google ao seu site.** Acabamos de tirar as fontes do Google
  justamente para não entregar o IP de cada leitor a um terceiro. O
  reCAPTCHA faz isso e mais: ele existe para perfilar comportamento, e roda
  em **todas** as páginas, não só onde há formulário. Isso reabre a questão
  de LGPD que fechamos.
- **Quebra a CSP** que fechamos, e obriga a afrouxá-la.
- **Pesa** — é um dos scripts mais gordos que se instala numa página.
- **Derruba conversão.** Em página de vendas, todo atrito custa venda.

Ou seja: pagaria o preço todo e não compraria proteção nenhuma.

#### O que esta página oferece de superfície

Vale ver o tamanho real do problema:

| | |
|---|---|
| Formulário | nenhum |
| Campo de digitação | nenhum |
| Envio de dados | nenhum |
| Login ou sessão | nenhum |
| Endpoint próprio | nenhum |

Um robô que visite esta página consegue **baixar 500 KB de arquivo estático**.
Só isso. Não há o que floodar, porque não há nada que receba dados.

#### O que de fato resolve o que você teme

**1. Ponha o site atrás da Cloudflare — é lá que robô se barra.**

Hospedando no **Cloudflare Pages** (grátis) ou apontando seu domínio para a
Cloudflare, você liga no painel:

- **Bot Fight Mode** — barra robô conhecido na borda, antes de chegar na página
- **Proteção contra DDoS** — automática, sem configurar
- **Rate limiting** — corta excesso de requisição do mesmo endereço

Isso é a "verificação de humano" que você quer, só que no lugar certo: **antes**
da página, não dentro dela. E não atrapalha quem é gente.

> **Se o seu medo é flood, esta é a razão decisiva para escolher Cloudflare
> Pages:** o plano grátis tem **banda ilimitada**. Na Netlify e na Vercel o
> plano grátis tem teto de tráfego, então um flood grande pode te gerar conta
> ou tirar o site do ar. Na Cloudflare, não vira despesa.

**2. Clique inválido é problema do anunciante, e eles já cuidam.**

Google Ads e Meta Ads detectam tráfego inválido e **estornam** o que foi
cobrado indevidamente. Acompanhe a coluna de cliques inválidos no relatório.
Se aparecer padrão estranho que eles não pegaram, dá para abrir contestação —
e isso se resolve na plataforma de anúncio, não no HTML.

**3. Fraude de cartão não é sua.**

Teste de cartão roubado acontece no checkout, que é da Hotmart/Kiwify, com o
antifraude deles. Nada disso passa por aqui.

**4. Quando tiver analytics, filtre robô.**

Ative a exclusão de robôs conhecidos na ferramenta. Isso não é segurança — é
não deixar seu relatório mentir sobre a conversão.

#### O dia em que o CAPTCHA vai fazer sentido

Quando você adicionar **formulário** — captura de e-mail, lista de espera,
contato. Aí existe algo que recebe dados, e aí sim precisa de proteção.

Quando esse dia chegar, o caminho é **Cloudflare Turnstile**, não reCAPTCHA:
faz a mesma coisa (invisível, com pontuação), é grátis, e **não entrega seus
visitantes ao Google** — mantém a conformidade que a página tem hoje. E o
servidor que falta para validar o token você ganha junto: **Pages Functions**,
incluso no plano grátis da Cloudflare.

Me chame quando chegar lá que eu monto — formulário, Turnstile e a validação
no servidor, de uma vez.

#### robots.txt

Existe no projeto, e faz o que dá para fazer: pede aos buscadores que indexem
(você quer aparecer no Google) e pede aos raspadores de treino de IA que não
copiem. **É um pedido, não uma trava** — robô sério respeita, robô ruim nem
lê o arquivo. Está lá por higiene e por causa do SEO, não como defesa.

---

### Antes de publicar

- [ ] HTTPS ativo — Netlify, Vercel e Cloudflare Pages fazem sozinhos
- [ ] Conferir os cabeçalhos depois no ar em
      [securityheaders.com](https://securityheaders.com)
- [ ] Confirmar que o link do botão abre o checkout do **seu** produto
- [ ] Se adicionar rastreador, atualizar `privacidade.html` antes
- [ ] Trocar o domínio no `robots.txt`
- [ ] Se for anunciar, ligar o Bot Fight Mode na Cloudflare

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
| 1 | **Abertura** | Logotipo, 3 checks, botão e bônus — e o livro, que gira, abre e vira a página que você lê |
| 2 | Problema | "Você sabe as regras, mas trava" |
| 3 | **Mais sobre o Volume 1** | Foto do livro aberto com o argumento à esquerda e o sumário dourado à direita |
| 4 | **Experimente** | Demonstração ao vivo do toque-pra-traduzir |
| 5 | Pra quem é | Os 3 perfis com ilustração, dados e objetivo |
| 6 | O que vem dentro | 7 peças em grade |
| 7 | Tutor de IA | Prompt real com botão de copiar |
| 8 | Depoimentos | (reservado) |
| 9 | Autor | Sua história |
| 10 | Oferta | Preço, o que inclui, garantia |
| 11 | Dúvidas | 7 perguntas |
| 12 | Fechamento | Última chamada |

### Os dois momentos que carregam a página

**A abertura (seção 1).** Começa como um hero comum: logotipo à esquerda, o
livro fechado à direita, com dois cartões flutuando ao redor. Eles mostram a
mesma pergunta — *"What can I get you?"* — com duas respostas: a de antes
(você trava) e a de depois (você responde). É a promessa inteira sem precisar
ler nada.

Aí a pessoa começa a descer, e a seção não sai do lugar: o livro **dá uma
volta completa** sobre o próprio eixo, **a capa gira sobre a lombada e abre**,
o conjunto **caminha para a esquerda**, e a página direita — a que você
estaria lendo, se o livro estivesse nas suas mãos — recebe os números do
Volume 1 e o botão. A borda dessa página se dissolve no fundo, e por um
instante a página do livro e a página do site são a mesma coisa.

Subir o scroll desfaz tudo na ordem inversa. Isso não é um segundo efeito
programado: a animação está **presa à posição da barra de rolagem**, não
disparada por evento. Cada ponto do scroll corresponde a um quadro, então o
filme roda para trás sozinho — e para no meio se você parar no meio.

Duas coisas que vale saber:

- **O livro da sequência é montado em CSS, não é a fotografia.** Uma foto não
  tem verso nem miolo; não há como abri-la. A fotografia continua em uso como
  estado de repouso de quem não recebe a animação.
- **A sequência é coisa de tela larga** (a partir de 901 px) e de navegador
  com animação presa ao scroll. No celular, no Firefox e para quem pediu menos
  movimento, a seção vira um hero comum: fotografia do livro e, logo abaixo,
  um cartão com os mesmos quatro números. Nada se perde.

Para desligar só a sequência, apague a linha do `opening.css` no `<head>`.

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
