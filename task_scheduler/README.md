
# Automated Task Scheduler for Repetitive Tasks

This script is designed to automate repetitive tasks by scheduling them at predefined intervals using Python's `schedule` library. It logs task execution, making it easy to track the status of scheduled jobs.

## Functionalities

- Schedule and automate repetitive tasks.
- Log task execution to a file for monitoring and debugging.
- Customizable task functions to fit user needs.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-link>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd automated-task-scheduler
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```bash
   python task_scheduler.py
   ```

## Detailed Explanation of Script

- **Task Functions:** `task_one` and `task_two` are sample tasks. You can modify these functions to suit your automation needs.
  
- **Scheduling:** The script schedules `task_one` to run every 10 minutes and `task_two` to run every hour using the `schedule` library. You can adjust these intervals in the `setup_schedule()` function.
  
- **Logging:** Each task's execution is logged in the `task_scheduler.log` file with timestamps, providing visibility into when tasks were run.

- **Main Loop:** The script continuously runs in an infinite loop (`run_scheduler()`), checking for pending tasks and executing them at the scheduled times.

## Output

The script generates a `task_scheduler.log` file, which logs the execution of tasks like this:

```
2024-10-13 12:00:00 - Task 1 is running
2024-10-13 12:10:00 - Task 1 is running
2024-10-13 13:00:00 - Task 2 is running
```

## Author(s)

- ARNAV RAJ

## Disclaimers

- Ensure that the script is running continuously in the background for tasks to execute as scheduled.
- The `schedule` library is suitable for lightweight task scheduling. For more complex scheduling requirements, consider using a task queue like Celery or a cron job.
