# CalcToWork Analytics Setup Guide

## Admin Dashboard Access

**URL:** https://calctowork.web.app/admin.html

**Access Code:** `admin123`

## What You'll See

### Real-Time Metrics
- **Active Users** – Currently online visitors
- **Page Views** – Total page loads today
- **Calculations** – How many times users clicked "Calculate"
- **Avg Time on Page** – How long users stay
- **Copy Results** – How many users copy/share results
- **Bounce Rate** – Users who leave without calculating

### Charts
- Page views over time (hourly)
- Calculations over time (hourly)
- User actions breakdown
- Device breakdown (desktop/mobile/tablet)

### Tables
- **Top Calculators** – Which tools are most popular
- **Top Countries** – Where your users are from
- **Recent Activity** – Live event stream

## How to Update Firebase Config

The dashboard needs your Firebase API key to connect. Here's how to get it:

1. Go to https://console.firebase.google.com/project/calctowork/settings/general
2. Scroll down to "Your apps" section
3. Click the web app (</> icon)
4. Copy the `firebaseConfig` object
5. Open `public/admin.html` and replace:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",        // Replace this
  authDomain: "calctowork.firebaseapp.com",
  projectId: "calctowork",
  storageBucket: "calctowork.appspot.com",
  messagingSenderId: "YOUR_SENDER_ID",  // Replace this
  appId: "YOUR_APP_ID"                  // Replace this
};
```

## How to Deploy Cloud Functions

The analytics API needs Cloud Functions to receive data:

```bash
# Install Firebase CLI if not already installed
npm install -g firebase-tools

# Login to Firebase
firebase login

# Deploy functions
firebase deploy --only functions
```

## How to Enable Firestore

1. Go to https://console.firebase.google.com/project/calctowork/firestore
2. Click "Create database"
3. Choose "Start in production mode"
4. Select your region (europe-west1 recommended)

## Security Rules

After enabling Firestore, set these security rules:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /analytics_events/{document} {
      allow create: if true;  // Allow public writes
      allow read: if true;    // Allow dashboard reads
    }
    match /analytics_daily/{document} {
      allow read, write: if true;
    }
  }
}
```

> ⚠️ **Warning:** These rules allow public access. For production, add authentication.

## How Analytics Works

1. User visits calculator page
2. `analytics-tracker.js` sends events to Firebase
3. Events stored in Firestore collection `analytics_events`
4. Admin dashboard reads from Firestore
5. Data updates automatically every 30 seconds

## Events Tracked

| Event | Trigger | Data Collected |
|-------|---------|----------------|
| `page_view` | Page loads | URL, referrer, device info |
| `calculation_completed` | Click "Calculate" | Input values (anonymized), results count |
| `copy_results` | Click copy button | Calculator used |
| `share_clicked` | Click share | Social platform |
| `input_changed` | User types in field | Field name, has value |
| `scroll_depth` | Scrolls 25/50/75/100% | Scroll percentage |
| `time_on_page` | Every 10 seconds | Seconds on page |
| `exit_intent` | Mouse leaves page | Time on page, calculations done |

## Customizing Dashboard

### Change Access Code
Edit `public/admin.html`:
```javascript
if (code === 'admin123') {  // Change this
```

### Add More Charts
The dashboard uses Chart.js. Add new charts by:
1. Adding a `<canvas>` element to the HTML
2. Creating chart data in the `updateCharts()` function
3. Initializing with `new Chart()`

### Export Data
Add this button to export to CSV:
```javascript
function exportToCSV() {
  // Get data from Firestore
  // Convert to CSV format
  // Download file
}
```

## Troubleshooting

### Dashboard shows "Demo Mode"
- Firebase config not set correctly
- Firestore database not created
- No data collected yet (wait for users)

### No data appearing
- Check browser console for errors
- Verify Cloud Functions deployed: `firebase functions:list`
- Check Firestore has data: https://console.firebase.google.com/project/calctowork/firestore/data

### High costs
- Analytics events accumulate quickly
- Set up data retention (90 days recommended)
- The cleanup function runs daily at 2 AM

## Next Steps

1. ✅ Add Firebase config to admin.html
2. ✅ Enable Firestore database
3. ✅ Deploy Cloud Functions
4. ✅ Set Firestore security rules
5. ✅ Verify data collection
6. 🔄 Monitor for 24-48 hours
7. 🔄 Adjust based on insights
