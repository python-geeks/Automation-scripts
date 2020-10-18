# Import necessary libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys    # noqa: F401
from selenium.webdriver.common.by import By    # noqa: F401
from selenium.webdriver.chrome.options import Options   # noqa: F401
import os
from time import sleep

# Enter your login Credentials within the ""

username = ""
password = ""

# Select your language, default is C++, you may change it as per your requirements or check out the available list from the langauges.txt folder    # noqa: E501

language = "GNU G++17 7.3.0"

# Locating the problem: Please enter the problem code.

print("Please enter your problem code: For instance 4A or 1021G")
problem = ""
problem = input()
part1 = ""
part2 = ""

t = len(problem)
for i in range(t):
    if(not problem[i].isdigit()):
        break
    else:
        part1 = part1 + problem[i]

for j in range(i, t):
    part2 = part2 + problem[j]

st = part1 + '/' + part2


print('https://codeforces.com/problemset/problem/' + st)

# Locating path of problem

print("Please enter the file path: For instance: 1021A.cpp or Watermelon.cpp")

path = os.getcwd()
Path = input()
path = path + '/' + Path
print(path)

# Acessing the browser

options = webdriver.ChromeOptions()
options.add_argument(r"C:\Users\Divyansh Mishra\AppData\Local\Google\Chrome\User Data\Default")    # noqa: E501
driver = webdriver.Chrome(r'C:\Python\Chromedriver\chromedriver.exe')


driver.get('https://codeforces.com/problemset/problem/' + st)


driver.find_element_by_xpath("//*[@id='header']/div[2]/div[2]/a[1]").click()
driver.find_element_by_id("handleOrEmail").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("/html/body/div[6]/div[5]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input").click()    # noqa: E501

sleep(5)
# Language selection

js = "var op = document.getElementsByTagName('option'); for(var i=0;i<op.length;i++){if(op[i].innerHTML == arguments[0]){op[i].setAttribute('selected','selected');}}"    # noqa: E501
driver.execute_script(js, language)

dropFileArea = driver.find_element_by_xpath("//input[@name='sourceFile']")
dropFileArea.send_keys(path)
driver.find_element_by_xpath("//input[@value='Submit']").click()
