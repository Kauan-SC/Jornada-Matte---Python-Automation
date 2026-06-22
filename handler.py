import json
import traceback

from core.logger import get_logger
from stages.stage_1.stage_1 import run

logger = get_logger(__name__)

headers = {
    "Acess-Control-Allow-Origin": "*",
    "Acess-Control-Allow-Headers": "Content-Type"
}


def webhook(event: dict, context: object) -> dict:

    try:
        body: dict = json.loads(event.get("body", "{}"))

        client_name: str = body["client_name"]
        company_name: str = body["company_name"]
        service_description: str = body.get("service_description", "")

        run(client_name, company_name, service_description)            

        logger.info(f"Webhook recebecido - {company_name} {client_name}")

        return {
            "statusCode": 200,
            "body": json.dumps({"Ok": True}),
        }

    except Exception as e:
        logger.error(f"Erro: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        # logger.error(f"Webhook com erro: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"Error": str(e)}),
        }
    
def check_stages(event: dict, context: object) -> dict:
    try:
        from stages.stage_1.stage_1_check import check_stage_1
        from stages.stage_2.stage_2_check import check_stage_2
        from stages.stage_3.stage_3_a.stage_3a_check import check_stage_3a
        from stages.stage_3.stage_3_b.stage_3b_check import check_stage_3b
        from stages.stage_3.stage_3_c.stage_3c_check import check_stage_3c
        from stages.stage_3.stage_3_d.stage_3d_check import check_stage_3d
        from stages.stage_final.stage_final_check import check_stage_4a, check_stage_4b
        check_stage_1()
        check_stage_2()
        check_stage_3a()
        check_stage_3b()
        check_stage_3c()
        check_stage_3d()
        check_stage_4a()
        check_stage_4b()
        return {
            "statusCode": 200,
            "body":json.dumps({"Ok": True}),
        }
    
    except Exception as e:
        logger.error(f"Erro na verificação da tarefa: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        return {
            "statusCode": 500,
            "body": json.dumps({"Error": str(e)}),
        }
