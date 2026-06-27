# Estrutura de Pastas — Matte Dashboard

```
matte-dashboard/
├── index.html          # Entry point, contém as 3 abas
├── style.css           # Estilos globais + tema dark/light
├── app.js              # Lógica principal, roteamento de abas, auto-refresh
│
├── config/
│   └── constants.js    # URLs da API, chaves Supabase/ClickUp, IDs de lista
│
├── services/
│   ├── supabase.js     # Funções de leitura/escrita no Supabase
│   └── clickup.js      # getTasks, getSpaces, filtros por stage
│
├── pages/
│   ├── dashboard.js    # Lógica da Aba 1 (métricas, gráfico, status)
│   ├── projects.js     # Lógica da Aba 2 (cards de progresso, 3 pontinhos)
│   └── devmonth.js     # Lógica da Aba 3 (ranking, formulário de reclamação)
│
└── data/
    └── devmonth.json   # Histórico mensal do Dev do Mês (versionado no GitHub)
```