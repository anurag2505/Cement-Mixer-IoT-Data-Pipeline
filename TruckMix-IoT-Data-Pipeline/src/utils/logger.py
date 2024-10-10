import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger; can be used across the module."""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

# Example usage
if __name__ == "__main__":
    log_file_path = os.path.join(os.path.dirname(__file__), 'app.log')
    logger = setup_logger('main_logger', log_file_path)
    logger.info('Logger is set up and ready to use.')