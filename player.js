const games = {'raindrops':'Raindrops','ricochet':'Ricochet: Neon Drive','bunny-runner':'Bunny Runner'};
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
 document.getElementById('title').textContent = 'Game not found — choose a game from All games.';
}
