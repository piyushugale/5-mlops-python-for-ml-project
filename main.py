from src.logger.logger import setup_logging, get_logger
from src.utils.data import load_data

def main():
    
    setup_logging()                         # Should only be called once → usually at program startup
    logger = get_logger()                   # after that, any other file/module in your project can just call get_logger() to reuse the same logger (instead of re-configuring logging every time).
    logger.info("Main program started...")

    logger.info("Load data started ...")
    load_data()
    logger.info("Load data completed ...")


if __name__ == "__main__":
    main()

