"""
Script standalone (fora do projeto) para consultar o CloudWatch Logs
e ver o histórico de chegada/execução do webhook da Lambda "jornada-matte".

NÃO faz parte do projeto Serverless - é só uma ferramenta de diagnóstico.
Não altera nada no projeto nem na AWS, apenas LÊ os logs.

Como usar:
1. Copie este arquivo para a pasta raiz do projeto
   ("Jornada Matte - Automação Python"), onde está o .env.
2. Instale a dependência (se ainda não tiver):
       pip install boto3 python-dotenv
3. Rode:
       python ver_historico_webhook.py
   (opcional: passe quantas horas atrás quer olhar, padrão = 24h)
       python ver_historico_webhook.py --horas 72
"""

import argparse
from datetime import datetime, timedelta, timezone

import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# Nome do log group da função Lambda que recebe o webhook (handler.webhook)
LOG_GROUP = "/aws/lambda/Jornada-Matte-dev-jornada-matte"
REGION = "us-east-1"


def get_client():
    return boto3.client(
        "logs",
        region_name=REGION,
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )


def formatar_timestamp(ms: int) -> str:
    dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
    return dt.strftime("%d/%m/%Y %H:%M:%S UTC")


def classificar(mensagem: str) -> str:
    msg = mensagem.lower()
    if "webhook recebecido" in msg or "webhook recebido" in msg:
        return "✅ WEBHOOK RECEBIDO"
    if "erro ao criar tarefa" in msg:
        return "❌ ERRO CLICKUP"
    if "erro ao salvar etapa 1 no supabase" in msg or "erro ao salvar" in msg:
        return "❌ ERRO SUPABASE"
    if "erro:" in msg or "traceback" in msg:
        return "❌ ERRO GERAL"
    if "start request" in msg:
        return "▶️  INÍCIO DA EXECUÇÃO"
    if "report request" in msg:
        return "⏹️  FIM DA EXECUÇÃO"
    return ""


def main():
    parser = argparse.ArgumentParser(description="Histórico de chegada do webhook (CloudWatch Logs)")
    parser.add_argument("--horas", type=int, default=24, help="Quantas horas para trás olhar (padrão: 24)")
    args = parser.parse_args()

    client = get_client()

    inicio = datetime.now(timezone.utc) - timedelta(hours=args.horas)
    start_time_ms = int(inicio.timestamp() * 1000)

    print(f"Buscando logs de '{LOG_GROUP}' nas últimas {args.horas}h (desde {formatar_timestamp(start_time_ms)})...\n")

    paginator = client.get_paginator("filter_log_events")
    eventos = []
    try:
        for page in paginator.paginate(
            logGroupName=LOG_GROUP,
            startTime=start_time_ms,
        ):
            eventos.extend(page.get("events", []))
    except client.exceptions.ResourceNotFoundException:
        print(f"Log group '{LOG_GROUP}' não encontrado. Confira se o nome da função está certo "
              f"(rode 'serverless info' pra ver o nome exato).")
        return

    if not eventos:
        print("Nenhum log encontrado nesse período. "
              "Isso pode indicar que o webhook não está sendo chamado, "
              "ou que a função ainda não foi invocada nesse intervalo de tempo.")
        return

    eventos.sort(key=lambda e: e["timestamp"])

    for ev in eventos:
        ts = formatar_timestamp(ev["timestamp"])
        msg = ev["message"].strip()
        tag = classificar(msg)
        linha = f"[{ts}] {msg}"
        if tag:
            print(f"{tag}  {linha}")
        else:
            print(f"           {linha}")

    print(f"\nTotal de linhas de log encontradas: {len(eventos)}")


if __name__ == "__main__":
    main()
