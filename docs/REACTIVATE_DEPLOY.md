# Reactivating Deployment — CalcToWork

This guide explains how to get **`firebase deploy` working again** after it stopped
because of two separate, pre-existing problems:

1. **Hosting** is blocked by an exceeded **storage quota**.
2. **Functions** can't deploy because **`functions/package.json` is missing** from the repo
   (a blanket `*.json` rule in `.gitignore` prevented it from ever being committed).

Neither is caused by content changes — both are one-time infrastructure fixes.

> **Project:** `calctowork` · **Region:** `us-central1` · **Node (local):** v24.11.1
> **Python:** `C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe`

---

## Part A — Reactivate Hosting (storage quota)

### Symptom
```
Error: Request to https://firebasehosting.googleapis.com/... HTTP Error: 429,
You have exceeded the Hosting storage quota for your Firebase project,
so you cannot deploy to your site right now.
```

### Why
Every full deploy uploads ~19,000 files. Firebase keeps **all past versions** by default,
and on the Spark (free) plan they add up until you hit the storage cap.

### Fix (one-time, in the Firebase Console — cannot be done from the CLI)

1. Open the release-retention settings:
   **https://console.firebase.google.com/project/calctowork/hosting/sites**
2. Click the **⋮ (three-dot) menu** next to the `calctowork` site → **Release settings**
   (a.k.a. "Version history settings").
3. Set **"Retain the most recent"** to a small number — **5** is plenty.
4. Save. Firebase garbage-collects the old versions within a few minutes,
   which frees the storage.

> **Alternative:** Upgrade the project to the **Blaze** (pay-as-you-go) plan.
> Hosting storage stays effectively free at this scale, and this also unblocks
> Cloud Functions (Part B requires Blaze anyway to deploy).

### Verify the quota is freed
```powershell
firebase hosting:channel:list
```
You should still see just the `live` channel. Give it ~5 minutes after changing retention.

### Deploy
```powershell
# 1. Rebuild the static site (regenerates public/)
& "C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe" scripts/generate_calctowork.py

# 2. Deploy only hosting
firebase deploy --only hosting
```

> The recent **title / meta-description CTR changes only require hosting** — once this
> succeeds they are live at https://calcto.work.

---

## Part B — Reactivate Functions (missing package.json)

### Symptom
```
Error: Could not detect runtime for functions at C:\Users\julie\calctowork\functions
```

### Why
`.gitignore` line 7 is `*.json`, which silently excluded `functions/package.json`.
Without it, the Firebase CLI has no `engines`/dependency manifest, so it refuses to deploy.

### Fix

**1. `functions/package.json` is now committed in the repo** (Node 22 runtime; deps:
`cors`, `firebase-admin`, `firebase-functions`, `googleapis`, `node-fetch`, `nodemailer`).
It was reconstructed from the `require(...)` calls in the functions source.

**2. It is now un-ignored** via these lines already added to `.gitignore`:
```
!functions/package.json
!functions/package-lock.json
```

**3. Install dependencies**
```powershell
npm install --prefix functions
```
Verify the runtime is detected without actually deploying:
```powershell
firebase deploy --only functions --dry-run
```
A successful run ends with **"Dry run complete!"**. (You will see non-fatal warnings about
`firebase-functions` version and the `functions.config()` API being deprecated before
March 2027 — safe to ignore for now; see the migration note at the end.)

**4. (First time only) Set the GSC credentials** the functions need. If they were
already set on the project you can skip this; check with `firebase functions:config:get`.
```powershell
firebase functions:config:set gsc.client_id="YOUR_CLIENT_ID"
firebase functions:config:set gsc.client_secret="YOUR_CLIENT_SECRET"
firebase functions:config:set gsc.refresh_token="YOUR_REFRESH_TOKEN"
firebase functions:config:set gsc.site_url="sc-domain:calcto.work"
```

**5. Deploy the functions**
```powershell
firebase deploy --only functions
```

> Cloud Functions require the **Blaze** plan. If you get a billing error here,
> upgrade the project (this also permanently solves the Part A quota problem).

### Verify
```powershell
firebase functions:list
```
Confirm `getGscData`, `getAlerts`, `runAutoPilot`, `auditRisingPages` (and the rest) appear.

---

## Part C — Deploy Everything (normal workflow, once unblocked)

```powershell
# rebuild static site
& "C:\Users\julie\AppData\Local\Programs\Python\Python314\python.exe" scripts/generate_calctowork.py

# deploy hosting + functions + firestore indexes together
firebase deploy
```

Or target individually:
```powershell
firebase deploy --only hosting
firebase deploy --only functions
firebase deploy --only firestore:indexes
```

---

## Post-deploy checks

1. **CTR changes live:** open a fixed page and view source —
   https://calcto.work/en/bmr-mifflin-st-jeor/ should show the new `<title>` and
   `<meta name="description">`.
2. **Admin dashboard:** https://calctowork.web.app/admin-v2.html — data tabs now load
   (the fatal script error is fixed).
3. **GSC data:** in the dashboard, **Settings → "Fetch GSC Data Now"**, or:
   ```powershell
   curl "https://us-central1-calctowork.cloudfunctions.net/fetchGscOnDemand?days=30"
   ```

---

## Preventing this in the future

- Keep `!functions/package.json` in `.gitignore` (and commit `functions/package-lock.json`).
- Keep Hosting **retained releases** low (5) so storage never fills again.
- If you ever re-clone the repo, run `npm install --prefix functions` before deploying.

## Note: `functions.config()` deprecation (before March 2027)

The functions still use the legacy `functions.config()` API (for GSC credentials). Google is
retiring it in March 2027. When convenient, migrate to environment params:
```powershell
firebase functions:config:export   # interactive migration helper
```
See https://firebase.google.com/docs/functions/config-env#migrate-config — not urgent.
