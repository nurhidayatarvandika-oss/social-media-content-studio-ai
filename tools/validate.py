#!/usr/bin/env python3
"""Validasi struktur, rujukan, routing, jumlah, dan pengaturan keamanan repositori."""
import json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warns = [], []
def err(m): errors.append(m)

def frontmatter(p):
    t = p.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    if not m: err(f'{p.relative_to(ROOT)}: frontmatter hilang'); return {}, t
    fm = {}
    for ln in m.group(1).split('\n'):
        if ':' in ln:
            k, v = ln.split(':', 1); fm[k.strip()] = v.strip().strip('"')
    return fm, t[m.end():]

def parse_list(v): return [x.strip() for x in v.strip('[]').split(',') if x.strip()]

# --- agen ---
agent_files = sorted((ROOT/'agents').rglob('*.md'))
agents = {}
method_sections = {}
REQ = ['## Peran','## Keahlian inti','## Menerima dari','## Metode kerja','## Format output','## Pemeriksaan sebelum menyerahkan','## Serahkan ke','## Aturan studio']
for p in agent_files:
    fm, body = frontmatter(p)
    n = fm.get('name')
    if n != p.stem: err(f'{p.name}: name "{n}" != nama file')
    if len(fm.get('description','')) < 30: err(f'{p.name}: description terlalu pendek')
    if fm.get('group') != p.parent.name: err(f'{p.name}: group "{fm.get("group")}" != folder {p.parent.name}')
    for s in REQ:
        if s not in body: err(f'{p.name}: bagian "{s}" hilang')
    if "You are the studio's" in body: err(f'{p.name}: masih berisi boilerplate lama')
    m = re.search(r'## Metode kerja\n(.*?)\n## ', body, re.S)
    sig = m.group(1).strip() if m else ''
    if len(sig.split('\n')) < 3: err(f'{p.name}: metode kerja kurang dari 3 langkah')
    if sig in method_sections: err(f'{p.name}: metode kerja identik dengan {method_sections[sig]}')
    method_sections[sig] = p.name
    agents[n] = p

# --- skill ---
skills = {}
for p in sorted((ROOT/'skills').glob('*/SKILL.md')):
    fm, body = frontmatter(p)
    if fm.get('name') != p.parent.name: err(f'{p}: name != folder')
    for a in parse_list(fm.get('agents','[]')):
        if a not in agents: err(f'{p.parent.name}: agen "{a}" tidak ada')
    if len(body.split('\n')) < 20: err(f'{p.parent.name}: isi skill terlalu tipis')
    skills[p.parent.name] = p

# --- workflow ---
workflows = {}
for p in sorted((ROOT/'workflows').glob('*.md')):
    t = p.read_text(); workflows[p.stem] = t
    rows = [r for r in t.split('\n') if re.match(r'^\| \d+ \|', r)]
    if not rows: err(f'{p.name}: tabel langkah hilang')
    for r in rows:
        for a in [x.strip() for x in r.split('|')[2].split(',')]:
            if a != 'studio-director' and a not in agents: err(f'{p.name}: agen "{a}" tidak ada')
            if a == 'studio-director' and a not in agents: err('studio-director tidak ada')

# --- command ---
commands = {}
for p in sorted((ROOT/'commands').glob('*.md')):
    fm, body = frontmatter(p); commands[p.stem] = fm
    if fm.get('workflow') not in workflows: err(f'{p.name}: workflow "{fm.get("workflow")}" tidak ada')
    for s in parse_list(fm.get('skills','[]')):
        if s not in skills: err(f'{p.name}: skill "{s}" tidak ada')
    if '$ARGUMENTS' not in body: err(f'{p.name}: $ARGUMENTS hilang')
    if '## Gerbang' not in body: err(f'{p.name}: bagian Gerbang hilang')

# --- config / routing ---
try:
    import yaml
except ImportError:
    yaml = None; warns.append('PyYAML tidak terpasang: pemeriksaan YAML dilewati (pip install pyyaml)')
if yaml:
    studio = yaml.safe_load((ROOT/'config/studio.yaml').read_text())
    route = yaml.safe_load((ROOT/'config/agent-routing.yaml').read_text())
    guard = yaml.safe_load((ROOT/'config/platform-guardrails.yaml').read_text())
    wf = studio['workflow']
    if wf['auto_publish'] or wf['auto_spend'] or wf['auto_delete']: err('config: auto_* harus false')
    if not wf['require_approval']: err('config: require_approval harus true')
    if wf['approval_gates'] != ['topic','script','final-assets','publishing-action']: err('config: approval_gates berubah')
    if studio['brand']['name'] is not None: err('config: brand.name harus null (nama brand belum ditentukan)')
    if not guard['all_platforms']['require_human_approval_before_publish']: err('guardrails: persetujuan manusia dimatikan')
    routed = set()
    for k, v in route['routing'].items():
        for a in v:
            routed.add(a)
            if a not in agents: err(f'routing.{k}: agen "{a}" tidak ada')
    for k, v in route['pipelines'].items():
        if k not in workflows: err(f'pipelines: workflow "{k}" tidak ada')
        for a in v:
            if a not in agents: err(f'pipelines.{k}: agen "{a}" tidak ada')
    for k, v in route['commands'].items():
        if k not in commands: err(f'routing.commands: "{k}" tidak ada')
        elif commands[k]['workflow'] != v['workflow']: err(f'routing.commands.{k}: workflow tidak cocok dengan file command')
    for c in commands:
        if c not in route['commands']: err(f'command "{c}" belum ada di routing.commands')
    for a in agents:
        if a not in routed: err(f'agen "{a}" tidak ada di routing')

# --- jumlah ---
count = dict(agents=len(agents), skills=len(skills), commands=len(commands), workflows=len(workflows), templates=len(list((ROOT/'templates').iterdir())))
man = json.loads((ROOT/'MANIFEST.json').read_text())
for k in ('agents','skills','commands','workflows'):
    if man.get(k) != count[k]: err(f'MANIFEST {k}: {man.get(k)} != {count[k]}')
on_disk = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts)
if sorted(man['files']) != on_disk:
    diff = set(on_disk) ^ set(man['files']); err(f'MANIFEST files tidak cocok: {sorted(diff)[:6]}')
inv = (ROOT/'docs/INVENTORY.md').read_text()
for label, k in (('Agen spesialis','agents'),('Skill','skills'),('Command','commands'),('Workflow','workflows'),('Template','templates')):
    m = re.search(rf'{label}: (\d+)', inv)
    if not m or int(m.group(1)) != count[k]: err(f'INVENTORY {label} tidak cocok ({count[k]})')
readme = (ROOT/'README.md').read_text()
for pat, k in ((r'(\d+) specialist agents','agents'),(r'(\d+) reusable skills','skills'),(r'(\d+) operational slash-command','commands'),(r'(\d+) templates','templates')):
    m = re.search(pat, readme)
    if m and int(m.group(1)) != count[k]: err(f'README {k}: {m.group(1)} != {count[k]}')
cat = (ROOT/'docs/AGENT_CATALOG.md').read_text()
m = re.search(r'(\d+) agen spesialis', cat)
if not m or int(m.group(1)) != count['agents']: err('AGENT_CATALOG: jumlah salah')
for a in agents:
    if f'`{a}`' not in cat: err(f'AGENT_CATALOG: {a} belum terdaftar')

# --- rujukan path di semua md ---
pat = re.compile(r'`((?:agents|skills|commands|workflows|templates|config|docs|examples|tools)/[A-Za-z0-9_\-./*]+)`')
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts: continue
    for ref in pat.findall(p.read_text()):
        if '*' in ref or ref.endswith('/'): continue
        if not (ROOT/ref).exists(): err(f'{p.relative_to(ROOT)}: rujukan rusak `{ref}`')

print(f'Agen {count["agents"]}, skill {count["skills"]}, command {count["commands"]}, workflow {count["workflows"]}, template {count["templates"]}')
for w in warns: print('PERINGATAN:', w)
if errors:
    print(f'GAGAL: {len(errors)} masalah'); [print(' -', e) for e in errors]; sys.exit(1)
print('LULUS: semua pemeriksaan berhasil')
