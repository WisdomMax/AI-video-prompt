/**
 * Runway Wan 3.0 Auto Generator Script for Aside REPL
 * Usage: node runner or via `aside repl`
 */

const fs = require('fs');

async function checkRunwayStatus(page) {
  const s = await snapshot(page, { interactive: true });
  const hasGenerate = s.tree.includes('button "Generate"');
  const isGenerating = s.tree.includes('button "Generating"') || s.tree.includes('button "Queued"') || s.tree.includes('%');
  return { hasGenerate, isGenerating, tree: s.tree };
}

async function injectPartPrompt(page, promptText) {
  const s = await snapshot(page, { interactive: true });
  const promptMatch = s.tree.match(/textbox \"Prompt\" \[ref=(e\d+)\]/);
  if (!promptMatch) throw new Error('Prompt textbox not found');
  const promptRef = promptMatch[1];
  
  await page.locator(promptRef).click();
  await page.locator(promptRef).fill(promptText);
  console.log('Prompt successfully filled!');
}

async function triggerGenerate(page) {
  const s = await snapshot(page, { interactive: true });
  const genMatch = s.tree.match(/button \"Generate\" \[ref=(e\d+)\]/);
  if (!genMatch) throw new Error('Generate button not ready or currently generating');
  const genRef = genMatch[1];
  
  await page.locator(genRef).click();
  console.log('Generate button successfully clicked! Video rendering started.');
}

module.exports = { checkRunwayStatus, injectPartPrompt, triggerGenerate };
