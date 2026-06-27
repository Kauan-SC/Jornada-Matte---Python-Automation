# Checklist — Matte Dashboard

## Setup Inicial
- [X] Criar estrutura de pastas
---

## Aba 1 — Dashboard Principal
- [ ] Renderizar os 2 cards de projetos (ativos / finalizados)
- [ ] Conectar ClickUp e buscar tarefas por stage (usar getTasks já mapeado)
- [ ] Renderizar os 6 cards de stage com contagem
- [ ] Implementar gráfico de colunas (Chart.js) com últimos 5 projetos entregues + média
- [ ] Renderizar card de média geral de tempo de projeto
- [ ] Implementar lógica de status (contagem de urgentes por prazo)
- [ ] Renderizar Status Dash full-width com emoji e lista de urgentes

---

## Aba 2 — Progresso dos Projetos
- [ ] Buscar todos os leads do Supabase (`company_name` + `stage`)
- [ ] Renderizar cards com porcentagem simples (stage 1 e 2)
- [ ] Implementar bifurcação de porcentagem CRM/IA (stage 3+)
- [ ] Criar menu de 3 pontinhos por card
- [ ] Criar modal de edição de status
- [ ] Implementar PATCH no Supabase ao salvar status alterado

---

## Aba 3 — Dev do Mês
- [ ] Criar estrutura do `devmonth.json` (array de registros mensais)
- [ ] Renderizar ranking com lógica de pontuação
- [ ] Adicionar espaço para foto do 1º lugar
- [ ] Criar formulário de registro de feedback (dev, cliente, motivo, tipo)
- [ ] Salvar novo registro no `devmonth.json`
- [ ] Criar GitHub Action para push automático do JSON

---

## Global
- [ ] Implementar toggle Dark/White com persistência em localStorage
- [ ] Implementar `setInterval` de 30 min para refresh geral
- [ ] Implementar rotação automática de abas a cada 2 min
- [ ] Testar em tela 1080p+
- [ ] Garantir que todas as chamadas de API tratam erro (catch + mensagem visual)