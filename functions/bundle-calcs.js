/**
 * Copies src/calculators/ JSON files into functions/calcs/
 * Run: node functions/bundle-calcs.js
 */
const fs = require('fs');
const path = require('path');

const SRC = path.join(__dirname, '..', 'src', 'calculators');
const DST = path.join(__dirname, 'calcs');

if (!fs.existsSync(SRC)) { console.error('src/calculators not found'); process.exit(1); }
fs.mkdirSync(DST, { recursive: true });

const ids = fs.readdirSync(SRC).filter(id => fs.statSync(path.join(SRC, id)).isDirectory());
let count = 0;

for (const id of ids) {
  const srcDir = path.join(SRC, id);
  const dstDir = path.join(DST, id);
  fs.mkdirSync(dstDir, { recursive: true });

  const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.json'));
  for (const f of files) {
    fs.copyFileSync(path.join(srcDir, f), path.join(dstDir, f));
    count++;
  }
}

console.log(`Copied ${count} JSON files for ${ids.length} calculators to functions/calcs/`);
