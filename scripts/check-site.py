"""Check generated navigation, locale parity, fragments and local assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,parse_qs
ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__();self.refs=[];self.ids=set();self.lang=None;self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='html':self.lang=a.get('lang')
  for key in ('src','href'):
   if key in a:self.refs.append(a[key])
pages={p:Page(p) for p in [*ROOT.glob('*.html'),*(ROOT/'ru').glob('*.html')]}
errors=[]; count=0
for path,page in pages.items():
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(path.parent/unquote(u.path)).resolve() if u.path else path
  if target.is_dir():target=target/'index.html'
  count+=1
  if not target.exists():errors.append(f'{path.name}: missing {ref}')
  elif u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{path.name}: missing fragment {ref}')
  if target.name=='play.html':
   slug=parse_qs(u.query).get('game',[''])[0]
   if slug and not (ROOT/'games'/slug/'index.html').exists():errors.append(f'unknown game: {slug}')
for path in (ROOT/'ru').glob('*.html'):
 if not (ROOT/path.name).exists():errors.append(f'Locale counterpart missing: {path.name}')
 if pages[path].lang!='ru':errors.append(f'Wrong locale: {path.name}')
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; {count} local references; locale parity, fragments and game targets.')
# The replacement must remain consistent across both public home pages.
for path in (ROOT/'index.html', ROOT/'ru/index.html'):
 markup=path.read_text()
 assert 'raindrops' not in markup.lower(), f'Old portfolio entry: {path}'
 assert 'bunny-survival.html' in markup, f'Missing Bunny Survival: {path}'
demo=ROOT/'games/bunny-survival/index.html'
assert demo.exists(), 'Bunny Survival build missing'
assert 'https://sdk.crazygames.com/' not in demo.read_text(), 'Standalone demo loads portal SDK'
print('PASS: Bunny Survival replacement and standalone entrypoint')
