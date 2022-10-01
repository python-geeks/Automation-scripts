import ctypes
import sys
from sys import platform
import os
from os import system
from elevate import elevate


class Blocker:
    hosts_path = ''
    redirect = "127.0.0.1"
    website_list = []
    os_number = 0
    exit_blocker = False

    def __init__(self, path, os_num):
        self.hosts_path = r"" + path
        self.os_number = os_num

        print("Blocked Websites (^v^)")
        print("# None")

    def blocker_menu(self):
        if self.os_number == 2:
            self.duplicate_host_file()

        while not self.exit_blocker:
            print("********************")
            print("WEBSITE BLOCKER MENU")
            print("********************")
            print("Type '+' to add Website")
            print("Type 'exit' to stop the blocker")
            user_input = input("Enter here: ")

            if user_input == '+':
                self.add_websites()

                print("Blocked Websites (^v^)")
                for website in self.website_list:
                    print("# " + website)
            elif user_input == 'exit':
                print("Restoring Every change.....")
                self.restore_host_file()
                print("Thanks you using")
                self.exit_blocker = True
            else:
                print("Invalid Input Try Again")

    def restore_host_file(self):
        with open(self.hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in self.website_list):
                    file.write(line)

            file.truncate()
        file.close()

    def duplicate_host_file(self):
        # to create a copy of host file specially for windows if script not working
        pass

    def add_websites(self):
        print("Enter a website url to add like 'www.facebook.com or facebook.com'")
        user_input = input("Enter URL Here: ")
        self.website_list.append(user_input)
        with open(self.hosts_path, 'r+') as file:
            file.write(self.redirect + " " + user_input + "\n")

        file.close()

    def clear_console(self):
        if self.os_number == 2:
            _ = system('cls')
        else:
            _ = system('clear')


def get_os():
    if platform == "linux" or platform == "linux2":
        # linux
        return 0
    elif platform == "darwin":
        # OS X
        return 1
    elif platform == "win32":
        # Windows...
        return 2


def driver():
    if get_os() == 2:
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        if os.getuid() == 0:
            elevate(graphical=False)

    print("Running script with Root/Admin privileges. AWESOME!!")

    os_number = get_os()

    if os_number == 2:
        print("OS: Windows")
        website_blocker = Blocker(r"C:\Windows\System32\drivers\etc\hosts", os_number)
        website_blocker.blocker_menu()
    elif os_number == 1:
        print("OS: OS X")
        website_blocker = Blocker("/etc/hosts", os_number)
        website_blocker.blocker_menu()
    elif os_number == 0:
        print("OS: Linux")
        website_blocker = Blocker("/etc/hosts", os_number)
        website_blocker.blocker_menu()


if __name__ == "__main__":
    driver()
