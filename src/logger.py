import logging
import os

log_dir = "data/log_file"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{log_dir}/app.log"),
        logging.StreamHandler()
    ]
)