# CalcToWork Growth Dashboard — Deployment Tutorial

## What We Built

A professional growth dashboard with **8 tabs** integrating Google Search Console, real-time analytics, content performance, traffic patterns, conversion funnels, technical SEO, anomaly alerts, and configuration. All powered by Firebase Cloud Functions + Firestore.

### Files Created:
```
functions/
├── gsc-collector.js    ← Fetches GSC data daily (queries, pages, stats, coverage)
├── aggregator.js       ← Aggregates analytics events into daily summaries
├── alerting.js         ← Detects traffic anomalies and creates alerts
├── index.js            ← Updated with new function exports
└── package.json        ← Updated with googleapis dependency

public/
└── admin-v2.html       ← The professional dashboard (single file, ~2000 lines)

src/
└── admin-v2.html       ← Source copy (for generator)

config/
└── firestore.indexes.json  ← Updated with composite indexes

scripts/
└── generate_calctowork.py  ← Updated to copy admin-v2.html

GROWTH_DASHBOARD_PLAN.md   ← Full architecture document
```

---

## Step-by-Step Deployment

### Step 1: Set GSC credentials as Firebase environment variables

These are already in your `gsc-credentials.json` and `gsc-token.json`. Copy them:

```bash
# From your home directory
cd C:\Users\julie

# Set each one (you already have these values in gsc-credentials.json and gsc-token.json)
firebase functions:config:set gsc.client_id="YOUR_CLIENT_ID"
firebase functions:config:set gsc.client_secret="YOUR_CLIENT_SECRET"
firebase functions:config:set gsc.refresh_token="YOUR_REFRESH_TOKEN"
firebase functions:config:set gsc.site_url="sc-domain:calcto.work"
```

**IMPORTANT**: The refresh token expires. If GSC functions stop working, regenerate:
```bash
# Run the CLI to refresh the token
cd C:\Users\julie
python gsc.py sites
# This auto-refreshes gsc-token.json. Then copy the new refresh_token from it.
```

### Step 2: Install new npm dependencies

```bash
cd C:\Microsaas\obra\functions
npm install
```

### Step 3: Deploy Firestore indexes

```bash
cd C:\Microsaas\obra
firebase deploy --only firestore:indexes
```

Wait 5-10 minutes for indexes to build in Firebase console before Step 5.

### Step 4: Deploy the dashboard (static HTML)

```bash
cd C:\Microsaas\obra
python scripts/generate_calctowork.py
firebase deploy --only hosting
```

Verify: https://calctowork.web.app/admin-v2.html (password: admin123)

### Step 5: Deploy the Cloud Functions

```bash
cd C:\Microsaas\obra
firebase deploy --only functions
```

Wait for deployment to complete. You'll see URLs like:
- `https://us-central1-calctowork.cloudfunctions.net/getGscData`
- `https://us-central1-calctowork.cloudfunctions.net/getAggregatedData`
- `https://us-central1-calctowork.cloudfunctions.net/getAlerts`
- `https://us-central1-calctowork.cloudfunctions.net/fetchGscOnDemand`

### Step 6: Trigger the first GSC data fetch

```bash
# Option A: Via the dashboard
# Go to Settings tab → Click "Fetch GSC Data Now"

# Option B: Via curl
curl "https://us-central1-calctowork.cloudfunctions.net/fetchGscOnDemand?days=30"
```

### Step 7: Verify it works

1. Open https://calctowork.web.app/admin-v2.html
2. Login with password: `admin123`
3. Check the **Overview tab** — you should see GSC data appearing
4. Check the **Search Console tab** — queries and pages tables
5. Check the **Alerts tab** — any anomalies detected

---

## What Each Tab Shows

| Tab | Data Source | What You See |
|-----|------------|-------------|
| **Overview** | Firestore + GSC | 8 big KPIs, clicks/impr chart, views/calcs chart, top queries/pages, alert panel |
| **Search Console** | GSC via API | Full query table, page table, CTR by position, position distribution, device filters |
| **Content** | Firestore events | Calculator performance with GSC columns, language breakdown, category breakdown |
| **Traffic** | Firestore events | Users/sessions, device/browser charts, hourly activity heatmap |
| **Conversions** | Firestore events | Funnel visualization (view→calc→copy→share), time to first calc, calcs per session |
| **Technical SEO** | GSC coverage | Coverage issues table, site stats summary (clicks, impr, CTR, position) |
| **Alerts** | Cloud Function | Traffic drops, impression drops, CTR changes, coverage issues — dismissable |
| **Settings** | Config | Quick action buttons (fetch GSC, open Firestore/Functions/GSC consoles), data freshness info |

---

## Scheduled Functions (automatic)

| Function | Schedule | What It Does |
|----------|----------|-------------|
| `fetchGscData` | Daily 3 AM UTC | Pulls 90 days of GSC search analytics, page stats, site stats, coverage issues |
| `aggregateDailyStats` | Daily 2 AM UTC | Aggregates yesterday's raw events into calculator-level daily summaries |
| `checkAlerts` | Daily 4 AM UTC | Compares current vs previous week, detects anomalies >25% change |

---

## Troubleshooting

### "Loading GSC data..." never loads
The Cloud Functions need to be deployed. Check:
```bash
firebase functions:list
```
If `getGscData` is not listed, run `firebase deploy --only functions`.

### GSC data shows zero
First-time fetch needed. Go to Settings → "Fetch GSC Data Now". Or the daily cron will pick it up at 3 AM UTC.

### "Coverage issues" empty
This is actually good — means no indexation problems. If you want to see issues, open GSC Console directly.

### Refresh token expired
```bash
cd C:\Users\julie
python gsc.py sites  # This refreshes the token
# Then get the new refresh_token from gsc-token.json and update:
firebase functions:config:set gsc.refresh_token="NEW_TOKEN"
firebase deploy --only functions
```

### Dashboard shows "No data for this period"
The dashboard queries the last N events (10k max). For older data, use Firestore Console to query directly.

---

## Growth Tips (How to Use This Dashboard)

1. **Check Overview daily** — Watch for drops in organic clicks or impressions
2. **Sort Content by GSC Position** — Find calculators ranking 11-20 and optimize them to get to page 1
3. **Watch Bounce Rate** — High bounce + high impressions = poor content. Add more value.
4. **Search Console tab** — Find queries with high impressions but low CTR. Improve your titles.
5. **Conversion funnel** — Identify where users drop off. If many view but few calculate, simplify the form.
6. **Alerts** — Act on red alerts immediately. Dismiss false alarms.

## Next Phase (Future)
- AdSense revenue dashboard
- Competitor keyword tracking
- Automated weekly email reports
- AI content recommendations
