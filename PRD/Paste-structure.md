# Estrutura de Pastas — Jornada Matte (atual)

```
jornada_matte/
│
├── handler.py                 # Ponto de entrada Lambda — webhook e check_stages
├── config.py                  # Configurações centralizadas (lidas do .env)
├── constants.py               # Constantes do projeto (etapas, status, assignees)
├── serverless.yml             # Configuração Serverless Framework (Lambda + EventBridge)
├── requirements.txt           # Dependências do projeto
├── .env                       # Credenciais e variáveis de ambiente (NÃO versionar)
├── .env.example               # Exemplo de variáveis necessárias (versionar)
├── .gitignore
├── README.md
│
├── core/
│   ├── __init__.py
│   ├── database.py            # Conexão Supabase e funções de leitura/escrita
│   ├── helpers.py             # Funções auxiliares
│   ├── logger.py              # Configuração do sistema de logging
│   └── notifier.py            # Notificações de erro
│
├── integrations/
│   ├── __init__.py
│   └── clickup.py             # Criação, verificação e busca de tarefas no ClickUp
│
├── stages/
│   ├── __init__.py
│   ├── stage_1/
│   │   ├── stage_1.py
│   │   └── stage_1_check.py
│   ├── stage_2/
│   │   ├── stage_2.py
│   │   └── stage_2_check.py
│   ├── stage_3/
│   │   ├── stage_3_a/
│   │   │   ├── stage_3a.py
│   │   │   └── stage_3a_check.py
│   │   ├── stage_3_b/
│   │   │   ├── stage_3b.py
│   │   │   └── stage_3b_check.py
│   │   ├── stage_3_c/
│   │   │   ├── stage_3c.py
│   │   │   └── stage_3c_check.py
│   │   └── stage_3_d/
│   │       ├── stage_3d.py
│   │       └── stage_3d_check.py
│   ├── stage_4/
│   │   ├── stage_4_a/
│   │   │   └── stage_4a.py
│   │   └── stage_4_b/         
│   │       └── stage_4b.py
│   └── stage_final/
│       ├── stage_final.py
│       └── stage_final_check.py
│
├── dashboard/                 # Pendente de implementação
│   ├── app.py
│   ├── static/
│   └── templates/
│
├── logs/
│   └── jornada_matte.log
│
├── PRD/
│   ├── PRD-Project.md
│   ├── Paste-structure.md
│   ├── Checklist.md
│   └── Raw-Notes.md
│
└── tests/
    ├── __init__.py
    ├── test_helpers.py
    ├── test_stage_2.py
    ├── tests_clickup/
    │   ├── test_clickup.py
    │   └── test_connection.py
    └── tests_stages/
        ├── tests_stage_1/
        │   └── test_stage_1.py
        └── tests_stages_2/
```

## Diferenças em relação à estrutura planejada

| Planejado | Real |
|---|---|
| `main.py` | `handler.py` (ponto de entrada Lambda) |
| `stages/` flat (arquivos diretos) | `stages/` com subpastas por etapa |
| `stages/stage_3b.py` | `stages/stage_3/stage_3_b/stage_3b.py` |
| stage_3c e stage_3d não existiam | Adicionadas stage_3_c e stage_3_d |
| `integrations/whatsapp.py` | Não existe ainda |
| `tests/` flat | `tests/` com subpastas por contexto |
| — | `logs/` e `PRD/` adicionados |
| `stage_4_b/` | `Stage_4_b/` — capital S, inconsistência a corrigir |