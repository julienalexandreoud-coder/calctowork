# CalcToWork Growth Dashboard — Architecture & Implementation Plan

## Overview
This is the pillar of CalcToWork's growth. A single professional dashboard that unifies:
- **Google Search Console** (queries, clicks, impressions, CTR, positions, indexation)
- **User Analytics** (visitors, calculations, conversions, bounce, behaviour)
- **Content Performance** (calculator-level metrics, efficiency scores)
- **Alerts & Monitoring** (traffic drops, indexation issues, opportunities)
- **Export & Reporting** (CSV, PDF, scheduled reports)

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Admin Dashboard V2                      │
│              (public/admin-v2.html)                       │
│    Single-page app with 8 tabs, Chart.js, real-time       │
└──────────┬──────────────────────────────────┬───────────┘
           │                                  │
    Firestore SDK                     REST API calls
    (onSnapshot)                      (fetch JSON)
           │                                  │
┌──────────▼──────────┐    ┌──────────────────▼──────────┐
│  Firestore Database │    │   Firebase Cloud Functions  │
│                     │    │                              │
│ analytics_events    │    │ getGscData ───────────┐     │
│ analytics_daily     │◄───│ aggregateDailyStats    │     │
│ gsc_search_data     │◄───│ fetchGscData (cron) ──►│ GSC │
│ gsc_page_data       │◄───│ checkAlerts (cron)     │ API │
│ dashboard_alerts    │◄───│ getAggregatedData      │     │
│ dashboard_config    │    │ getAlerts              │     │
└─────────────────────┘    └──────────────────────────────┘
```

## Data Pipeline

### 1. Real-time events → Firestore (already working)
`public/js/analytics-tracker.js` writes events to `analytics_events` collection.
Fields: event_name, event_time, session_id, user_id, calc_slug, language, is_bot, etc.

### 2. GSC data → Firestore (NEW — Firebase Function)
`functions/gsc-collector.js` — Scheduled daily at 3 AM UTC:
- Fetches search analytics from GSC API (last 90 days)
- Dimensions: query, page, country, device
- Stores in `gsc_search_data` collection
- Also fetches sitemap status and coverage issues
- Stores in `gsc_page_stats` and `gsc_coverage`

### 3. Analytics aggregation → Firestore (NEW — Firebase Function)
`functions/aggregator.js` — Scheduled daily at 2 AM UTC:
- Aggregates yesterday's `analytics_events` into `analytics_daily`
- Groups by: calculator_slug, language, date
- Computes: page_views, calculations, copies, shares, avg_time, bounce_rate, unique_users, sessions

### 4. Alert detection (NEW — Firebase Function)
`functions/alerting.js` — Scheduled daily at 4 AM UTC:
- Compares today vs yesterday, this week vs last week
- Detects: traffic drops >30%, indexation drops, ranking anomalies
- Creates alert documents in `dashboard_alerts`

## Firestore Collections

### `analytics_events` (existing)
Raw user interaction events. 90-day TTL recommended.

### `analytics_daily` (NEW)
```
{
  date: "2026-05-07",
  calculator_slug: "calculadora-hormigon-masa",
  calculator_id: "001",
  block: "estructuras",
  language: "es",
  page_views: 150,
  calculations: 45,
  copies: 12,
  shares: 3,
  avg_time_seconds: 52,
  unique_users: 38,
  sessions: 42,
  bounced_sessions: 25
}
```

### `gsc_search_data` (NEW)
```
{
  date: "2026-05-04",
  query: "calculadora hormigon",
  clicks: 12,
  impressions: 150,
  ctr: 0.08,
  position: 4.5,
  page: "/es/estructuras/calculadora-hormigon-masa/",
  country: "esp",
  device: "DESKTOP",
  site_url: "https://calcto.work"
}
```

### `gsc_page_stats` (NEW)
```
{
  date: "2026-05-04",
  page: "/es/estructuras/calculadora-hormigon-masa/",
  total_clicks: 45,
  total_impressions: 580,
  avg_ctr: 0.078,
  avg_position: 6.2,
  query_count: 12
}
```

### `gsc_site_stats` (NEW)
```
{
  date: "2026-05-04",
  site_url: "https://calcto.work",
  total_clicks: 1200,
  total_impressions: 25000,
  avg_ctr: 0.048,
  avg_position: 14.3,
  pages_with_clicks: 85,
  total_queries: 210
}
```

### `dashboard_alerts` (NEW)
```
{
  created_at: <timestamp>,
  type: "traffic_drop" | "traffic_spike" | "indexation_issue" | "ranking_change",
  severity: "high" | "medium" | "low",
  title: "Organic clicks dropped 35% vs last week",
  metric: "clicks",
  current_value: 800,
  previous_value: 1230,
  change_pct: -35,
  acknowledged: false
}
```

### `dashboard_config` (NEW)
```
{
  gsc_site_url: "https://calcto.work",
  alert_click_drop_pct: 25,
  alert_impression_drop_pct: 30,
  data_retention_events_days: 90,
  report_recipients: ["user@email.com"]
}
```

## Dashboard V2 — Tab Structure

### Tab 1: 📊 Overview
- **KPI Row**: Organic Clicks, Impressions, Avg CTR, Avg Position, Users, Page Views, Calculations, Bounce Rate
- **Sparklines**: 7-day mini trend on each KPI
- **Chart Row 1**: Clicks & Impressions over time (dual-axis line chart)
- **Chart Row 2**: Top 10 queries (horizontal bar) | Top 10 pages (horizontal bar)
- **Chart Row 3**: Device split (donut) | Language split (donut)
- **Alert Panel**: Unacknowledged alerts with severity badges

### Tab 2: 🔍 Search Console
- **Filters**: Date range, country dropdown, device dropdown, search type
- **Chart**: Clicks & impressions over time
- **Position distribution**: Position 1-3, 4-10, 11-20, 21+ (donut)
- **Query table**: Query, Clicks, Impr, CTR, Position. Sortable. Click for drill-down.
- **Page table**: Page, Clicks, Impr, CTR, Avg Position. Sortable. Click for drill-down.
- **Drill-down modal**: When clicking a query/page, shows detail with trend

### Tab 3: 📝 Content Performance
- **Calculator table** (enhanced): Calculator, Views, Calcs, Conv%, Bounce%, Avg Time, GSC Clicks, GSC Impr, GSC Position, Efficiency Score
- **Efficiency Score**: (Organic Clicks / Page Views) × 100 — how well content converts impressions to visits
- **Underperforming flagger**: Calcs with high impressions but low clicks (CTR < 1%)
- **Language comparison**: Side-by-side table of same calculator across languages
- **Content freshness**: Days since last update, sorted

### Tab 4: 📈 Traffic Analytics
- **Real-time**: Active users counter with 5-min refresh
- **Traffic sources**: Organic, Direct, Referral, Social (pie chart)
- **Geographic**: Country table from GSC + analytics language data
- **Time patterns**: Hourly heatmap (24h × 7d)
- **Device breakdown**: Desktop/Mobile/Tablet with trends
- **Browser breakdown**: Pie chart

### Tab 5: 🎯 Conversions
- **Full funnel**: Page View → Calculation → Copy/Share → Email Capture
- **Funnel visualization**: Horizontal bar at each stage with drop-off %
- **Email captures**: Count, rate, trend
- **Affiliate clicks**: By calculator, by program
- **Time to first calculation**: Distribution histogram
- **Calculations per session**: Distribution

### Tab 6: ⚙️ Technical SEO
- **Indexation status**: Indexed / Submitted / Not indexed (from GSC)
- **Coverage issues**: Table of URLs with issues (crawled_not_indexed, soft_404, etc.)
- **Sitemap status**: Submitted, last crawled, errors
- **Crawl stats**: Pages crawled per day (from GSC)

### Tab 7: 🔔 Alerts
- **Alert list**: Type, severity, message, date, status
- **Filters**: Acknowledged/unacknowledged, by type, by severity
- **Actions**: Acknowledge, dismiss

### Tab 8: ⚡ Settings
- GSC site URL management
- Alert thresholds (traffic drop %, impression drop %)
- Data refresh intervals
- Export settings
- Cache management

## Implementation Files

### New Files Created:
| File | Purpose |
|------|---------|
| `public/admin-v2.html` | Main dashboard page (~3000 lines) |
| `functions/gsc-collector.js` | GSC API data fetcher |
| `functions/aggregator.js` | Daily analytics aggregation |
| `functions/alerting.js` | Anomaly detection |
| `functions/package.json` | Updated dependencies |

### Existing Files Modified:
| File | Change |
|------|--------|
| `functions/index.js` | Add new endpoints, scheduled functions |
| `firestore.indexes.json` | Add composite indexes |

## Deployment Process

1. **Install dependencies**: `cd functions && npm install`
2. **Set GSC credentials as environment variables** in Firebase:
   - `GSC_CLIENT_ID`
   - `GSC_CLIENT_SECRET`  
   - `GSC_REFRESH_TOKEN`
3. **Deploy functions**: `firebase deploy --only functions`
4. **Deploy hosting**: `firebase deploy --only hosting`
5. **Access**: https://calctowork.web.app/admin-v2.html

## Future Enhancements (Phase 2)
- AdSense revenue integration
- Competitor keyword tracking
- AI-powered content recommendations
- Automated weekly PDF reports email
- Slack/Telegram alert notifications
- BigQuery pipeline for advanced analytics
- Heatmap and session recording
- A/B test integration
