# Jornada Matte

## Objetivo Principal

O objetivo principal da Jornada Matte é, através de automações, melhorar e padronizar o atendimento pós-venda da Matte — um gargalo que apresentou problemas e desgaste com clientes anteriormente.

Por meio de automações no ClickUp (App de Atividades da Equipe), a automação irá criar um acompanhamento do projeto que dura em torno de 20 dias úteis (1 mês).

---

## Envio do Projeto do Cliente

A passagem de bastão entre o time de Vendas e o time de Desenvolvimento já está pronta. Um formulário simples detalha o Nome do(s) Cliente(s), Nome da Empresa e Descrição breve sobre o produto/serviço trabalhado pelo cliente.

Esse site simples envia um Webhook para um fluxo que dá início em todo o projeto.

---

# Etapa 1 — Webhook Enviado

Com o Webhook enviado com os dados do cliente, serão criadas automaticamente as seguintes atividades:

### Boas-Vindas
Adição de todos os funcionários no grupo do cliente e boas-vindas ao cliente.
> Nota: automatizar a identificação do grupo seria muito complexo para o tempo que economizaria — considerado inútil por ora.

### Apresentação da Equipe da Matte
Mensagem padrão apresentando todos os funcionários e suas funções.

### Pedir Feedback sobre a Reunião de Vendas
Atividade para mandar mensagem no privado ao cliente que acabou de contratar, pedindo Feedback sobre a reunião de vendas. Objetivo: capturar bons Feedbacks ou identificar gargalos no processo comercial.

### Marcar Onboarding com o Cliente
Enviar mensagem ao cliente sobre a reunião de apresentação e início do projeto.

---

### ✅ Verificação da Etapa 1
Só avança para o próximo passo após todas as tarefas (ou a última) estarem concluídas.

---

# Etapa 2 — Pós-Onboarding

### Pós-Onboarding
Etapa para enviar os detalhes sobre os próximos passos e o que o cliente precisa realizar para que o time da Matte possa dar start no projeto:

- [ ] Criar a conta no CRM Matte
- [ ] Enviar o Briefing da IA

### Feedback sobre o Onboarding de Apresentação
Atividade para o CS/Gestor de Projetos enviar mensagem no privado do(s) cliente(s) para coletar Feedback sobre a reunião de Onboarding. O responsável pelo envio deve ser sempre o oposto de quem conduziu a reunião (se o CS fez, o Gestor manda, e vice-versa).

---

### ✅ Verificação da Etapa 2
Etapa para cobrar o cliente de suas responsabilidades. O próximo passo só é dado após a conclusão das duas tarefas.

---

# Etapa 3 — Bifurcação: 3a + 3b

## 3a: Personalização do CRM

Nessa etapa ocorre a bifurcação entre o time de CS/Gestor de Projetos e o time de Desenvolvimento. O objetivo é manter o time de Desenvolvimento focado na criação da IA e ajustes, enquanto CS/Gestor atuam como suporte e desenvolvedores de automações simples (conexões básicas, templates de mensagens, etc.). Fluxos mais complexos são repassados ao time de Desenvolvimento.

### Checklist de Personalizações do CRM

**Comunicação e Canais**
- [ ] Cadastro do WhatsApp Business
- [ ] Cadastro do WhatsApp API Oficial
- [ ] Cadastro de e-mail marketing
- [ ] Conectar Ligação por WhatsApp Business

**Captação e Integração de Leads**
- [ ] Cadastro da Meta Ads (Facebook/Instagram)
- [ ] Criação de dashboard de leads da META
- [ ] Criação ou integração de formulários/sites

**Cadastro de Leads, Calendários e Horários**
- [ ] Importação, tagueamento e personalização de Leads
- [ ] Importação, tagueamento e personalização de Pipeline
- [ ] Cadastro e ajuste de calendário por funcionário
- [ ] Ajuste de disponibilidade

**Automações**
- [ ] Divisão de Contatos
- [ ] Criar automação de respostas para posts no Instagram/Facebook/TikTok
- [ ] *(Pensar em mais automações...)*

---

### ✅ Verificação da Etapa 3a
Verifica se a Etapa 3a foi concluída e finalizada.

---

## 3b: Criação da IA

Etapa destinada ao time especializado de criação de IA, responsável pela criação da IA, Pipelines, automações e fluxos de trabalho. O CS/Gestor de Projetos atua como verificador, pois como cada IA é diferente, é impossível traçar um padrão único para todas.

### Criar IA
Tarefa de criação da IA com o nome do cliente para fácil identificação.
> ⚠️ A identificação do nome do cliente é imprescindível — a ausência disso gerou atrasos anteriormente.

Sub-tarefas:
- [ ] IA deve mover as Pipelines (se o cliente não repassar Pipelines específicas, criar novas de acordo com a IA)
- [ ] IA deve preencher os Campos Personalizados com informações do cliente
- [ ] Automações/Fluxos de Trabalho devem estar funcionando
- [ ] Agendamento: se necessário, agendar / se necessário repassar, notificar o consultor

---

### ✅ Verificar Conclusão da Criação da IA
Verifica se a atividade "Criar IA" foi concluída.

---

### Aprovação da IA
Um segundo desenvolvedor realiza os testes e aprova a IA criada, evitando erros e reclamações futuras.

Sub-tarefas:
- [ ] Testar IA
- [ ] Verificar se IA está movendo as Pipelines
- [ ] Verificar se todos os Fluxos de Trabalho e Campos Personalizados estão sendo ativados/capturados
- [ ] Verificar se IA está agendando ou repassando para o consultor

---

### ✅ Verificar Conclusão da Aprovação da IA
Verifica se a atividade "Aprovação da IA" foi concluída.

---

### Primeira Entrega da IA
Atividade focada em entregar a IA ao cliente.

- [ ] Conectar IA
- [ ] Criar resumo sobre o projeto e enviar no grupo
- [ ] Realizar entrega e agendar reunião pós-entrega para pontuações e coleta de Feedback
- [ ] Se o cliente estiver satisfeito, pedir indicação e Feedback

> *(Após isso, não é possível prever os próximos passos, pois a IA pode demandar diversas outras atualizações.)*

---

# Etapa 4a — Onboarding do CRM

Após a conclusão da Etapa 3a, o próximo passo é marcar a reunião de Onboarding do CRM — uma reunião com todo o time da empresa para apresentar todas as abas e funcionalidades do sistema da Matte.

- [ ] Marcar reunião de Onboarding do CRM
- [ ] Coletar Feedback pós-reunião e sobre a personalização do sistema (verificar se desejam ajustes)
- [ ] Pedir indicação conforme Feedback do cliente

---

# Etapa 4b — Plano de Ação de 90 Dias

Essa etapa só ocorre após a Primeira Entrega. É necessária uma verificação para isso.

Após a primeira entrega, marcar uma reunião com o Founder da Matte com o objetivo de escalar o projeto com IA.

### Pós-Reunião do Plano de Ação de 90 Dias
- [ ] Coletar Feedback e indicação do cliente

---

# Acompanhamento Final

Após 30 dias da primeira entrega da IA, verificar como está o projeto do cliente: se ele gostou, se está rodando bem, coletar indicação e Feedback.

Objetivo: em 30 dias após a primeira entrega, o projeto já deve estar rodando e funcionando para o cliente.

---

# Observações

### Feedback
Pedir Feedback nunca é demais — demonstra atenção e cuidado com o cliente. Porém, deve ser feito nos momentos certos: após entregas ou reuniões realizadas pela equipe da Matte. Isso torna mais difícil a ocorrência de reclamações soltas.

### Indicação
Assim como o Feedback, a indicação deve ser pedida somente quando o cliente se manifestar de forma positiva sobre o acompanhamento. Evitar pedir indicação em entregas muito próximas entre si (ex.: reunião de primeira entrega e Plano de Ação de 90 dias na mesma semana) — pode ser percebido como chato pelo cliente.

### Divisão de Tarefas entre CS e Gestor de Projetos
Seria interessante, em algumas tarefas, aplicar uma lógica de 50/50 para definir aleatoriamente o proprietário da tarefa entre CS e Gestor. Um simples `random` em Python já resolveria isso.

### Notificação de Erro
Ainda sem definição de implementação, mas criar uma etapa onde qualquer erro no sistema dispare uma notificação (e-mail e Dashboard) parece algo viável e não muito complexo.

### Cancelamento de Projeto
No Dashboard, incluir a opção de visualizar todos os projetos em andamento e poder cancelar ou pausar qualquer um a qualquer momento. Idealmente, também ser possível reiniciar um projeto a partir de uma etapa específica, sem precisar recomeçar do zero.

> O objetivo de "Cancelamento" e "Notificação de Erro" é facilitar a identificação de onde e por que ocorreu um erro, tornando a correção mais rápida. São detalhes mais complexos que podem aguardar.

---

# Dashboard

Talvez a etapa mais complexa do projeto. Uma versão anterior já foi feita em menor escala no N8N, então a familiaridade com APIs e criação de etapas já existe. A transição para Python deve ser tranquila.

A principal diferença desta versão é a criação de um Dashboard visual em Front-end para acompanhamento em tempo real — pensando na TV próxima à equipe de Desenvolvedores, CS e Gestor.

### O que deve conter no Dashboard

**Dash 1**
- [ ] Quantidade de tarefas
- [ ] Quantidade de projetos (por cliente)
- [ ] Gráfico de colunas: quantidade de tarefas por desenvolvedor (Isaac, Felipe e Vitor)
- [ ] Gráfico de tempo médio entre início (tarefa "Boas-Vindas") e fim (tarefa "Primeira Entrega da IA") do projeto

**Dash 2**
- [ ] Aba de registro de Reclamações e Elogios por desenvolvedor (Feedback do mês)
- [ ] Aba "Desenvolvedor do Mês" com foto, quantidade de reclamações e elogios, e notas (0 a 10) sobre entregas e atualizações
  > Verificar com o chefe a possibilidade de bonificação para o Dev do Mês

**Dash 3**
- [ ] Gráfico de porcentagem de conclusão do projeto por empresa

Exemplo:
```
Euro Líder    → 10%
Max Pereira   → 50%
...
```

### Observações sobre o Dashboard

Como todos os gráficos juntos podem ficar pequenos em uma tela só, a ideia é um timer de 30 segundos alternando entre os 3 Dashboards (Dash 1 → Dash 2 → Dash 3).

Dash 2 pode exibir ranking de 1º, 2º e 3º lugar, deixando mais dinâmico e visual.

Uma aba lateral exibirá as reclamações registradas, e outra exibirá todos os projetos em andamento com opção de excluir/cancelar.

Notificações na tela + som para erros do sistema.

---

# Comentários Finais

A maior parte do projeto envolve automação de criação e verificação de tarefas no ClickUp, que não é algo difícil. O mais complexo, de fato, é o Dashboard.

### O que Gostaria
Usar IA para transformar este documento em um PRD estruturado, com passo a passo e marcação de tarefas no formato `( )` — onde o `X` e a data/horário de início e fim serão adicionados manualmente.

### PRD
O PRD deve ser:
- Separado por Etapas (Etapa 1, Etapa 2...) com verificações e funcionalidades de cada uma
- Baseado em boas práticas de programação, especialmente Python e automações
- Organizado em pastas por etapa para facilitar a manutenção

> Como este é o primeiro projeto grande planejado e executado de forma independente, as boas práticas ficam a cargo da IA orientar.
>
> **A IA está estritamente proibida de criar qualquer tipo de código.** (Importante manter isso no PRD caso ele seja enviado para outra IA analisar.)
