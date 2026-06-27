# PRD — Matte Dashboard

## Visão Geral
Dashboard interno da Matte para gestão operacional. Integra dados do **ClickUp** (tarefas) e **Supabase** (leads/projetos). Roda no browser, HTML/CSS/JS puro, sem framework. Auto-atualiza a cada 30 minutos e rotaciona entre abas a cada 2 minutos.

## Tecnologia
- HTML + CSS + JS vanilla
- Supabase JS SDK (CDN)
- ClickUp REST API (já mapeada no projeto Python)
- Chart.js (CDN) — gráfico de colunas
- GitHub — versionamento do `devmonth.json`

---

## Aba 1 — Dashboard Principal

| Componente | Fonte | Descrição |
|---|---|---|
| Projetos Ativos | Supabase | Retângulo com total de projetos com status ativo |
| Projetos Finalizados | Supabase + manual | Retângulo com total acumulado |
| Tarefas por Estágio | ClickUp | 6 cards side-by-side com contagem por lista/stage |
| Gráfico IA | ClickUp | Colunas com tempo de entrega dos últimos 5 projetos + média geral |
| Média Total do Projeto | ClickUp | Card único com número em destaque |
| Status Dash | ClickUp | Retângulo full-width, tarefas urgentes + emoji de status |

**Stages do ClickUp:**
- IAs para Criar/Revisar
- Tarefas de Suporte
- Tarefas do CS
- Personalizar CRM
- Reuniões Kauan
- Reuniões Pedro

**Lógica do Status Dash:**
```
tarefas com prazo < 24h  →  🔴 Foco Total
tarefas com prazo < 72h  →  🟡 Tranquilo, mas atenção
demais                   →  🔵 Deboas
```

---

## Aba 2 — Progresso dos Projetos

- Puxa todos os leads do Supabase via `company_name` + `stage`
- Exibe cards compactos: nome do cliente + barra(s) de porcentagem
- **Stages 1 e 2:** porcentagem única linear
- **Stage 3+:** bifurca em % CRM e % IA separadas
- Menu de 3 pontinhos por card → modal para alterar status do lead
- Status disponíveis: Ativo / Desativado / Concluído / Pausado
- Alteração salva direto no Supabase via PATCH

**Mapeamento de porcentagem por stage:**
```
stage_1      →  10%
stage_2      →  25%
stage_3_crm  →  50% CRM / 0% IA
stage_3_ia   →  0% CRM / 50% IA
stage_4      →  75% cada
stage_5      →  100% cada
```
*(ajustar conforme os stages reais do Supabase)*

---

## Aba 3 — Dev do Mês

- Ranking mensal: 1º (foto + nome), 2º e 3º (só nome)
- Formulário interno para o CS registrar: dev, empresa/cliente, motivo, tipo (positivo/negativo)
- Dados persistidos em `data/devmonth.json`
- GitHub Action faz push automático do JSON ao detectar mudança
- Pontuação: +1 positivo / -1 negativo → ordena ranking

---

## Comportamento Global

| Feature | Detalhe |
|---|---|
| Tema | Toggle Dark/White — salvo em localStorage |
| Auto-refresh | Chama todas as APIs a cada 30 min via `setInterval` |
| Rotação de abas | Troca de aba a cada 2 min automaticamente |
| Indicador visual | Ícone/emoji no header indicando o tema atual |