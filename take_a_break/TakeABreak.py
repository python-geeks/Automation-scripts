import webbrowser
import time

total_breaks = int(3)
break_count = int(0)

print("This program started on" + time.ctime())

while break_count < total_breaks:
    time.sleep(int(2) * int(60) * int(60))
    webbrowser.open("http://www.youtube.com")
    break_count += int(1)
