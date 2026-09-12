/* ==========================================================================
   Real-Life English — Volume 1 · VERSÃO 2
   CAMADA DE MOVIMENTO — o que o CSS sozinho não faz
   --------------------------------------------------------------------------
   O grosso do movimento está no motion.css, em animações nativas presas ao
   scroll — elas rodam na GPU e não travam a rolagem. Este arquivo cuida de
   três coisas que precisam de JavaScript:

     1. O holofote que segue o cursor nos cards
     2. Os números da faixa que contam quando entram na tela
     3. A barra de progresso e o fio lateral em navegadores que ainda não
        têm animação presa ao scroll (hoje, o Firefox)

   Nada aqui esconde conteúdo. Se este arquivo não carregar, a página
   continua inteira e legível — só fica mais parada.
   ========================================================================== */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) { return; }

  var $$ = function (sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); };

  /* ========================================================================
     1. Holofote no cursor
     ------------------------------------------------------------------------
     Escreve a posição do cursor, relativa ao card, em duas custom properties.
     O gradiente que usa essas variáveis está no motion.css.
     ======================================================================== */
  var SPOT = '.tile, .profile, .faq__item';
  var spotPending = false;
  var spotEvent = null;

  function paintSpot() {
    spotPending = false;
    var ev = spotEvent;
    if (!ev) { return; }
    var card = ev.target.closest ? ev.target.closest(SPOT) : null;
    if (!card) { return; }
    var r = card.getBoundingClientRect();
    card.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
    card.style.setProperty('--my', (ev.clientY - r.top) + 'px');
  }

  document.addEventListener('pointermove', function (ev) {
    if (ev.pointerType === 'touch') { return; }
    spotEvent = ev;
    if (!spotPending) { spotPending = true; requestAnimationFrame(paintSpot); }
  }, { passive: true });

  /* ========================================================================
     2. Os números contam ao entrar na tela
     ------------------------------------------------------------------------
     O valor final já está escrito no HTML. Se nada disto rodar, ele aparece
     direto — a contagem é enfeite, não conteúdo.
     ======================================================================== */
  function countUp(el, target) {
    var start = null;
    var dur = 900;

    function frame(now) {
      if (start === null) { start = now; }
      var t = Math.min(1, (now - start) / dur);
      var eased = 1 - Math.pow(1 - t, 3);         // desacelera no fim
      el.textContent = Math.round(target * eased);
      if (t < 1) { requestAnimationFrame(frame); }
      else { el.textContent = target; }
    }
    requestAnimationFrame(frame);
  }

  if ('IntersectionObserver' in window) {
    var numbers = $$('.metric b').filter(function (el) {
      return /^\d+$/.test(el.textContent.trim());
    });

    if (numbers.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) { return; }
          io.unobserve(entry.target);
          countUp(entry.target, parseInt(entry.target.textContent.trim(), 10));
        });
      }, { threshold: 0.6 });

      numbers.forEach(function (el) { io.observe(el); });
    }
  }

  /* ========================================================================
     3. Progresso e fio lateral onde o CSS ainda não chega
     ------------------------------------------------------------------------
     Chrome, Edge e Safari novo prendem estas duas animações ao scroll pelo
     próprio CSS. No Firefox isso ainda não existe, então fazemos na mão.
     ======================================================================== */
  var hasScrollTimeline = window.CSS && CSS.supports && CSS.supports('animation-timeline', 'scroll()');
  if (hasScrollTimeline) { return; }

  var bar = document.querySelector('.scroll-progress');
  var seam = document.querySelector('.seam');
  if (!bar && !seam) { return; }

  var barFill = bar ? bar.firstElementChild : null;
  var seamFill = seam ? seam.firstElementChild : null;

  // o ::after do CSS não é alcançável pelo JS, então criamos um filho real
  if (bar && !barFill) {
    barFill = document.createElement('i');
    barFill.style.cssText = 'display:block;height:100%;transform-origin:0 50%;transform:scaleX(0);' +
      'background:linear-gradient(90deg,var(--amber-lo),var(--amber-hi));box-shadow:0 0 14px var(--amber-glow)';
    bar.appendChild(barFill);
    bar.classList.add('is-js');
  }
  if (seam && !seamFill) {
    seamFill = document.createElement('i');
    seamFill.style.cssText = 'display:block;height:100%;transform-origin:50% 0;transform:scaleY(0);' +
      'background:linear-gradient(180deg,transparent,rgba(224,165,63,.5) 12%,rgba(224,165,63,.22) 55%,transparent)';
    seam.appendChild(seamFill);
    seam.classList.add('is-js');
  }

  var ticking = false;
  function paintProgress() {
    ticking = false;
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    var p = max > 0 ? Math.min(1, Math.max(0, window.pageYOffset / max)) : 0;
    if (barFill) { barFill.style.transform = 'scaleX(' + p + ')'; }
    if (seamFill) { seamFill.style.transform = 'scaleY(' + p + ')'; }
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(paintProgress); }
  }, { passive: true });
  window.addEventListener('resize', paintProgress, { passive: true });
  paintProgress();
})();
