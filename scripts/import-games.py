"""Rebuild sibling projects in temporary copies; publish compiled assets only."""
import pathlib, tempfile, shutil, subprocess, re, json
root=pathlib.Path(__file__).resolve().parents[1]
projects={'raindrops':'ya_games_raindrops','ricochet':'game_rickochet','bunny-runner':'bunny_runner'}
for slug, source in projects.items():
 src=root.parent/source
 with tempfile.TemporaryDirectory(prefix='serendipity-') as tmp:
  work=pathlib.Path(tmp)/source
  shutil.copytree(src,work,ignore=shutil.ignore_patterns('.git','node_modules','dist','release','store','gametest-out','test-results','playwright-report','references','*.zip','.env*'))
  (work/'node_modules').symlink_to(src/'node_modules',target_is_directory=True)
  def edit(name,old,new):
   p=work/name;s=p.read_text();assert old in s,(name,old);p.write_text(s.replace(old,new))
  if slug=='raindrops':
   edit('src/main.ts','const isLocalHost = LOCAL_HOSTS.has(globalThis.location.hostname);','const isLocalHost = true; // Standalone portfolio demo')
   edit('src/main.ts','createMockAdapter({ setMuted,','createMockAdapter({ navigatorLanguage: "en", setMuted,')
  elif slug=='ricochet':
   edit('src/game/sdk/platform.ts',"location.hostname === 'localhost'","true || location.hostname === 'localhost'")
   edit('src/game/sdk/platform.ts',"(typeof navigator !== 'undefined' ? navigator.language : 'ru').slice(0, 2)","'en'")
  else:
   edit('src/YandexSDK.js',"if (!ysdk) return 'ru';","if (!ysdk) return 'en';")
   p=work/'index.html';s=p.read_text();s=re.sub(r'<script>.*?</script>\s*<script async src="/sdk.js".*?</script>','<script>window.__yandexSdkInitPromise = Promise.resolve(null);</script>',s,flags=re.S);p.write_text(s)
  # Vite produces production assets; source projects remain untouched.
  subprocess.run([str(src/'node_modules/.bin/vite'),'build','--base','./'],cwd=work,check=True)
  target=root/'games'/slug
  if target.exists():shutil.rmtree(target)
  shutil.copytree(work/'dist',target)
  for p in target.rglob('*.map'):p.unlink()
  print('IMPORTED',slug,flush=True)
