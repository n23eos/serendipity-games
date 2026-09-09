const root = document.documentElement;
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
if (!reduce.matches && 'IntersectionObserver' in window) {
 root.classList.add('js-motion');
 const observer = new IntersectionObserver(entries => entries.forEach(entry => {
  if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
 }), {threshold: .08});
 document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}
const motion = document.querySelector('.motion');
motion?.addEventListener('click', () => {
 const paused = root.classList.toggle('motion-paused');
 motion.setAttribute('aria-pressed', String(paused));
 motion.textContent = paused ? '▷' : 'Ⅱ';
 motion.setAttribute('aria-label', document.documentElement.lang === 'ru' ? (paused ? 'Включить анимацию' : 'Приостановить анимацию') : (paused ? 'Resume animations' : 'Pause animations'));
});
