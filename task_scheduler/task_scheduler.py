import schedule
import time
import logging

# Set up logging
logging.basicConfig(
    filename='task_scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Example task 1: Function to be scheduled
def task_one():
    logging.info("Task 1 is running")

# Example task 2: Another task to be scheduled
def task_two():
    logging.info("Task 2 is running")

# Schedule tasks
def setup_schedule():
    # Schedule task_one every 10 minutes
    schedule.every(10).minutes.do(task_one)
    
    # Schedule task_two every hour
    schedule.every().hour.do(task_two)
    
    # Add more tasks here as needed

# Main loop to keep the scheduler running
def run_scheduler():
    setup_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()
