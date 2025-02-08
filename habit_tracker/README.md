Habit Tracker

1. Installing Dependencies
To install the required dependencies, run the following command:

$ pip install -r requirements.txt

2. Using the Habit Tracker
Run the application using:

python habit_tracker.py

Once the GUI opens, you can:

Add a Habit: Enter the name of a habit in the input field and click "Add Habit."
Mark Habit Done: Enter the habit name and click "Mark Habit Done" when you've completed the habit for the day.
View Habits: Click "View Habits" to display your current habits and their streaks.

3. Streak and Progress Tracking
The Habit Tracker records each habit's daily streak and saves progress in a habits.json file. Each day you mark a habit as completed, the streak increases by one. Use the "View Habits" option to see how long you've maintained each habit.

Bonus1 (Fixed Schedule for Habit Completion)
You can set up a fixed daily schedule to automate marking your habits as done.
Create a new Python file in the same directory as habit_tracker.py and code the following:

from habit_tracker import mark_habit_done
import time
import datetime

# Define your schedule
times = [[1000, 1100], [1200, 1300], [1400, 1500]]  # Time in 24-hour format
habits = ["Habit1", "Habit2", "Habit3"]

while True:
    current_time = int(datetime.datetime.now().strftime("%H%M"))
    for i, time_slot in enumerate(times):
        if time_slot[0] <= current_time < time_slot[1]:
            mark_habit_done(habits[i])
    time.sleep(60)  # Check every minute

* Replace "Habit1", "Habit2", and "Habit3" with your actual habit names, and adjust the times accordingly.

Bonus2 (Habit Notification System)
You can set up notifications for your habits by installing the plyer library to send desktop notifications:

pip install plyer

Use the notification functionality within the app to remind you to mark your habits as done.