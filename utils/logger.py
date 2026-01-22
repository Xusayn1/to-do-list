import logging

logging.basicConfig(
    filename="to_do/logger.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
