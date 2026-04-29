const fs = require('fs');

// Read the calculators.json file
const data = JSON.parse(fs.readFileSync('src/calculators/calculators.json', 'utf8'));

// Fields to extract (keep example_inputs as-is)
const fieldsToExtract = ['example_label', 'range_hints', 'result_context', 'formula_display', 'steps', 'mistakes', 'input_type_review'];

// Extract fields for all calculators (text is already in Spanish)
const output = data.calculators.map(calc => {
    const extracted = {
        id: calc.id,
        slug: calc.slug,
        example_inputs: calc.example_inputs || {}
    };
    
    for (const field of fieldsToExtract) {
        extracted[field] = calc[field] || null;
    }
    
    return extracted;
});

// Save to i18n_es.json with UTF-8 encoding (no BOM)
fs.writeFileSync('i18n_es.json', JSON.stringify(output, null, 2), 'utf8');

console.log(`Extracted ${output.length} calculators to i18n_es.json`);
