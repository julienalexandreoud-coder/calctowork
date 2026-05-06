const fs = require('fs');
const text = fs.readFileSync('C:/Microsaas/obra/src/i18n/de.json','utf8');
let depth = 0, inString = false, escape = false;
for (let i = 0; i < text.length; i++) {
  const ch = text[i];
  if (escape) { escape = false; continue; }
  if (ch === '\\') { escape = true; continue; }
  if (ch === '"') { inString = !inString; continue; }
  if (inString) continue;
  if (ch === '{' || ch === '[') depth++;
  if (ch === '}') { depth--; if (depth === 0) { console.log('Root closed at position', i, 'line', text.substring(0,i).split('\n').length); } }
  if (ch === ']') { depth--; }
}
console.log('Final depth:', depth);
