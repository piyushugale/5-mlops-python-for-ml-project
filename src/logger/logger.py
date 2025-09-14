import logging
import os
from datetime import datetime

def setup_logging():
    """Basic logging setup."""
    
    # Create logs directory
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # Create timestamped log file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f"logs/mlops_{timestamp}.log"
    
    # Configure logging
    logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging started. File: {log_file}")
    return logger

def get_logger():
    """Get logger."""
    return logging.getLogger(__name__)


'''
Summary:
1. Creates a logs directory (if it doesn’t already exist) to store log files.
2. Generates a timestamped log file (mlops_YYYYMMDD_HHMMSS.log) for each run.
3. Configures logging with both file logging and console streaming using logging.basicConfig.
4. Uses a consistent format: [timestamp] - LEVEL - message.
5. setup_logging()  # Should only be called once → usually at program startup
   get_logger()     # After that, any other file/module in your project can just call get_logger() to reuse the same logger (instead of re-configuring logging every time).
'''