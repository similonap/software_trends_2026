// Callback voor <Profiler onRender={meet}>. React roept die op na elke commit
// waarin de Profiler meedeed. "duur" is de tijd die het renderen van alles
// binnen de Profiler kostte; 0 ms betekent dat React die deelboom oversloeg.
// We schrijven het resultaat rechtstreeks in de DOM (buiten React),
// anders zou het meten zelf renders veroorzaken.
let aantal = 0

export function meet(id, fase, duur) {
  aantal += 1
  const regel =
    duur < 0.05
      ? `#${aantal} ${id}: overgeslagen (0 ms)`
      : `#${aantal} ${id} rendert (${fase}): ${duur.toFixed(1)} ms`
  console.log('[meting]', regel)
  const paneel = document.getElementById('meting')
  if (paneel) paneel.textContent = regel
}
