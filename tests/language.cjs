const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html = fs.readFileSync('index.html', 'utf8');
const elements = [...html.matchAll(/data-en="([^"]*)" data-zh="([^"]*)"/g)].map(match => ({
  dataset: { en: match[1], zh: match[2] }, textContent: match[1]
}));
assert.ok(elements.length > 40, 'Expected bilingual page content');
let click;
const button = { hidden: true, setAttribute() {}, addEventListener(event, handler) { assert.equal(event, 'click'); click = handler; } };
const document = {
  documentElement: { lang: 'en' },
  getElementById(id) { assert.equal(id, 'language'); return button; },
  querySelectorAll(selector) { assert.equal(selector, '[data-en][data-zh]'); return elements; },
  querySelector() { return { setAttribute() {} }; }
};
vm.runInNewContext(fs.readFileSync('script.js', 'utf8'), { document });
assert.equal(button.hidden, false);
for (const language of ['zh', 'en', 'zh', 'en']) {
  click();
  assert.equal(document.documentElement.lang, language === 'zh' ? 'zh-CN' : 'en');
  for (const element of elements) assert.equal(element.textContent, element.dataset[language]);
  assert.equal(button.textContent, language === 'en' ? '中文' : 'English');
}
console.log(`PASS: ${elements.length} bilingual elements; repeated language switching`);
