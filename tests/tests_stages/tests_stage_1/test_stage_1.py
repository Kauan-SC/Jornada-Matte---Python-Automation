import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stages.stage_1.stage_1 import run

run(
    client_name="Joao Silva",
    company_name="Euro Lider"
)