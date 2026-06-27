# Dashboard

## Funcionalidade do Dashboard 

O objetivo do Dashboard é ajudar e facilitar os gestores e outros a saberem em qual etapa cada cliente está, média de tempo para entrega do projeto, quantidades de atividades
necessárias para se fazer, quantidade de atividades por Desenvolvedor e ajustar a gerir e atualizar o projetos mais facilmente
Além de enviar avisos e outros quando projetos são iniciados, tarefas entregues e outros

---

## Quais serão os Dashboards

### Total de Projetos ativos e Total de Projetos finalizados
Dois retângulos com a quantidade de projetos ativos(Pegando do Supabase) e o total de projetos entregue(Que será um número que colocaremos + os próximos do Supabase)

### Quantidade de tarefas por estágio
O Objetivo é criar 5 quadrados pequenos e básicos, todos um do lado do outro, mostrando a quantidade de tarefas em cada estágio
Os estágios são:
IAs para Criar/Revisar
Tarefas de Suporte
Tarefas do CS
Personalizar CRM
Reuniões Kauan
Reuniões Pedro

Isso ficaria na primeira linha de quadrados, todas com um título de fácil leitura e um número da quantidade de atividades em grande escala

---

### Média de tempo de entrega da IA
Um gráfico, queria fazer um de colunas, que mostra sobre as entregas mais recentes e logo ao lado tem uma média geral
O gráfico de colunas é o tempo de cada projeto(Por cliente), pegando os mais recentes que foram entregues

Imagina que tem 5 colunas com os últimos 5 projetos e o tempo de cada e do lado uma média geral

---

### Média de tempo de finalização de todo o projeto
Esse é somente um quadrado simples e com um número no centro

---

### Dash de Status
Dash retângular que cobre todo o restante da tela inferior, com as tarefas urgentes e o tempo de entrega. Vou colocar uma variável que verifica se tem muitas tarefas com prazo
curto e aparecer um "Status" e tipo um Emoji sobre isso -> "Foco total (Em Vermelho)" , "Tranquilo, mas atenção(Em Amarelo)" e "Deboas(Em Azul)"


------------------------------------------------------------------------------------------------------

# Segunda aba

## Etapa de Porcentagem dos Projetos
Ness etapa ela pega todos os dados dos Leads direto do Supabase, pois não leva em conta os dados do ClickUp.
Ela pega o "company_name" como ID e pega o STAGE também para saber a porcentagem

Até o stage_2 é somente uma porcentagem
Depois quando tem a bifurcação, ele divide em duas(Porcentagem de CRM e Porcentagem da IA). Dependendo disso ele terá uma porcentagem de conclusão do Projeto.

Outra coisa que queria fazer era nessa aba colocar uma opção de 3 pontinhos que consigo mexer em algumas configurações do projeto do Lead
Mexer no Status dele(Ativo, Desativado, Concluído e outros)

## Visual desse Dash
O visual tem que ser uma caixinha com o "Company_name" do cliente e as porcentagens logo abaixo e os 3 pontinhos. Bem básico e simples
Coisa não muito grande, mas que seja bem visível e fácil de compreender quantos porcento de cada projeto

------------------------------------------------------------------------------------------------------

# Terceira aba

## Desenvolvedor do mês
Essa etapa é sobre o desenvolvedor do mês
Ela é como se fosse um histórico, não sei se tem uma forma de guardar isso no HTML e depois criar uma automação que da um ADD e PUSH disso no GitHub
Esse histórico é somente mensal

## Funcionamento
Básicamento, a cada reclamação o CS adiciona essa reclamação nessa etapa, escolhe o desenvolvedor, o nome da empresa/cliente e motivo
O que ele precisa armazenar no Github são essas informações. Dentro do Front é somente a pontuação
Quem tiver mais pontos positivos e menos negativos é o DEV do Mês

## Visual
O Visual é algo bem simples
Somente uma colocação com Primeiro, Segundo ou Terceiro
O primeiro lugar aparece a foto dele, dos outros somente o nome

------------------------------------------------------------------------------------------------------

# Global do Projeto
Esse projeto precisa ter um background que pode se modificar entre BLACK e WHITE
Quero adicionar algum emoji, simbolo ou algo do tipo
Esses Dashbods se auto atualizam
Ou seja, ele terá um Update a cada 1/2 horas
E ele ficará mudando as abas a cada 2 minutos(Talvez eu mexa nisso depois, mas por enquanto esse é o tempo)

Ainda estou verificando vários sites de projetos meio que prontos e Blackgrounds legais, então talvez use isso na criação

