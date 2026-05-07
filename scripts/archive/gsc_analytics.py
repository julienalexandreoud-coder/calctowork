import json
import sys
import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
SITE_URLS = ["https://calcto.work", "sc-domain:calcto.work", "calcto.work"]
SITE_URL = None
KEY_FILE = os.path.join(os.path.dirname(__file__), "..", "calctowork-3bfe4a8f9efd.json")

LANGS = ["es", "en", "fr", "pt", "de", "it"]


def get_service():
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    return build("searchconsole", "v1", credentials=creds)


def detect_site(service):
    global SITE_URL
    try:
        sites = service.sites().list().execute()
        available = [s["siteUrl"] for s in sites.get("siteEntry", [])]
        print(f"  Available GSC properties: {available}")
        for candidate in SITE_URLS:
            if candidate in available:
                SITE_URL = candidate
                print(f"  Using: {SITE_URL}")
                return
        if available:
            SITE_URL = available[0]
            print(f"  Using first available: {SITE_URL}")
    except Exception as e:
        print(f"  Could not auto-detect property: {e}")
        SITE_URL = SITE_URLS[0]


def query(service, start_date, end_date, dimensions=None, filters=None, row_limit=25000, start_row=0):
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions or ["page"],
        "rowLimit": row_limit,
        "startRow": start_row,
    }
    if filters:
        body["dimensionFilterGroups"] = [{"filters": filters}]
    return service.searchanalytics().query(siteUrl=SITE_URL, body=body).execute()


def fmt(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def run():
    print("=" * 70)
    print("  CalcToWork - Google Search Console Analytics")
    print("=" * 70)

    service = get_service()
    detect_site(service)

    end = datetime.now().strftime("%Y-%m-%d")
    start_7d = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    start_28d = (datetime.now() - timedelta(days=28)).strftime("%Y-%m-%d")
    start_90d = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")

    print(f"\n  Site:       {SITE_URL}")
    print(f"  Last 7 days:  {start_7d} -> {end}")
    print(f"  Last 28 days: {start_28d} -> {end}")
    print(f"  Last 90 days: {start_90d} -> {end}")

    # ── 1. Overview ──
    print("\n" + "─" * 70)
    print("  1. OVERVIEW (last 28 days)")
    print("─" * 70)

    for period, s, e in [("7d", start_7d, end), ("28d", start_28d, end), ("90d", start_90d, end)]:
        data = query(service, s, e, dimensions=["page"])
        if not data:
            print(f"\n  {period}: No data returned.")
            continue
        rows = data.get("rows", [])
        total_clicks = sum(r.get("clicks", 0) for r in rows)
        total_impressions = sum(r.get("impressions", 0) for r in rows)
        total_ctr = (total_clicks / total_impressions * 100) if total_impressions else 0
        avg_pos = sum(r.get("position", 0) * r.get("impressions", 1) for r in rows) / max(total_impressions, 1)
        print(f"\n  {period}: {fmt(total_clicks)} clicks | {fmt(total_impressions)} impressions | CTR {total_ctr:.1f}% | Avg position {avg_pos:.1f}")

    # ── 2. Top Pages ──
    print("\n" + "─" * 70)
    print("  2. TOP 30 PAGES by clicks (last 28 days)")
    print("─" * 70)

    data = query(service, start_28d, end, dimensions=["page"])
    if data:
        rows = sorted(data.get("rows", []), key=lambda r: r.get("clicks", 0), reverse=True)
        for i, r in enumerate(rows[:30], 1):
            page = r["keys"][0].replace(SITE_URL, "")
            print(f"  {i:2}. {fmt(r['clicks']):>6} clicks | {fmt(r['impressions']):>7} imp | CTR {r['ctr']*100:5.1f}% | pos {r['position']:5.1f} | {page}")

    # ── 3. Top Queries ──
    print("\n" + "─" * 70)
    print("  3. TOP 30 QUERIES by clicks (last 28 days)")
    print("─" * 70)

    data = query(service, start_28d, end, dimensions=["query"])
    if data:
        rows = sorted(data.get("rows", []), key=lambda r: r.get("clicks", 0), reverse=True)
        for i, r in enumerate(rows[:30], 1):
            print(f"  {i:2}. {fmt(r['clicks']):>6} clicks | {fmt(r['impressions']):>7} imp | CTR {r['ctr']*100:5.1f}% | pos {r['position']:5.1f} | {r['keys'][0]}")

    # ── 4. High Impression, Low CTR (opportunities) ──
    print("\n" + "─" * 70)
    print("  4. OPPORTUNITIES: High impressions, LOW CTR (last 28 days)")
    print("─" * 70)

    data = query(service, start_28d, end, dimensions=["page"])
    if data:
        rows = sorted(data.get("rows", []), key=lambda r: r.get("impressions", 0), reverse=True)
        opps = [r for r in rows if r.get("impressions", 0) >= 10 and r.get("ctr", 0) < 0.03]
        for i, r in enumerate(opps[:20], 1):
            page = r["keys"][0].replace(SITE_URL, "")
            print(f"  {i:2}. {fmt(r['impressions']):>7} imp | CTR {r['ctr']*100:5.1f}% | pos {r['position']:5.1f} | {page}")

    # ── 5. Per-Language Breakdown ──
    print("\n" + "─" * 70)
    print("  5. PER-LANGUAGE BREAKDOWN (last 28 days)")
    print("─" * 70)

    data = query(service, start_28d, end, dimensions=["page"])
    if data:
        lang_stats = {}
        for r in data.get("rows", []):
            page = r["keys"][0]
            lang = "other"
            for l in LANGS:
                if f"/{l}/" in page:
                    lang = l
                    break
            if lang not in lang_stats:
                lang_stats[lang] = {"clicks": 0, "impressions": 0, "ctr_sum": 0, "pos_sum": 0, "count": 0}
            lang_stats[lang]["clicks"] += r.get("clicks", 0)
            lang_stats[lang]["impressions"] += r.get("impressions", 0)
            lang_stats[lang]["count"] += 1

        for lang in sorted(lang_stats, key=lambda x: lang_stats[x]["clicks"], reverse=True):
            s = lang_stats[lang]
            ctr = (s["clicks"] / s["impressions"] * 100) if s["impressions"] else 0
            print(f"  /{lang}/  {fmt(s['clicks']):>6} clicks | {fmt(s['impressions']):>7} imp | CTR {ctr:5.1f}% | {s['count']} pages")

    # ── 6. Top Queries Per Page (for top 10 pages) ──
    print("\n" + "─" * 70)
    print("  6. TOP QUERIES for TOP 10 PAGES (last 28 days)")
    print("─" * 70)

    data = query(service, start_28d, end, dimensions=["page"])
    if data:
        top_pages = sorted(data.get("rows", []), key=lambda r: r.get("clicks", 0), reverse=True)[:10]
        for r in top_pages:
            page = r["keys"][0]
            short = page.replace(SITE_URL, "")
            print(f"\n  >> {short} ({fmt(r['clicks'])} clicks, {fmt(r['impressions'])} imp)")

            qdata = query(
                service, start_28d, end,
                dimensions=["query"],
                filters=[{"dimension": "page", "operator": "equals", "expression": page}],
            )
            if qdata:
                qrows = sorted(qdata.get("rows", []), key=lambda x: x.get("clicks", 0), reverse=True)
                for qr in qrows[:5]:
                    print(f"      {fmt(qr['clicks']):>5} clicks | {fmt(qr['impressions']):>6} imp | pos {qr['position']:5.1f} | {qr['keys'][0]}")

    # ── 7. Index Coverage ──
    print("\n" + "─" * 70)
    print("  7. SITEMAP STATUS")
    print("─" * 70)

    try:
        sitemaps = service.sitemaps().list(siteUrl=SITE_URL).execute()
        sm = sitemaps.get("sitemap", [])
        if sm:
            for s in sm:
                print(f"  {s.get('path', '?')} — last submitted: {s.get('lastSubmitted', '?')} — errors: {s.get('errors', 0)} — warnings: {s.get('warnings', 0)}")
        else:
            print("  No sitemaps found.")
    except Exception as e:
        print(f"  Could not fetch sitemap info: {e}")

    print("\n" + "=" * 70)
    print("  Done.")
    print("=" * 70)


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"\nERROR: {e}")
        if "403" in str(e) or "forbidden" in str(e).lower():
            print("\n  The service account needs access to Search Console.")
            print(f"  Add this email as a user in GSC:")
            print(f"  gsc-reader@gen-lang-client-0595392380.iam.gserviceaccount.com")
            print(f"\n  Go to: https://search.google.com/search-console → Settings → Users and permissions → Add user")
        sys.exit(1)
