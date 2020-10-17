from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
toaster.show_toast("I am the voice of today, the herald of tomorrow. ...I am the leaden army that conquers the world -- I am TYPE.",icon_path=None,duration=10)

toaster.show_toast("Example two","This notification is in it's own thread!",icon_path=None,duration=5,threaded=True)

# Wait for threaded notification to finish
while toaster.notification_active():time.sleep(0.1)