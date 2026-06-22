## 1. Checklist de Implementação por Etapa

> Use este checklist para acompanhar o progresso da construção. Marque `[x]` ao concluir cada item.

### Fundação (antes de começar as etapas)
- [x] Criar estrutura de pastas do projeto — 13/06
- [x] Configurar `.env` e `.env.example` com as variáveis necessárias — 13/06
- [x] Configurar `config.py` (leitura das variáveis de ambiente) — 13/06
- [x] Configurar `constants.py` (nomes de etapas, status, etc.) — 13/06
- [x] Configurar sistema de logging (`core/logger.py`) — 13/06
- [x] Configurar banco de dados e modelo de projeto (`core/database.py`) — 13/06
- [x] Criar `integrations/clickup.py` (funções base de criar tarefa, criar sub-tarefa, verificar conclusão) — 14/06
- [x] Criar `handler.py` com recebimento do webhook e parsing dos dados do cliente — 14/06

### Etapa 1 — Abertura do Projeto
- [x] Criar `stages/stage_1.py` — 14/06
- [x] Criar a tarefa única no ClickUp com nome do cliente no título — 14/06
- [x] Adicionar as 4 sub-tarefas (Boas-Vindas, Apresentação da Equipe, Feedback Vendas, Marcar Onboarding) — 14/06
- [x] Criar `stages/stage_1_check.py` (verifica se a tarefa foi concluída) — 14/06
- [x] Encadear: ao concluir, disparar a Etapa 2 — 14/06

### Etapa 2 — Pós-Onboarding
- [x] Criar `stages/stage_2.py` — 20/06
- [x] Criar a tarefa única com as 2 sub-tarefas (Próximos Passos, Feedback Onboarding) — 20/06
- [x] Criar `stages/stage_2_check.py` — 20/06
- [x] Encadear: ao concluir, disparar as Etapas 3a e 3b simultaneamente — 20/06

### Etapa 3a — Personalização do CRM
- [x] Criar `stages/stage_3a.py` — 20/06
- [x] Criar a tarefa única com todas as sub-tarefas do checklist do CRM — 20/06
- [x] Criar `stages/stage_3a_check.py` — 20/06
- [x] Encadear: ao concluir, disparar a Etapa 4a — 20/06

### Etapa 3b — Criação da IA
- [x] Criar `stages/stage_3b.py` — 20/06
- [x] Criar tarefa "Criação da IA" no ClickUp — 20/06
- [x] Criar `stages/stage_3b_check.py` — 20/06
- [x] Encadear: ao concluir, disparar a Etapa 3c — 20/06

### Etapa 3c — Revisão da IA
- [x] Criar `stages/stage_3c.py` — 20/06
- [x] Sorteio automático de dev revisor (diferente do autor da 3b) — 20/06
- [x] Criar `stages/stage_3c_check.py` — 20/06
- [x] Encadear: ao concluir, disparar a Etapa 3d — 20/06

### Etapa 3d — Entrega da IA
- [x] Criar `stages/stage_3d.py` — 20/06
- [x] Criar tarefa de entrega ao cliente (CS) — 20/06
- [x] Criar `stages/stage_3d_check.py` — 20/06
- [x] Encadear: ao concluir, disparar a Etapa 4b — 20/06

### Etapa 4a — Onboarding do CRM
- [x] Criar `stages/stage_4a.py` — 20/06
- [x] Criar a tarefa única com as sub-tarefas (Marcar Onboarding, Feedback, Indicação condicional) — 20/06

### Etapa 4b — Plano de Ação de 90 Dias
- [x] Criar `stages/stage_4b.py` — 20/06
- [x] Criar a tarefa única com as 2 sub-tarefas (Marcar Reunião, Feedback Pós-Reunião) — 20/06

### Etapa Final — Acompanhamento de 30 Dias
- [x] Criar `stages/stage_final.py` — 20/06
- [x] Criar a tarefa única com as sub-tarefas de acompanhamento — 20/06

### Funcionalidades Transversais
- [x] Atribuição de proprietário (fixo por padrão; sorteio automático na 3c) — 20/06
- [x] Notificação de erros (`core/notifier.py`) — 20/06
- [x] Due dates em dias úteis (sábados e domingos ignorados) — 21/06
- [ ] Regra de proximidade entre pedidos de indicação
- [ ] Cancelamento e pausa de projetos
- [ ] Reinicialização de projeto a partir de etapa específica

### Dashboard
- [ ] Servidor web base (`dashboard/app.py`)
- [ ] Painel 1 — Visão Geral
- [ ] Painel 2 — Performance da Equipe (Desenvolvedor do Mês)
- [ ] Painel 3 — Progresso por Projeto
- [ ] Rotação automática de painéis (30 segundos)
- [ ] Aba lateral — Gestão de Projetos (cancelar/pausar/reiniciar)
- [ ] Aba de Reclamações e Elogios
- [ ] Notificação visual e sonora de erros na tela

### Testes
- [ ] Testes das funções de verificação de cada etapa
- [ ] Testes das funções auxiliares (`core/helpers.py`)
- [ ] Testes da integração com o ClickUp

---

## 2. Backlog e Priorização

### MVP (Versão 1 — Funcional)
- [x] Recebimento do webhook e parsing dos dados do cliente
- [x] Criação das tarefas no ClickUp com identificação do cliente no título
- [x] Sistema de verificação de conclusão de etapa (polling via EventBridge)
- [x] Encadeamento 1 → 2 → 3 (bifurcação 3a/3b→3c→3d) → 4 → Final
- [x] Logging estruturado
- [x] Persistência de estado no Supabase
- [x] Variáveis de ambiente para credenciais

### V1.1 — Robustez
- [ ] Notificação de erro por e-mail
- [ ] Cancelamento e pausa de projetos via dashboard
- [ ] Reinicialização de projeto a partir de etapa específica
- [ ] Regra de proximidade entre pedidos de indicação

### V1.2 — Dashboard
- [ ] Painel 1: Visão Geral
- [ ] Painel 2: Performance da Equipe
- [ ] Painel 3: Progresso por Projeto
- [ ] Rotação automática de painéis (30 segundos)
- [ ] Notificação visual e sonora de erros no dashboard
- [ ] Aba de reclamações e elogios

### V2.0 — Melhorias futuras
- [ ] Integração automática de funcionários em grupos WhatsApp do cliente
- [ ] Relatório mensal automático de feedbacks
- [ ] Expansão do checklist de automações do CRM
- [ ] Suporte a múltiplos workspaces no ClickUp

---

## 3. Glossário

| Termo | Definição |
|---|---|
| CS | Customer Success — profissional responsável pelo sucesso do cliente |
| Gestor | Gestor de Projetos da Matte |
| Dev | Desenvolvedor — time técnico responsável pela criação da IA |
| ClickUp | Ferramenta de gestão de tarefas usada pela equipe Matte |
| GHL | GoHighLevel — CRM principal da Matte e dos clientes |
| Briefing da IA | Documento enviado pelo cliente com informações para criação do agente de IA |
| Pipeline | Funil de vendas configurado no CRM do cliente |
| Webhook | Notificação HTTP disparada automaticamente por um evento |
| Jornada | Nome dado ao fluxo completo de onboarding de um cliente da Matte |
| PRD | Product Requirements Document — documento que define os requisitos e o escopo do produto |

---

## 4. Restrições

- **Nenhum código deve ser gerado por terceiros ou IAs externas sem revisão do autor.**
- **Não criar código neste PRD.** Este documento é exclusivamente de planejamento.
- O sistema deve funcionar de forma independente da disponibilidade manual da equipe.
- Credenciais de API não devem aparecer em nenhum arquivo versionado no repositório.