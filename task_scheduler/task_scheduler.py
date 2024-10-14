import time
import schedule


def task():
    print("Task is being executed")


def task2():
    print("Another task is being executed")


def run_tasks():
    schedule.every(1).minutes.do(task)
    schedule.every(2).minutes.do(task2)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_tasks()
