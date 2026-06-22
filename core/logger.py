import logging
from pathlib import Path

# Create logger paste if it doesn't exist
# log_dir = Path(__file__).parent.parent / "logs"
# log_dir.mkdir(exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    # handlers=[
    #     logging.StreamHandler(),
    #     logging.FileHandler(log_dir / "jornada_matte.log", encoding="utf-8")
    # ]
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)