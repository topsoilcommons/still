// Pacer timing test for Still.
// Runs the same phase math the page uses: the phase is computed from total
// elapsed time, never from chained timers, so drift cannot accumulate.
// Measures when phase changes are observed against the ideal times.
const PHASES = [
  { name: "Breathe in", ms: 4000 },
  { name: "Hold", ms: 4000 },
  { name: "Breathe out", ms: 6000 }
];
const CYCLE = PHASES.reduce((a, p) => a + p.ms, 0); // 14000

function phaseAt(elapsed) {
  let t = elapsed % CYCLE;
  for (let i = 0; i < PHASES.length; i++) {
    if (t < PHASES[i].ms) return i;
    t -= PHASES[i].ms;
  }
  return 0;
}

const CYCLES_TO_RUN = 3;
const totalMs = CYCLE * CYCLES_TO_RUN;
const idealTransitions = [];
for (let c = 0; c < CYCLES_TO_RUN; c++) {
  let acc = c * CYCLE;
  for (const p of PHASES) { acc += p.ms; idealTransitions.push(acc); }
}

const start = Date.now();
let lastPhase = phaseAt(0);
const observed = [];
const timer = setInterval(() => {
  const elapsed = Date.now() - start;
  const ph = phaseAt(elapsed);
  if (ph !== lastPhase) {
    observed.push(elapsed);
    lastPhase = ph;
  }
  if (elapsed >= totalMs + 50) {
    clearInterval(timer);
    const drifts = idealTransitions.map((ideal, i) => ({
      ideal_ms: ideal,
      observed_ms: observed[i] === undefined ? null : observed[i],
      drift_ms: observed[i] === undefined ? null : observed[i] - ideal
    }));
    const abs = drifts.map(d => Math.abs(d.drift_ms)).filter(x => x !== null);
    const result = {
      test: "still pacer phase timing",
      date: new Date().toISOString(),
      cycle_ms: CYCLE,
      cycles_run: CYCLES_TO_RUN,
      transitions_expected: idealTransitions.length,
      transitions_observed: observed.length,
      max_abs_drift_ms: Math.max(...abs),
      mean_abs_drift_ms: Math.round(abs.reduce((a, b) => a + b, 0) / abs.length * 100) / 100,
      drifts
    };
    console.log(JSON.stringify(result, null, 2));
  }
}, 2);
