import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_name = "Drink_Water_Notification",
            app_icon = "D:\\Abdul Rehman\\AI Automations\\Dekstop_Notification\\Icon.ico",
            timeout = 10)
	#Time to After which you want the Notfication in Sec  
        time.sleep(5)
