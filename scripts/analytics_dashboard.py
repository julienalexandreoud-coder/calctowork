#!/usr/bin/env python3
"""
CalcToWork Analytics Dashboard Generator
Creates an interactive HTML dashboard from GSC data
"""

import csv
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
GSC_DATA = ROOT / "gsc_data"
PUBLIC = ROOT / "public"
DASHBOARD_FILE = PUBLIC / "analytics.html"

def load_csv(filename):
    filepath = GSC_DATA / filename
    if not filepath.exists():
        return []
    with open(filepath, encoding='utf-8') as f:
        return list(csv.DictReader(f))

queries = load_csv("Consultas.csv")
pages = load_csv("Páginas.csv")
countries = load_csv("Países.csv")

# Metrics
total_clicks = sum(int(r.get('Clics', 0) or 0) for r in queries)
total_impressions = sum(int(r.get('Impresiones', 0) or 0) for r in queries)
avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
avg_position = sum(float(r.get('Posición', 0) or 0) for r in queries) / len(queries) if queries else 0

# Zero-CTR queries (10+ impressions, 0 clicks)
zero_ctr = [r for r in queries if int(r.get('Clics', 0) or 0) == 0 and int(r.get('Impresiones', 0) or 0) >= 10]
zero_ctr.sort(key=lambda x: -int(x.get('Impresiones', 0) or 0))

# Page 2 opportunities (position 10-30)
page2 = [r for r in queries if 10 <= float(r.get('Posición', 0) or 0) < 30 and int(r.get('Impresiones', 0) or 0) >= 5]
page2.sort(key=lambda x: -int(x.get('Impresiones', 0) or 0))

# Top pages
top_pages = sorted(pages, key=lambda x: -int(x.get('Impresiones', 0) or 0))[:20]

# Zero-CTR pages (50+ impressions)
zero_ctr_pages = [p for p in pages if int(p.get('Clics', 0) or 0) == 0 and int(p.get('Impresiones', 0) or 0) >= 50]
zero_ctr_pages.sort(key=lambda x: -int(x.get('Impresiones', 0) or 0))

# Categories
def categorize(q):
    q = q.lower()
    if any(x in q for x in ['tile', 'baldosa', 'azulejo']): return 'Tiles'
    if any(x in q for x in ['cop', 'eer', 'hvac']): return 'HVAC'
    if any(x in q for x in ['bmr', 'metabolic', 'calorie']): return 'Health'
    if any(x in q for x in ['concrete', 'hormigon']): return 'Concrete'
    if any(x in q for x in ['pladur', 'drywall']): return 'Drywall'
    return 'Other'

cats = {}
for q in queries:
    c = categorize(q.get('Consultas principales', ''))
    if c not in cats: cats[c] = {'clicks': 0, 'imps': 0}
    cats[c]['clicks'] += int(q.get('Clics', 0) or 0)
    cats[c]['imps'] += int(q.get('Impresiones', 0) or 0)

# Generate HTML
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CalcToWork Analytics</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
:root{{--primary:#f97316;--success:#22c55e;--warning:#f59e0b;--danger:#ef4444;--bg:#f8fafc;--card:#fff;--text:#1e293b;--muted:#64748b;--border:#e2e8f0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;padding:2rem}}
.dashboard{{max-width:1400px;margin:0auto}}
.header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;padding-bottom:1rem;border-bottom:2px solid var(--border)}}
.header h1{{font-size:1.75rem;color:var(--primary)}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin-bottom:2rem}}
.kpi{{background:var(--card);border-radius:12px;padding:1.5rem;box-shadow:0 1px 3px rgba(0,0,0,0.1);border:1px solid var(--border)}}
.kpi h3{{font-size:0.75rem;text-transform:uppercase;color:var(--muted);margin-bottom:0.5rem}}
.kpi .value{{font-size:2rem;font-weight:700}}
.kpi .sub{{font-size:0.875rem;color:var(--muted);margin-top:0.5rem}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(450px,1fr));gap:1.5rem;margin-bottom:2rem}}
.card{{background:var(--card);border-radius:12px;padding:1.5rem;box-shadow:0 1px 3px rgba(0,0,0,0.1)}}
.card h2{{font-size:1.125rem;margin-bottom:1rem;padding-bottom:0.75rem;border-bottom:1px solid var(--border);color:var(--primary)}}
table{{width:100%;border-collapse collapse;font-size:0.875rem}}
th,td{{padding:0.75rem;text-align:left;border-bottom:1px solid var(--border)}}
th{{background:var(--bg);font-weight:600;color:var(--muted);font-size:0.75rem;text-transform:uppercase}}
tr:hover{{background:var(--bg)}}
.badge{{display:inline-block;padding:0.25rem 0.5rem;border-radius:9999px;font-size:0.75rem;font-weight:600}}
.badge-danger{{background:#fef2f2;color:var(--danger)}}
.badge-warning{{background:#fffbeb;color:var(--warning)}}
.badge-success{{background:#f0fdf4;color:var(--success)}}
.url{{max-width:280px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:0.75rem}}
.query{{max-width:320px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.action{{padding:0.75rem 0;border-bottom:1px solid var(--border)}}
.action:last-child{{border-bottom:none}}
.priority{{display:inline-block;width:2rem;height:2rem;border-radius:6px;text-align:center;line-height:2rem;font-weight:700;font-size:0.75rem;color:#fff}}
.priority.h{{background:var(--danger)}}
.priority.m{{background:var(--warning)}}
.priority.l{{background:var(--success)}}
.chart-wrap{{position:relative;height:250px}}
@media(max-width:768px){{.grid{{grid-template-columns:1fr}}body{{padding:1rem}}}}
</style>
</head>
<body>
<div class="dashboard">
<div class="header"><h1>📊 CalcToWork Analytics</h1><div>Updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</div></div>

<div class="kpi-grid">
<div class="kpi"><h3>Total Clicks</h3><div class="value">{total_clicks}</div><div class="sub">Sample period</div></div>
<div class="kpi"><h3>Impressions</h3><div class="value">{total_impressions:,}</div><div class="sub">All queries</div></div>
<div class="kpi"><h3>Avg CTR</h3><div class="value" style="color:{'var(--success)' if avg_ctr>=2 else 'var(--warning)' if avg_ctr>=1 else 'var(--danger)'}">{avg_ctr:.2f}%</div><div class="sub">Target: 2-5%</div></div>
<div class="kpi"><h3>Avg Position</h3><div class="value">{avg_position:.1f}</div><div class="sub">Lower=better</div></div>
<div class="kpi"><h3 style="color:var(--danger)">Zero-CTR</h3><div class="value">{len(zero_ctr)}</div><div class="sub">10+ imps, 0 clicks</div></div>
<div class="kpi"><h3 style="color:var(--warning)">Page 2</h3><div class="value">{len(page2)}</div><div class="sub">Position 10-30</div></div>
</div>

<div class="grid">
<div class="card">
<h2>🚨 Zero-CTR Queries (Priority Fix)</h2>
<table><thead><tr><th>Query</th><th>Impressions</th><th>Position</th><th>Action</th></tr></thead><tbody>
'''

for q in zero_ctr[:12]:
    query = q.get('Consultas principales', '')
    imps = int(q.get('Impresiones', 0) or 0)
    pos = float(q.get('Posición', 0) or 0)
    html += f'<tr><td class="query">{query}</td><td>{imps}</td><td>{pos:.1f}</td><td><span class="badge badge-danger">Fix meta</span></td></tr>\n'

html += '''</tbody></table>
</div>

<div class="card">
<h2>📈 Page 2 Opportunities</h2>
<table><thead><tr><th>Query</th><th>Impressions</th><th>Position</th><th>Action</th></tr></thead><tbody>
'''

for q in page2[:12]:
    query = q.get('Consultas principales', '')
    imps = int(q.get('Impresiones', 0) or 0)
    pos = float(q.get('Posición', 0) or 0)
    html += f'<tr><td class="query">{query}</td><td>{imps}</td><td>{pos:.1f}</td><td><span class="badge badge-warning">Improve</span></td></tr>\n'

html += '''</tbody></table>
</div>
</div>

<div class="grid">
<div class="card">
<h2>📄 Top Pages by Impressions</h2>
<table><thead><tr><th>Page</th><th>Clicks</th><th>Impressions</th><th>CTR</th><th>Pos</th></tr></thead><tbody>
'''

for p in top_pages[:15]:
    url = p.get('Páginas principales', '').replace('https://calcto.work/', '')
    clicks = int(p.get('Clics', 0) or 0)
    imps = int(p.get('Impresiones', 0) or 0)
    ctr = p.get('CTR', '0%')
    pos = float(p.get('Posición', 0) or 0)
    badge = 'badge-danger' if clicks==0 and imps>=50 else 'badge-success'
    html += f'<tr><td class="url">{url}</td><td>{clicks}</td><td>{imps}</td><td><span class="badge {badge}">{ctr}</span></td><td>{pos:.1f}</td></tr>\n'

html += '''</tbody></table>
</div>

<div class="card">
<h2>🌍 Top Countries</h2>
<table><thead><tr><th>Country</th><th>Clicks</th><th>Impressions</th><th>CTR</th><th>Pos</th></tr></thead><tbody>
'''

for c in sorted(countries, key=lambda x: -int(x.get('Impresiones', 0) or 0))[:12]:
    html += f'<tr><td>{c.get("País", "")}</td><td>{c.get("Clics", 0)}</td><td>{c.get("Impresiones", 0)}</td><td>{c.get("CTR", "0%")}</td><td>{float(c.get("Posición", 0) or 0):.1f}</td></tr>\n'

html += f'''</tbody></table>
</div>
</div>

<div class="grid">
<div class="card">
<h2>📊 Traffic by Category</h2>
<div class="chart-wrap"><canvas id="catChart"></canvas></div>
</div>

<div class="card">
<h2>✅ Action Plan</h2>
<div class="action"><span class="priority h">P0</span> <strong>Fix Meta Descriptions</strong><br><span class="sub">{len(zero_ctr)} queries have 0% CTR with 10+ impressions. Rewrite meta descriptions to be benefit-driven.</span></div>
<div class="action"><span class="priority h">P0</span> <strong>Add Featured Snippet Boxes</strong><br><span class="sub">Add quick-answer boxes to tile calculator, COP/EER calculator for position 0.</span></div>
<div class="action"><span class="priority m">P1</span> <strong>Improve Page 2 Rankings</strong><br><span class="sub">{len(page2)} queries rank position 10-30. Add internal links and expand content.</span></div>
<div class="action"><span class="priority m">P1</span> <strong>Fix Missing Content</strong><br><span class="sub">DE missing 4 files, PT missing 3 files. Restore from Git.</span></div>
<div class="action"><span class="priority l">P2</span> <strong>Build Collection Pages</strong><br><span class="sub">Create hub pages for category keywords.</span></div>
<div class="action"><span class="priority l">P2</span> <strong>Add Blog Section</strong><br><span class="sub">Publish 10-20 informational posts.</span></div>
</div>
</div>

</div>

<script>
new Chart(document.getElementById('catChart'),{{
type:'doughnut',
data:{{labels:{json.dumps(list(cats.keys()))},datasets:[{{data:{json.dumps([cats[c]["imps"] for c in cats])},backgroundColor:['#f97316','#3b82f6','#22c55e','#eab308','#ef4444','#8b5cf6']}}]}},
options:{{responsive:true,maintainAspectRatio:false,plugins:{{legend:{{position:'right'}}}}}}
}});
</script>
</body>
</html>
'''

DASHBOARD_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"[OK] Dashboard: {DASHBOARD_FILE}")
print(f"\nGSC Summary:")
print(f"  Queries: {len(queries):,}")
print(f"  Pages: {len(pages):,}")
print(f"  Clicks: {total_clicks}")
print(f"  Impressions: {total_impressions:,}")
print(f"  CTR: {avg_ctr:.2f}%")
print(f"  Zero-CTR (10+ imps): {len(zero_ctr)}")
print(f"  Page 2 Opps: {len(page2)}")
