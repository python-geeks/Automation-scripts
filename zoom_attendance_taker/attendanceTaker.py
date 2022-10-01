from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


class Zoom:
    def __init__(
        self, selected_driver, meeting_personal_id, username, meeting_password
    ):

        self.meeting_personal_id = meeting_personal_id
        self.selected_driver = selected_driver
        self.username = username
        self.meeting_password = meeting_password
        self.driver = None

    def setup_driver(self):
        if self.selected_driver == "Chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.selected_driver == "FireFox(Gecko)":
            self.driver = webdriver.Firefox(GeckoDriverManager().install())
        elif self.selected_driver == "Edge":
            self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    def join(self):

        self.wait = ui.WebDriverWait(self.driver, 30)
        self.zoom_join_meeting = self.driver.get("https://zoom.us/join")
        ui.WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH,
                                           '//*[@id="join-confno"]'))
        )
        enter_pid = self.driver.find_element_by_xpath('//*[@id="join-confno"]')
        enter_pid.send_keys(self.meeting_personal_id)
        join_button = self.driver.find_element_by_xpath('//*[@id="btnSubmit"]')
        join_button.click()
        self.wait.until(
            lambda button: self.driver.find_element_by_xpath(
                '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div/div'
            )
        )
        launch_meeting = self.driver.find_element_by_xpath(
            '//*[@id="zoom-ui-frame"]/div[2]/div/div[1]/div/div'
        )
        launch_meeting.click()
        self.wait.until(
            lambda button: self.driver.find_element_by_xpath(
                '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a'
            )
        )
        join_from_browser = self.driver.find_element_by_xpath(
            '//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a'
        )
        join_from_browser.click()
        self.wait.until(
            lambda field:
            self.driver.find_element_by_xpath('//*[@id="inputname"]')
        )
        name_field = self.driver.find_element_by_xpath('//*[@id="inputname"]')
        name_field.send_keys(self.username)
        join_button = ui.WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="joinBtn"]'))
        )
        join_button.click()
        passcode = ui.WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.XPATH,
                                           '//*[@id="inputpasscode"]'))
        )
        passcode.send_keys(self.meeting_password)
        join_button = ui.WebDriverWait(self.driver, 300).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="joinBtn"]'))
        )
        join_button.click()
        """participants = ui.WebDriverWait(self.driver, 600).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="wc-footer"]/div/div[2]/button[1]')
            )
        )"""

    def get_attendees_list(self):

        ui.WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="wc-container-left"]/div[3]/div/'
                    'div[2]/div/div/div[1]/div',
                )
            )
        )
        elem = self.driver.find_element_by_xpath(
            '//*[@id="wc-container-left"]/div[3]/div/div[2]/div/div/div[1]/div'
        )
        attendees = [elem.text]
        try:
            i = 2
            while True:
                elem = self.driver.find_element_by_xpath(
                    f'//*[@id="wc-container-left"]/div[3]/div/div[2]'
                    f'/div/div/div[1]/div[{i}]/div'
                )
                i += 1
                attendees.append(elem.text)
        except NoSuchElementException:
            pass
        print(attendees)
        with open("attended.csv", "w+") as fp:
            fp.write(datetime.now().isoformat(' '))
            fp.writelines(",".join(attendees))


class GUI:
    def __init__(self):
        self.drivers = ["Chrome", "FireFox(Gecko)", "Edge"]
        self.layout = [
            [sg.Text("Meeting ID: "), sg.Input(key="meetingID")],
            [sg.Text("Meeting Password"),
             sg.Input(password_char="*", key="password")],
            [sg.Text("Name"), sg.Input(key="name")],
            [
                sg.Listbox(
                    self.drivers,
                    auto_size_text=True,
                    key="Driver",
                    default_values="Chrome",
                    enable_events=True,
                )
            ],
            [sg.Button("Submit", key="submit")],
        ]

    def create(self):
        self.window = sg.Window("Zoom", self.layout, size=(600, 200))
        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED or self.event == "Exit":
                break
            elif self.event == "submit":
                return self.values


if __name__ == "__main__":
    gui = GUI()
    values = gui.create()
    zoom_client = Zoom(
        values["Driver"][0], values["meetingID"],
        values["name"], values["password"]
    )
    zoom_client.setup_driver()
    zoom_client.join()
    zoom_client.get_attendees_list()
