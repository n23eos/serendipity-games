"""Rebuild sibling projects in temporary copies; publish compiled assets only."""
import pathlib, tempfile, shutil, subprocess, re, json, sys
root=pathlib.Path(__file__).resolve().parents[1]
projects={'bunny-survival':'Crazy Games/Bunny Survival','ricochet':'game_rickochet','bunny-runner':'bunny_runner','jelly-mix':'jelly3_in_row'}
for slug, source in projects.items():
 if len(sys.argv)>1 and slug not in sys.argv[1:]: continue
 src=root.parent/source
 with tempfile.TemporaryDirectory(prefix='serendipity-') as tmp:
  work=pathlib.Path(tmp)/source
  shutil.copytree(src,work,ignore=shutil.ignore_patterns('.git','node_modules','dist','release','store','gametest-out','test-results','playwright-report','references','*.zip','.env*','Crazy Games','assets_archive','assets-src','bunny-backpack-assets','bunny-survive-yandex-draft-sprint16-mobile-ui','tmp'))
  (work/'node_modules').symlink_to(src/'node_modules',target_is_directory=True)
  def edit(name,old,new):
   p=work/name;s=p.read_text();assert old in s,(name,old);p.write_text(s.replace(old,new))
  if slug=='bunny-survival':
   edit('index.html','<script src="https://sdk.crazygames.com/crazygames-sdk-v3.js"></script>','')
   edit('src/main.js',"setLanguageFromSdk(sdk?.user?.systemInfo?.locale || 'en');","setLanguageFromSdk(langParam || 'en');")
   build_id=subprocess.check_output(['git','rev-parse','--short','HEAD'],cwd=src,text=True).strip()
   edit('vite.config.js',"JSON.stringify(buildStamp())",json.dumps(json.dumps('portfolio-'+build_id)))
  elif slug in ('ricochet', 'jelly-mix'):
   edit('src/game/sdk/platform.ts',"location.hostname === 'localhost'","true || location.hostname === 'localhost'")
   edit('src/game/sdk/platform.ts',"(typeof navigator !== 'undefined' ? navigator.language : 'ru').slice(0, 2)","'en'")
   if slug=='jelly-mix':
    edit('index.html','<script src="/sdk.js"></script>','')
    build_id=subprocess.check_output(['git','rev-parse','--short','HEAD'],cwd=src,text=True).strip()
    edit('vite.config.ts',"execFileSync('git', ['rev-parse', '--short', 'HEAD'], { encoding: 'utf8' }).trim()",json.dumps(build_id))
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
