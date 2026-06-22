# PRD — Jornada Matte
**Product Requirements Document**
**Versão:** 2.0
**Autor:** Kauan de Souza Cunha
**Status:** Em produção

---

### Changelog

| Versão | Data | Descrição |
|---|---|---|
| 2.0 | Jun/2026 | Reconstrução em Python (AWS Lambda + Serverless Framework). Etapa 3b desmembrada em 3b → 3c → 3d. Plano de Ação movido para etapa final (4b). Banco de dados migrado para Supabase/PostgreSQL. |
| 1.0 | — | Versão original em N8N (descontinuada). |

---

## Índice

1. [Visão Geral do Produto](#1-visão-geral-do-produto)
2. [Contexto e Problema](#2-contexto-e-problema)
3. [Objetivos e Métricas de Sucesso](#3-objetivos-e-métricas-de-sucesso)
4. [Arquitetura do Projeto](#4-arquitetura-do-projeto)
5. [Etapas do Fluxo de Automação](#5-etapas-do-fluxo-de-automação)
6. [Dashboard](#6-dashboard)
7. [Funcionalidades Transversais](#7-funcionalidades-transversais)
8. [Backlog e Priorização](#8-backlog-e-priorização)
9. [Restrições](#9-restrições)
10. [Glossário](#10-glossário)
11. [Checklist de Implementação por Etapa](#11-checklist-de-implementação-por-etapa)

---

## 1. Visão Geral do Produto

**Nome do Projeto:** Jornada Matte

**Descrição:** Sistema de automação pós-venda da Matte Tecnologia, responsável por orquestrar e padronizar toda a jornada de onboarding de novos clientes — desde a passagem de bastão do time de vendas até a primeira entrega da IA e o acompanhamento de 30 dias posterior. O sistema é acionado por um webhook e opera criando, verificando e encadeando tarefas no ClickUp, com um Dashboard de acompanhamento em tempo real exibido em TV interna.

**Tecnologia principal:** Python (AWS Lambda + Serverless Framework v3)

**Integrações externas:**
- ClickUp API (criação e gestão de tarefas)
- Supabase / PostgreSQL (persistência de estado dos projetos)
- WhatsApp (comunicação com clientes — mensagens automáticas)
- GoHighLevel / CRM Matte (configuração e personalização)
- Meta Ads (cadastro e dashboard de leads)

---

## 2. Contexto e Problema

O atendimento pós-venda da Matte apresentava gargalos recorrentes: falta de padronização nas etapas de onboarding, ausência de identificação clara do cliente em tarefas, e desgaste com clientes causado por falta de acompanhamento estruturado.

Uma versão anterior foi construída em N8N. Esta é a versão 2.0, reconstruída em Python, com as seguintes melhorias:
- Adição de novas etapas e tarefas identificadas como necessárias
- Dashboard visual de acompanhamento em tempo real (inexistente na v1.0)
- Maior controle sobre erros, cancelamentos e reinicializações de projetos
- Código mais manutenível e testável

---

## 3. Objetivos e Métricas de Sucesso

| Objetivo | Métrica |
|---|---|
| Padronizar o onboarding de novos clientes | 100% dos novos clientes passam pelo fluxo automatizado |
| Reduzir desgaste e reclamações no pós-venda | Redução de feedbacks negativos no período de onboarding |
| Dar visibilidade à equipe sobre o andamento dos projetos | Dashboard ativo e exibido na TV durante o horário comercial |
| Dividir responsabilidades de forma clara | Nenhuma tarefa sem proprietário definido no ClickUp |
| Rastrear tempo médio de entrega | Tempo médio calculado entre "Boas-Vindas" e "Primeira Entrega da IA" |

---

## 4. Arquitetura do Projeto

### Fluxo de alto nível

```
Webhook (Formulário de Passagem de Bastão)
        |
        v
[Etapa 1] Abertura do Projeto → Tarefas iniciais no ClickUp
        |
        v (verificação a cada 30 min via EventBridge)
[Etapa 2] Pós-Onboarding → Tarefas de próximos passos
        |
        v (verificação)
[Etapa 3] Bifurcação em paralelo:
        |
        |--- [3a] Personalização do CRM (CS/Gestor)
        |         |
        |         v (verificação)
        |    [4a] Onboarding do CRM
        |
        |--- [3b] Criação da IA (Dev)
                  |
                  v (verificação)
             [3c] Revisão da IA (Dev diferente)
                  |
                  v (verificação)
             [3d] Entrega da IA ao Cliente (CS)
                  |
                  v (verificação)
             [4b] Plano de Ação de 90 Dias
                  |
                  v
        [Etapa Final] Acompanhamento 30 dias pós-entrega
```

### Modelo de dados principal

Cada projeto (cliente) tem os seguintes atributos rastreados no Supabase:

- `id` — identificador único (UUID)
- `client_name` — nome do cliente
- `company_name` — nome da empresa
- `service_description` — descrição breve do produto/serviço
- `current_stage` — etapa atual do projeto
- `task_id` — ID da tarefa ativa no ClickUp (branch principal)
- `task_id_b` — ID da tarefa ativa no ClickUp (branch secundário, usado na bifurcação 3a/3b)
- `status` — ativo | pausado | cancelado | concluído
- `started_at` — data/hora de início da etapa atual
- `created_at` — data/hora de criação do projeto

> **Nota sobre a bifurcação:** Quando a Etapa 2 é concluída, o sistema insere uma segunda linha no banco para o branch 3b, mantendo o mesmo `company_name`. As duas branches são rastreadas independentemente até convergirem na Etapa Final.

---

## 5. Etapas do Fluxo de Automação

> **Convenção:** Cada etapa possui um módulo Python dedicado (`stage_X.py`) e uma função de verificação (`stage_X_check.py`) que detecta a conclusão da tarefa no ClickUp e dispara a criação da próxima etapa.

---

### Etapa 1 — Abertura do Projeto

**Gatilho:** Recebimento do webhook com dados do cliente (nome, empresa, descrição do produto/serviço).

**Responsabilidade:** Sistema (automação)

**Tarefa criada no ClickUp:** `Primeiro Passo de - [empresa]`

**Sub-tarefas:**
- Boas-Vindas
- Apresentação da Equipe
- Feedback da Reunião de Vendas
- Marcar Onboarding com Cliente

---

### Etapa 2 — Pós-Onboarding

**Gatilho:** Conclusão verificada da Etapa 1.

**Responsabilidade:** CS / Gestor

**Tarefa criada no ClickUp:** `Pós-Onboarding de - [empresa]`

**Sub-tarefas:**
- Enviar instruções ao Cliente (criação de conta no CRM)
- Feedback do Onboarding de Apresentação

---

### Etapa 3 — Bifurcação: 3a (CRM) e 3b (IA)

As etapas 3a e 3b são iniciadas **simultaneamente** após a verificação da Etapa 2.

---

#### Etapa 3a — Personalização do CRM

**Responsabilidade:** CS / Gestor de Projetos

**Tarefa criada no ClickUp:** `Personalização do CRM - [empresa]`

**Sub-tarefas:**
- Cadastro de Leads, Calendários e Horários
- Captação e Integração de Leads
- Automações
- Comunicação e Canais

---

#### Etapa 3b — Criação da IA

**Responsabilidade:** Dev (sem proprietário fixo — definido conforme disponibilidade)

**Tarefa criada no ClickUp:** `Criação da IA - [empresa]`

---

#### Etapa 3c — Revisão da IA

**Gatilho:** Conclusão verificada da Etapa 3b.

**Responsabilidade:** Dev diferente do que criou a IA (sorteio automático excluindo o autor da 3b)

**Tarefa criada no ClickUp:** `Revisão da IA - [empresa]`

**Itens a verificar:**
- Prompt conciso e coerente
- Fluxos de trabalho sendo acionados
- Campos Personalizados sendo preenchidos
- IA respondendo sem alucinações
- IA realizando agendamento ou repassando ao consultor

---

#### Etapa 3d — Entrega da IA

**Gatilho:** Conclusão verificada da Etapa 3c.

**Responsabilidade:** CS

**Tarefa criada no ClickUp:** `Realizar entrega da IA - [empresa]`

---

### Etapa 4a — Onboarding do CRM

**Gatilho:** Conclusão verificada da Etapa 3a.

**Responsabilidade:** CS / Gestor

**Tarefa criada no ClickUp:** `Onboarding do CRM - [empresa]`

**Sub-tarefas:**
- Marcar Onboarding do CRM
- Feedback do Onboarding do CRM
- Pedir Indicação (condicional — apenas se feedback positivo)

---

### Etapa 4b — Plano de Ação de 90 Dias

**Gatilho:** Conclusão verificada da Etapa 3d.

**Responsabilidade:** CS / Gestor + Founder da Matte

**Tarefa criada no ClickUp:** `Plano de Ação de 90 Dias - [empresa]`

**Sub-tarefas:**
- Marcar Reunião de Plano de Ação de 90 Dias
- Feedback Pós-Reunião de 90 Dias

---

### Etapa Final — Acompanhamento de 30 Dias

**Gatilho:** Conclusão verificada da Etapa 4b.

**Responsabilidade:** CS / Gestor

**Tarefa criada no ClickUp:** `Acompanhamento Após 30 dias - [empresa]`

**Itens:**
- Verificar andamento e funcionamento do projeto
- Confirmar satisfação do cliente
- Coletar feedback
- Se positivo: solicitar indicação

---

## 6. Dashboard

O Dashboard é uma interface web exibida em TV interna (tela full-screen), alternando automaticamente entre 3 painéis a cada 30 segundos.

### Painel 1 — Visão Geral de Projetos

| Elemento | Fonte dos dados |
|---|---|
| Total de tarefas ativas | ClickUp API |
| Total de projetos em andamento | Supabase |
| Gráfico de barras: tarefas por desenvolvedor | ClickUp API |
| Tempo médio entre Boas-Vindas e Primeira Entrega da IA | Supabase |

### Painel 2 — Performance da Equipe (Desenvolvedor do Mês)

| Elemento | Fonte dos dados |
|---|---|
| Foto, nome e cargo do Desenvolvedor do Mês | Cadastro interno |
| Quantidade de elogios e reclamações do mês | Supabase |
| Ranking com pontuação de avaliações (0 a 10) | Supabase |

### Painel 3 — Progresso por Projeto

| Elemento | Fonte dos dados |
|---|---|
| Gráfico de progresso por empresa (% de etapas concluídas) | Supabase |

### Aba Lateral — Gestão de Projetos

- Lista de todos os projetos em andamento com status
- Opção de pausar, cancelar ou reiniciar um projeto a partir de uma etapa específica

### Aba de Reclamações e Elogios

- Registro manual por projeto/desenvolvedor
- Listagem com data, responsável e descrição

### Notificações de Erro

- Alerta visual na tela quando um erro ocorrer no sistema
- Som de notificação no navegador
- Registro no banco com timestamp e contexto

---

## 7. Funcionalidades Transversais

### Regra de Indicação
- Só solicitar quando o cliente expressar satisfação positiva
- Nunca solicitar em dois momentos muito próximos (mesma semana ou semanas consecutivas)

### Regra de Feedback
- Sempre solicitado após entregas ou reuniões, nunca de forma genérica

### Regra de Atribuição de Tarefas
- Por padrão, cada tarefa tem um proprietário fixo definido no código
- Sorteio automático disponível apenas para tarefas específicas (ex: revisão da IA em 3c)
- Quando sorteio é usado, o resultado é persistido no banco

### Notificação de Erros
- Todo erro deve ser registrado no banco com timestamp, etapa, projeto e mensagem
- Exibir alerta no Dashboard e enviar notificação por e-mail ao responsável técnico

### Cancelamento e Reinicialização
- Pausar: congela o estado atual
- Cancelar: marca como cancelado, para execução
- Reiniciar: retoma a partir de uma etapa específica sem perda de dados anteriores

### Due Dates
- Calculados em dias úteis (sábados e domingos ignorados automaticamente)

---

## 8. Backlog e Priorização

| Item | Prioridade | Status |
|---|---|---|
| Webhook de entrada | Alta | ✅ Concluído |
| Etapas 1 a 4b + Final | Alta | ✅ Concluído |
| Polling via EventBridge (10 min) | Alta | ✅ Concluído |
| Persistência no Supabase | Alta | ✅ Concluído |
| Dashboard — Painel 1 | Média | 🔲 Pendente |
| Dashboard — Painel 2 | Média | 🔲 Pendente |
| Dashboard — Painel 3 | Média | 🔲 Pendente |
| Aba de gestão de projetos | Média | 🔲 Pendente |
| Notificação de erros por e-mail | Baixa | 🔲 Pendente |
| Testes automatizados por etapa | Baixa | 🔲 Pendente |

---

## 9. Restrições

- O sistema deve operar sem intervenção manual para projetos no fluxo padrão
- Credenciais (API Keys, URLs) devem estar em variáveis de ambiente, nunca no código
- O Dashboard deve funcionar offline em relação ao Lambda (leitura direta do Supabase e ClickUp)
- Tarefas criadas no ClickUp não devem ser deletadas pelo sistema — apenas criadas e monitoradas

---

## 10. Glossário

| Termo | Definição |
|---|---|
| Passagem de Bastão | Formulário preenchido pelo time de vendas ao fechar um novo cliente, que dispara o webhook |
| Etapa | Conjunto de tarefas no ClickUp que representa uma fase da jornada do cliente |
| Verificação | Processo automatizado (polling) que detecta a conclusão de uma etapa e inicia a próxima |
| Branch | Linha paralela de execução — as branches 3a (CRM) e 3b→3d (IA) correm simultaneamente |
| Polling | Verificação periódica via EventBridge a cada 30 minutos em produção |
| CS | Customer Success — responsável pelo relacionamento e acompanhamento do cliente |

---

## 11. Checklist de Implementação por Etapa

| Etapa | Criar tarefa | Verificar conclusão | Avançar para próxima |
|---|---|---|---|
| Etapa 1 | ✅ | ✅ | ✅ |
| Etapa 2 | ✅ | ✅ | ✅ |
| Etapa 3a | ✅ | ✅ | ✅ |
| Etapa 3b | ✅ | ✅ | ✅ |
| Etapa 3c | ✅ | ✅ | ✅ |
| Etapa 3d | ✅ | ✅ | ✅ |
| Etapa 4a | ✅ | ✅ | ✅ |
| Etapa 4b | ✅ | ✅ | ✅ |
| Etapa Final | ✅ | ✅ | ✅ |