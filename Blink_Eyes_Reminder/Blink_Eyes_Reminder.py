import time
from plyer import notification
while(True):
  notification.notify(
  title = "Start Blinking you Eyes",
  message = "Blinking nourishes your eye with oxygen and nutrients, keeping your eyes healthy and comfortable",
  timeout = 10
  )
  time.sleep(1200)
