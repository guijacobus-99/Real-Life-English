/* ==========================================================================
   Real-Life English — Volume 1 · VERSÃO 2 "Vitrine"
   Scripts da landing page
   ========================================================================== */
(function () {
  'use strict';

  /* ========================================================================
     ⚙️  CONFIGURAÇÃO — edite só esta parte
     ======================================================================== */
  var CONFIG = {
    // Link de checkout (Hotmart / Kiwify). Enquanto estiver vazio,
    // os botões de compra levam pra seção de preço.
    checkoutUrl: '',

    // Bloco de bônus do topo: quantas vagas de conversa de 15 min existem
    // e quantas ainda restam. Mantenha fiel à realidade — escassez inventada
    // é infração ao CDC e o público sente. Pra esconder o bloco inteiro,
    // apague a <div class="bonus"> do index.html.
    spotsTotal: 50,
    spotsLeft: 50
  };

  /* ========================================================================
     1. Dicionário da demonstração (toque-pra-traduzir)
        Formato:  'palavra': ['tradução', 'classe']
     ======================================================================== */
  var DICT = {
    // história 01 — no aeroporto
    'the':            ['o / a / os / as', 'artigo'],
    'line':           ['fila', 'substantivo'],
    'at':             ['em, no, na', 'preposição'],
    'boarding gate':  ['portão de embarque', 'expressão'],
    'is':             ['é, está', 'verbo to be'],
    'long':           ['longa, comprida', 'adjetivo'],
    'i':              ['eu', 'pronome'],
    'check':          ['conferir, checar', 'verbo'],
    'my':             ['meu, minha', 'possessivo'],
    'boarding pass':  ['cartão de embarque', 'expressão'],
    'again':          ['de novo, outra vez', 'advérbio'],
    'seat':           ['assento, lugar', 'substantivo'],
    '14a':            ['fileira 14, lugar A', 'assento'],
    'window':         ['janela', 'substantivo'],
    'a':              ['um, uma', 'artigo'],
    'woman':          ['mulher', 'substantivo'],
    'behind':         ['atrás de', 'preposição'],
    'me':             ['mim, me', 'pronome'],
    'asks':           ['pergunta', 'verbo'],
    'this':           ['este, isto', 'pronome'],
    'flight':         ['voo', 'substantivo'],
    'to':             ['para, até', 'preposição'],
    'lisbon':         ['Lisboa', 'nome próprio'],
    'smile':          ['sorrio, sorrir', 'verbo'],
    'and':            ['e', 'conjunção'],
    'say':            ['digo, dizer', 'verbo'],
    'yes':            ['sim', 'advérbio'],
    'it':             ['ele, ela, isso (coisa)', 'pronome'],
    'heart':          ['coração', 'substantivo'],
    'beats':          ['bate', 'verbo'],
    'fast':           ['rápido, depressa', 'advérbio'],
    'first':          ['primeiro, primeira', 'adjetivo'],
    'trip':           ['viagem', 'substantivo'],
    'alone':          ['sozinho, sozinha', 'adjetivo'],

    // história 03 — no café
    'what':           ['o que, qual', 'pronome'],
    'can':            ['posso, consigo', 'verbo modal'],
    'get':            ['trazer, pegar', 'verbo'],
    'you':            ['você', 'pronome'],
    'barista':        ['barista — quem faz o café', 'substantivo'],
    'large':          ['grande', 'adjetivo'],
    'coffee':         ['café', 'substantivo'],
    'please':         ['por favor', 'expressão'],
    'to go':          ['para viagem, para levar', 'expressão'],
    'she':            ['ela', 'pronome'],
    'writes':         ['escreve', 'verbo'],
    'name':           ['nome', 'substantivo'],
    'on':             ['em, sobre', 'preposição'],
    'cup':            ['copo, xícara', 'substantivo'],
    'spells':         ['soletra, escreve as letras', 'verbo'],
    'wrong':          ['errado', 'adjetivo'],
    "don't":          ['não (forma negativa)', 'negação'],
    'mind':           ['me importo, ligar para', 'verbo'],
    'thank you':      ['obrigado, obrigada', 'expressão'],
    'take':           ['pego, levar', 'verbo'],
    'outside':        ['para fora, lá fora', 'advérbio']
  };

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  function normalize(str) {
    return str.toLowerCase().replace(/[‘’]/g, "'").trim();
  }

  /* ========================================================================
     2. Toque-pra-traduzir
     ======================================================================== */
  function makeWord(text) {
    var entry = DICT[normalize(text)];
    if (!entry) { return null; }
    var span = document.createElement('span');
    span.className = 'w';
    span.textContent = text;
    span.setAttribute('data-pt', entry[0]);
    span.setAttribute('data-tag', entry[1]);
    span.setAttribute('role', 'button');
    span.setAttribute('tabindex', '0');
    span.setAttribute('aria-label', text + ': ' + entry[0]);
    return span;
  }

  function glossify(paragraph) {
    var nodes = Array.prototype.slice.call(paragraph.childNodes);

    nodes.forEach(function (node) {
      // frases já marcadas no HTML com <span data-ph>
      if (node.nodeType === 1 && node.hasAttribute('data-ph')) {
        var phrase = makeWord(node.textContent);
        if (phrase) { paragraph.replaceChild(phrase, node); }
        return;
      }
      if (node.nodeType !== 3) { return; }

      var parts = node.textContent.split(/([A-Za-z0-9’']+)/);
      if (parts.length < 2) { return; }

      var frag = document.createDocumentFragment();
      parts.forEach(function (part) {
        if (!part) { return; }
        var word = makeWord(part);
        frag.appendChild(word || document.createTextNode(part));
      });
      paragraph.replaceChild(frag, node);
    });
  }

  function setupStoryPanel(panel) {
    $$('[data-glossable]', panel).forEach(glossify);

    var chip = document.createElement('div');
    chip.className = 'gloss';
    chip.setAttribute('role', 'status');
    panel.appendChild(chip);

    var counter = $('[data-counter]', panel);
    var known = Object.create(null);
    var active = null;

    function updateCounter() {
      if (!counter) { return; }
      var n = Object.keys(known).length;
      counter.innerHTML = n === 0
        ? 'Nenhuma palavra traduzida ainda'
        : '<b>' + n + '</b> ' + (n === 1 ? 'palavra traduzida' : 'palavras traduzidas');
    }

    function hide() {
      chip.classList.remove('is-on');
      if (active) { active.classList.remove('is-active'); active = null; }
    }

    function show(word) {
      if (active === word) { hide(); return; }
      if (active) { active.classList.remove('is-active'); }

      active = word;
      word.classList.add('is-active', 'is-known');

      chip.innerHTML = '';
      var tag = document.createElement('small');
      tag.textContent = word.getAttribute('data-tag');
      chip.appendChild(tag);
      chip.appendChild(document.createTextNode(word.getAttribute('data-pt')));

      // posiciona o chip acima da palavra, sem escapar do cartão
      chip.classList.add('is-on');
      chip.style.left = '0px';
      chip.style.top = '0px';

      var pRect = panel.getBoundingClientRect();
      var wRect = word.getBoundingClientRect();
      var cRect = chip.getBoundingClientRect();
      var pad = 12;

      var wordCenter = wRect.left - pRect.left + wRect.width / 2;
      var left = wordCenter - cRect.width / 2;
      left = Math.max(pad, Math.min(left, pRect.width - cRect.width - pad));

      chip.style.left = left + 'px';
      chip.style.top = (wRect.top - pRect.top - cRect.height - 9) + 'px';
      chip.style.setProperty('--arrow', (wordCenter - left) + 'px');

      var key = normalize(word.textContent);
      if (!known[key]) {
        known[key] = true;
        updateCounter();
      }
    }

    panel.addEventListener('click', function (ev) {
      var word = ev.target.closest ? ev.target.closest('.w') : null;
      if (word && panel.contains(word)) { show(word); } else { hide(); }
    });

    panel.addEventListener('keydown', function (ev) {
      if (ev.key !== 'Enter' && ev.key !== ' ') { return; }
      var word = ev.target.closest ? ev.target.closest('.w') : null;
      if (!word) { return; }
      ev.preventDefault();
      show(word);
    });

    document.addEventListener('click', function (ev) {
      if (!panel.contains(ev.target)) { hide(); }
    });
    window.addEventListener('resize', hide);
    panel._hideGloss = hide;
  }

  $$('.story__panel').forEach(setupStoryPanel);

  /* ========================================================================
     3. Abas das histórias
     ======================================================================== */
  var tabs = $$('.story__tab');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (other) {
        var panel = document.getElementById(other.getAttribute('aria-controls'));
        var on = other === tab;
        other.setAttribute('aria-selected', on ? 'true' : 'false');
        if (panel) {
          panel.hidden = !on;
          if (!on && panel._hideGloss) { panel._hideGloss(); }
        }
      });
    });
  });

  /* ========================================================================
     4. Slots de imagem — o placeholder some quando a arte existe
     ======================================================================== */
  $$('.slot > img').forEach(function (img) {
    function fill() { img.parentNode.classList.add('is-filled'); }
    if (img.complete && img.naturalWidth > 0) { fill(); }
    img.addEventListener('load', function () { if (img.naturalWidth > 0) { fill(); } });
  });

  /* ========================================================================
     5. Checkout, preço e ano
     ======================================================================== */
  if (CONFIG.checkoutUrl) {
    $$('[data-cta]').forEach(function (link) {
      if (link.getAttribute('href') === '#') {
        link.setAttribute('href', CONFIG.checkoutUrl);
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener');
      }
    });
  } else {
    // sem checkout configurado: os botões levam pra seção de preço
    $$('[data-cta]').forEach(function (link) {
      if (link.getAttribute('href') === '#') { link.setAttribute('href', '#oferta'); }
    });
  }

  var priceEl = $('[data-price]');
  var priceMirror = $('[data-price-mirror]');
  if (priceEl && priceMirror) {
    priceMirror.textContent = priceEl.textContent.replace(/\s+/g, ' ').trim();
  }

  var yearEl = $('[data-year]');
  if (yearEl) { yearEl.textContent = new Date().getFullYear(); }

  // bloco de vagas do bônus
  var spotsLeftEl = $('[data-spots-left]');
  var spotsTotalEl = $('[data-spots-total]');
  var spotsBar = $('[data-spots-bar]');
  if (spotsLeftEl && spotsTotalEl && spotsBar) {
    var total = Math.max(1, CONFIG.spotsTotal);
    var left = Math.max(0, Math.min(CONFIG.spotsLeft, total));
    spotsLeftEl.textContent = left;
    spotsTotalEl.textContent = total;
    spotsBar.style.width = (left / total * 100) + '%';
  }

  /* ========================================================================
     6. Copiar o prompt do tutor
     ======================================================================== */
  var copyBtn = $('[data-copy-prompt]');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      var body = $('.prompt-card__body');
      if (!body) { return; }
      var text = body.innerText.replace('[cole sua resposta aqui]', '[cole sua resposta aqui]');
      var done = function () {
        var original = copyBtn.textContent;
        copyBtn.textContent = 'Copiado!';
        setTimeout(function () { copyBtn.textContent = original; }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, done);
      } else {
        var ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); } catch (e) {}
        document.body.removeChild(ta);
        done();
      }
    });
  }

  /* ========================================================================
     7. Barra de navegação e barra fixa de compra
     ======================================================================== */
  var nav = $('#nav');
  var sticky = $('#stickyBuy');
  var hero = $('#inicio');
  var offer = $('#oferta');

  function onScroll() {
    var y = window.pageYOffset;
    if (nav) { nav.classList.toggle('is-stuck', y > 8); }

    if (sticky && hero && offer) {
      var pastHero = y > hero.offsetHeight * 0.8;
      var offerRect = offer.getBoundingClientRect();
      var offerVisible = offerRect.top < window.innerHeight && offerRect.bottom > 0;
      sticky.classList.toggle('is-on', pastHero && !offerVisible);
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
