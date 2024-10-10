import time
import psutil
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def monitor_pipeline():
    while True:
        # Get CPU and memory usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # Log the health and performance metrics
        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory_usage}%")

        # Sleep for a specified interval before the next check
        time.sleep(10)

if __name__ == "__main__":
    logging.info("Starting pipeline monitor...")
    monitor_pipeline()