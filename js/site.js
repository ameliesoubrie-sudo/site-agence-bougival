(function () {
  // Menu mobile
  var b = document.querySelector('.burger'), n = document.getElementById('nav');
  if (b && n) b.addEventListener('click', function () {
    var o = n.classList.toggle('open');
    b.setAttribute('aria-expanded', o ? 'true' : 'false');
  });

  // Agence ouverte ou fermee (heure de Paris)
  var el = document.getElementById('open-status');
  if (el) {
    try {
      var p = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var m = {}; p.forEach(function (x) { m[x.type] = x.value; });
      var t = parseInt(m.hour, 10) * 60 + parseInt(m.minute, 10);
      var we = /sam|dim/i.test(m.weekday);
      var open = !we && ((t >= 540 && t < 750) || (t >= 840 && t < 1110));
      el.innerHTML = '<span class="dot' + (open ? ' open' : '') + '"></span>' + (open ? 'Agence ouverte en ce moment' : 'Agence fermée, laissez-nous un message');
    } catch (e) {}
  }
})();
