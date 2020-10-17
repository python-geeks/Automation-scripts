from win10toast import ToastNotifier
import time

toaster = ToastNotifier()
toaster.show_toast("Example One:",
                   "This is first notifs.",
                   icon_path=None,
                   duration=10)
toaster.show_toast("Example two",
                   "This notification is in it's own thread!",
                   icon_path=None,
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active():
    time.sleep(0.1)
