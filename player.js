const ru = new URLSearchParams(location.search).get('lang') === 'ru';
if (ru) { document.documentElement.lang='ru'; document.querySelector('.player-bar a').textContent='← Все игры'; document.querySelector('.player-bar a').href='./ru/#games'; document.querySelector('#fullscreen').textContent='⛶ На весь экран'; document.querySelector('.player-hint').textContent='Демо в разработке · Интерфейс игры может быть на английском.'; }
const games = {'raindrops':'Raindrops','ricochet':'Ricochet: Neon Drive','bunny-runner':'Bunny Runner','jelly-mix':'Jelly Mix'};
const slug = new URLSearchParams(location.search).get('game');
const frame = document.getElementById('game');
const button = document.getElementById('fullscreen');
if (Object.hasOwn(games, slug)) {
 document.title = `${games[slug]} — Serendipity Games`;
 document.getElementById('title').textContent = games[slug];
 frame.title = games[slug];
 frame.src = `games/${slug}/`;
 frame.addEventListener('load', () => frame.focus());
 button.addEventListener('click', async () => {
  try { if (frame.requestFullscreen) await frame.requestFullscreen(); else location.href = frame.src; }
  catch { location.href = frame.src; }
 });
} else {
 frame.remove(); button.remove();
 document.getElementById('title').textContent = ru ? 'Игра не найдена — вернитесь к списку игр.' : 'Game not found — choose a game from All games.';
}
