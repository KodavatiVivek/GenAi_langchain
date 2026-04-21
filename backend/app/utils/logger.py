import logging
from pathlib import Path
from datetime import datetime

log_dir = Path(__file__).resolve().parents[3] / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / f"app_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logger = logging.getLogger("rag_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)