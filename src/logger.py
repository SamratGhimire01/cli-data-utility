import logging

logging.basicConfig(
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data/log_file/app.log"),
        logging.StreamHandler()
    ]
)