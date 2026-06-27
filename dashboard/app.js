const { CLICKUP_API_KEY, CLICKUP_TEAM_ID, CLICKUP_LIST_ID, SUPABASE_KEY, SUPABASE_URL } = require('/config')
const { Stages, TaskStatus, ProjectStatus, ClickUpMembers } = require('./constants')

// ─── CONSTANTS (ajuste com seus valores) ──────────────────────────────────── 
const CLICKUP_LIST_IDS = {
    PEDRO: 72844227,
    ISAAC: 111975410,
    VITOR_AGUIAR: 111975411,
    KAUAN: 111975463,
    FELIPE: 118035447,
    VITOR_GUEDSON: 118065770,
}

// ─── INIT ───────────────────────────────────────────────────────────────────
const { createClient } = supabase   // global do CDN
const db = createClient(SUPABASE_URL, SUPABASE_ANON_KEY)

let _modalLeadId = null
let _devmonthData = []

const STAGE_PERCENT = {
    stage_1: { total: 10 },
    stage_2: { total: 25 },
    stage_3_crm: { crm: 50, ia: 0 },
    stage_3_ia: { crm: 0, ia: 50 },
    stage_4: { crm: 75, ia: 75 },
    stage_5: { crm: 100, ia: 100 },
}

// ─── THEME ──────────────────────────────────────────────────────────────────
function toggleTheme() {
    document.body.classList.toggle('light')
    localStorage.setItem('theme', document.body.classList.contains('light') ? 'light' : 'dark')
}
if (localStorage.getItem('theme') === 'light') document.body.classList.add('light')

// ─── TABS ───────────────────────────────────────────────────────────────────
function switchTab(id, btn) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'))
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'))
    document.getElementById('page-' + id).classList.add('active')
    btn.classList.add('active')
}

const tabOrder = ['dash', 'projects', 'devmonth']
let tabIndex = 0
setInterval(() => {
    tabIndex = (tabIndex + 1) % tabOrder.length
    const btn = document.querySelectorAll('.tab')[tabIndex]
    switchTab(tabOrder[tabIndex], btn)
}, 2 * 60 * 1000)

// ─── CLICKUP ────────────────────────────────────────────────────────────────
async function fetchClickUpTasks(listId) {
    const res = await fetch(`https://api.clickup.com/api/v2/list/${listId}/task?include_closed=false`, {
        headers: { Authorization: CLICKUP_TOKEN }
    })
    const data = await res.json()
    return data.tasks || []
}

// ─── ABA 1: DASHBOARD ───────────────────────────────────────────────────────
async function loadDashboard() {
    const { data: leads } = await db.from('leads').select('id, status')
    const ativos = leads?.filter(l => l.status === 'ativo').length ?? 0
    const finalizados = leads?.filter(l => l.status === 'concluido').length ?? 0
    document.getElementById('total-ativos').textContent = ativos
    document.getElementById('total-finalizados').textContent = finalizados

    const stageMap = {
        'stage-ia': CLICKUP_LIST_IDS.ia,
        'stage-suporte': CLICKUP_LIST_IDS.suporte,
        'stage-cs': CLICKUP_LIST_IDS.cs,
        'stage-crm': CLICKUP_LIST_IDS.crm,
        'stage-kauan': CLICKUP_LIST_IDS.reunioesKauan,
        'stage-pedro': CLICKUP_LIST_IDS.reunioesPedro,
    }

    const allTasks = []
    for (const [elId, listId] of Object.entries(stageMap)) {
        const tasks = await fetchClickUpTasks(listId)
        document.getElementById(elId).textContent = tasks.length
        allTasks.push(...tasks)
    }

    // Média de entrega
    const withDue = allTasks
        .filter(t => t.due_date && t.date_done)
        .sort((a, b) => b.date_done - a.date_done)
        .slice(0, 5)

    const days = withDue.map(t =>
        Math.round((parseInt(t.date_done) - parseInt(t.date_created)) / 86400000)
    )
    const avg = days.length ? Math.round(days.reduce((a, b) => a + b, 0) / days.length) : 0
    document.getElementById('avg-delivery').textContent = avg

    // Status Dash
    const now = Date.now()
    const urgentes = allTasks
        .filter(t => t.due_date && parseInt(t.due_date) > now)
        .sort((a, b) => parseInt(a.due_date) - parseInt(b.due_date))
        .slice(0, 6)

    const menorPrazo = urgentes[0] ? parseInt(urgentes[0].due_date) - now : Infinity
    const horas = menorPrazo / 3600000

    let emoji, label, labelClass
    if (horas < 24) { emoji = '🔴'; label = 'Foco Total'; labelClass = 'red' }
    else if (horas < 72) { emoji = '🟡'; label = 'Tranquilo, mas atenção'; labelClass = 'yellow' }
    else { emoji = '🔵'; label = 'Deboas'; labelClass = 'blue' }

    document.getElementById('status-emoji').textContent = emoji
    const lbl = document.getElementById('status-label')
    lbl.textContent = label
    lbl.className = 'status-label ' + labelClass

    const tasksEl = document.getElementById('status-tasks')
    tasksEl.innerHTML = urgentes.length
        ? urgentes.map(t => {
            const dH = Math.round((parseInt(t.due_date) - now) / 3600000)
            const urgClass = dH < 24 ? 'urgent' : ''
            return `<div class="status-task-item">
          <span>${t.name}</span>
          <span class="task-deadline ${urgClass}">${dH}h restantes</span>
        </div>`
        }).join('')
        : '<div style="color:var(--text-muted);font-size:13px">Nenhuma tarefa urgente 🎉</div>'

    document.getElementById('last-update').textContent =
        'Atualizado às ' + new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })
}

// ─── ABA 2: PROJETOS ────────────────────────────────────────────────────────
async function loadProjects() {
    const { data: leads } = await db.from('leads').select('id, company_name, stage, status')
    const grid = document.getElementById('projects-grid')

    if (!leads?.length) {
        grid.innerHTML = '<div style="color:var(--text-muted)">Nenhum projeto encontrado.</div>'
        return
    }

    grid.innerHTML = leads.map(lead => {
        const p = STAGE_PERCENT[lead.stage] ?? { total: 0 }
        const isSplit = p.crm !== undefined

        const bars = isSplit
            ? `<div class="progress-row">
           <div class="progress-label"><span>CRM</span><span>${p.crm}%</span></div>
           <div class="progress-bar"><div class="progress-fill crm" style="width:${p.crm}%"></div></div>
         </div>
         <div class="progress-row" style="margin-top:8px">
           <div class="progress-label"><span>IA</span><span>${p.ia}%</span></div>
           <div class="progress-bar"><div class="progress-fill ia" style="width:${p.ia}%"></div></div>
         </div>`
            : `<div class="progress-row">
           <div class="progress-label"><span>Progresso</span><span>${p.total}%</span></div>
           <div class="progress-bar"><div class="progress-fill" style="width:${p.total}%"></div></div>
         </div>`

        return `<div class="project-card">
      <div class="project-name">${lead.company_name}</div>
      ${bars}
      <button class="project-menu-btn" onclick="openModal('${lead.id}','${lead.company_name}','${lead.status}')">⋯</button>
    </div>`
    }).join('')
}

// ─── MODAL ──────────────────────────────────────────────────────────────────
function openModal(id, name, status) {
    _modalLeadId = id
    document.getElementById('modal-title').textContent = name
    document.getElementById('modal-status').value = status
    document.getElementById('modal-overlay').classList.add('open')
}

function closeModal() {
    document.getElementById('modal-overlay').classList.remove('open')
    _modalLeadId = null
}

async function saveStatus() {
    const status = document.getElementById('modal-status').value
    await db.from('leads').update({ status }).eq('id', _modalLeadId)
    closeModal()
    loadProjects()
}

// ─── ABA 3: DEV DO MÊS ──────────────────────────────────────────────────────
async function loadDevMonth() {
    const res = await fetch('./data/devmonth.json').catch(() => null)
    _devmonthData = res?.ok ? await res.json() : []
    renderRanking()
}

function renderRanking() {
    const mes = new Date().toISOString().slice(0, 7)
    const registros = _devmonthData.filter(r => r.mes === mes)

    const pontos = {}
    registros.forEach(r => {
        if (!pontos[r.dev]) pontos[r.dev] = 0
        pontos[r.dev] += r.tipo === 'positivo' ? 1 : -1
    })

    const ranking = Object.entries(pontos).sort((a, b) => b[1] - a[1])
    const posLabels = ['🥇', '🥈', '🥉']
    const posClass = ['first', 'second', 'third']

    document.getElementById('ranking-list').innerHTML = ranking.length
        ? ranking.slice(0, 3).map(([dev, pts], i) => `
        <div class="rank-card ${posClass[i] ?? ''}">
          <div class="rank-position">${posLabels[i] ?? i + 1}</div>
          ${i === 0 ? `<img class="rank-photo" src="./assets/${dev.toLowerCase()}.jpg" onerror="this.style.display='none'" />` : ''}
          <div class="rank-info">
            <div class="rank-name">${dev}</div>
            <div class="rank-score">${pts > 0 ? '+' : ''}${pts} pontos</div>
          </div>
        </div>`).join('')
        : '<div style="color:var(--text-muted);font-size:13px">Nenhum registro este mês.</div>'
}

function submitFeedback() {
    const dev = document.getElementById('fb-dev').value
    const cliente = document.getElementById('fb-cliente').value.trim()
    const motivo = document.getElementById('fb-motivo').value.trim()
    const tipo = document.querySelector('input[name="fb-tipo"]:checked').value

    if (!dev || !cliente || !motivo) { alert('Preencha todos os campos.'); return }

    const mes = new Date().toISOString().slice(0, 7)
    _devmonthData.push({ mes, dev, cliente, motivo, tipo, ts: Date.now() })

    document.getElementById('fb-dev').value = ''
    document.getElementById('fb-cliente').value = ''
    document.getElementById('fb-motivo').value = ''
    document.querySelector('input[name="fb-tipo"][value="positivo"]').checked = true

    renderRanking()
}

// ─── EXPÕE FUNÇÕES PRO HTML ─────────────────────────────────────────────────
window.toggleTheme = toggleTheme
window.switchTab = switchTab
window.openModal = openModal
window.closeModal = closeModal
window.saveStatus = saveStatus
window.submitFeedback = submitFeedback

// ─── LOAD INICIAL + AUTO-REFRESH 30min ──────────────────────────────────────
async function loadAll() {
    await Promise.all([loadDashboard(), loadProjects(), loadDevMonth()])
}

loadAll()
setInterval(loadAll, 30 * 60 * 1000)