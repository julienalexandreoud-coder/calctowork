/**
 * CalcToWork Analytics API
 * Receives and stores user interaction events in Firestore
 */

const functions = require("firebase-functions");
const admin = require("firebase-admin");

admin.initializeApp();
const db = admin.firestore();

const cors = require("cors")({ origin: true });

// Analytics endpoint - receives batched events
exports.analytics = functions.https.onRequest((req, res) => {
  return cors(req, res, async () => {
    // Only accept POST
    if (req.method !== "POST") {
      return res.status(405).send("Method Not Allowed");
    }

    const events = req.body;
    
    if (!Array.isArray(events) || events.length === 0) {
      return res.status(400).send("Invalid events array");
    }

    try {
      // Process events in batches
      const batch = db.batch();
      const now = admin.firestore.FieldValue.serverTimestamp();

      for (const event of events) {
        // Validate required fields
        if (!event.event_name || !event.session_id) {
          continue;
        }

        // Create document reference
        const eventRef = db.collection("analytics_events").doc();
        
        // Prepare event data
        const eventData = {
          event_name: event.event_name,
          event_time: event.event_time ? new Date(event.event_time) : now,
          session_id: event.session_id,
          user_id: event.user_id || null,
          page_url: event.page_url || null,
          page_title: event.page_title || null,
          calc_id: event.calc_id || null,
          calc_slug: event.calc_slug || null,
          referrer: event.referrer || null,
          user_agent: event.user_agent || null,
          language: event.language || null,
          screen_width: event.screen_width || null,
          screen_height: event.screen_height || null,
          viewport_width: event.viewport_width || null,
          viewport_height: event.viewport_height || null,
          device_memory: event.device_memory || null,
          connection: event.connection || null,
          // Event-specific fields
          inputs_filled: event.inputs_filled || null,
          inputs_total: event.inputs_total || null,
          results_count: event.results_count || null,
          calculation_number: event.calculation_number || null,
          time_to_calculate: event.time_to_calculate || null,
          time_on_page: event.time_on_page || null,
          calculations_done: event.calculations_done || null,
          field_id: event.field_id || null,
          field_name: event.field_name || null,
          has_value: event.has_value || null,
          percent: event.percent || null,
          created_at: now,
        };

        batch.set(eventRef, eventData);
      }

      await batch.commit();

      // Also update daily aggregates
      await updateDailyAggregates(events);

      res.status(200).send("OK");
    } catch (error) {
      console.error("Analytics error:", error);
      res.status(500).send("Internal Server Error");
    }
  });
});

// Update daily aggregate statistics
async function updateDailyAggregates(events) {
  const today = new Date();
  const dateStr = today.toISOString().split('T')[0]; // YYYY-MM-DD
  
  const aggregates = {
    page_views: 0,
    calculations: 0,
    unique_sessions: new Set(),
    unique_users: new Set(),
    calculators_used: new Set(),
  };

  for (const event of events) {
    if (event.session_id) aggregates.unique_sessions.add(event.session_id);
    if (event.user_id) aggregates.unique_users.add(event.user_id);
    if (event.calc_slug) aggregates.calculators_used.add(event.calc_slug);
    
    if (event.event_name === 'page_view') aggregates.page_views++;
    if (event.event_name === 'calculation_completed') aggregates.calculations++;
  }

  const aggRef = db.collection("analytics_daily").doc(dateStr);
  
  await db.runTransaction(async (transaction) => {
    const aggDoc = await transaction.get(aggRef);
    const current = aggDoc.exists ? aggDoc.data() : {};

    transaction.set(aggRef, {
      date: dateStr,
      page_views: admin.firestore.FieldValue.increment(aggregates.page_views),
      calculations: admin.firestore.FieldValue.increment(aggregates.calculations),
      unique_sessions: admin.firestore.FieldValue.increment(aggregates.unique_sessions.size),
      unique_users: admin.firestore.FieldValue.increment(aggregates.unique_users.size),
      calculators_used: admin.firestore.FieldValue.arrayUnion(...Array.from(aggregates.calculators_used)),
      updated_at: admin.firestore.FieldValue.serverTimestamp(),
    }, { merge: true });
  });
}

// Scheduled function to cleanup old events (keep 90 days)
exports.cleanupOldEvents = functions.pubsub
  .schedule('0 2 * * *') // Daily at 2 AM
  .timeZone('UTC')
  .onRun(async (context) => {
    const cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - 90);

    const snapshot = await db.collection("analytics_events")
      .where("created_at", "<", cutoff)
      .limit(1000)
      .get();

    const batch = db.batch();
    snapshot.docs.forEach(doc => batch.delete(doc.ref));
    
    await batch.commit();
    
    console.log(`Deleted ${snapshot.size} old analytics events`);
    return null;
  });
