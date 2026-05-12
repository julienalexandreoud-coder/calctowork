/**
 * CalcToWork Analytics API
 * Receives and stores user interaction events in Firestore
 * Also exports GSC collector, aggregator, and alerting functions
 */

const functions = require("firebase-functions");
const admin = require("firebase-admin");

admin.initializeApp();
const db = admin.firestore();

const cors = require("cors")({ origin: ['https://calcto.work', 'https://calctowork.web.app'] });

// Simple in-memory rate limiter (per IP, 60s window)
const rateLimit = new Map();
function checkRateLimit(ip) {
  const now = Date.now();
  const windowMs = 60000;
  const maxReq = 10;
  const entry = rateLimit.get(ip);
  if (!entry || entry.reset < now) {
    rateLimit.set(ip, { count: 1, reset: now + windowMs });
    return true;
  }
  if (entry.count >= maxReq) return false;
  entry.count++;
  return true;
}

// Analytics endpoint - receives batched events
exports.analytics = functions.https.onRequest((req, res) => {
  return cors(req, res, async () => {
    // Rate limit
    const clientIp = req.headers['x-forwarded-for'] || req.connection.remoteAddress || 'unknown';
    if (!checkRateLimit(clientIp)) {
      return res.status(429).send("Too Many Requests");
    }
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
          is_bot: event.is_bot || false,
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
      res.status(200).send("OK");
    } catch (error) {
      console.error("Analytics error:", error);
      res.status(500).send("Internal Server Error");
    }
  });
});

// Simple health check endpoint
exports.health = functions.https.onRequest((req, res) => {
  res.status(200).json({ status: "ok", timestamp: new Date().toISOString() });
});

// ── GSC Integration ──
const gscCollector = require("./gsc-collector");
exports.fetchGscData = gscCollector.fetchGscData;
exports.fetchGscOnDemand = gscCollector.fetchGscOnDemand;
exports.getGscData = gscCollector.getGscData;
exports.getMovement = gscCollector.getMovement;
exports.getIndexCoverage = gscCollector.getIndexCoverage;
exports.sendWeeklyDigest = gscCollector.sendWeeklyDigest;

// ── Analytics Aggregation ──
const aggregator = require("./aggregator");
exports.aggregateDailyStats = aggregator.aggregateDailyStats;
exports.aggregateOnDemand = aggregator.aggregateOnDemand;
exports.getAggregatedData = aggregator.getAggregatedData;

// ── Alerting ──
const alerting = require("./alerting");
exports.checkAlerts = alerting.checkAlerts;
exports.getAlerts = alerting.getAlerts;

// ── Calculator CMS ──
const calcPage = require("./calc-page");
exports.calcPage = calcPage.calcPage;
exports.translateCalc = calcPage.translateCalc;
exports.generateLongContent = calcPage.generateLongContent;
exports.retranslateLongContent = calcPage.retranslateLongContent;
exports.getCalcData = calcPage.getCalcData;
exports.publishCalcToHosting = calcPage.publishCalcToHosting;
exports.callAI = calcPage.callAI;
exports.saveAIConfig = calcPage.saveAIConfig;
exports.getAIConfig = calcPage.getAIConfig;
exports.generateCalcFromPrompt = calcPage.generateCalcFromPrompt;

// ── Autonomous Growth ──
exports.sitemap = calcPage.sitemap;
exports.findKeywordOpportunities = calcPage.findKeywordOpportunities;
exports.findKeywordOpportunitiesHttp = calcPage.findKeywordOpportunitiesHttp;
exports.generateSEOSuggestions = calcPage.generateSEOSuggestions;
exports.generateSEOSuggestionsHttp = calcPage.generateSEOSuggestionsHttp;
exports.generateGrowthReport = calcPage.generateGrowthReport;
exports.generateGrowthReportHttp = calcPage.generateGrowthReportHttp;
exports.runAutoPilot = calcPage.runAutoPilot;
exports.runAutoPilotHttp = calcPage.runAutoPilotHttp;
