const INTERVAL = 30000;
const pages = document.querySelectorAll('.page');
const dots = document.querySelectorAll('.dot');
const bar = document.getElementById('progress-bar');
let current = 0;
let startTime = null;

function goTo(idx) {
    pages[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = idx;
    pages[current].classList.add('active');
    dots[current].classList.add('active');
    startTime = performance.now();
}

dots.forEach(d => d.addEventListener('click', () => goTo(+d.dataset.idx)));

function tick(ts) {
    if (!startTime) startTime = ts;
    const elapsed = ts - startTime;
    bar.style.width = Math.min((elapsed / INTERVAL) * 100, 100) + '%';
    if (elapsed >= INTERVAL) goTo((current + 1) % pages.length);
    requestAnimationFrame(tick);
}

function updateClock() {
    const now = new Date();
    const t = String(now.getHours()).padStart(2, '0') + ':' + String(now.getMinutes()).padStart(2, '0');
    document.querySelectorAll('#clock, #clock3').forEach(el => el && (el.textContent = t));
}

updateClock();
setInterval(updateClock, 10000);
startTime = performance.now();
requestAnimationFrame(tick);
