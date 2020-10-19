# CF autosubmit (Headless version)

* This script will autmatically submit your code for the **Codeforces problems**. 
* This version will work for **Chrome** users only (other browsers coming soon!).

## Presetup zone

* Go through the **requirements.txt** file to make sure you have the required libraries.

* Download chromedriver zip file according to your chrome version (you can check your chrome version on 
  `chrome://version`) from [here](https://chromedriver.chromium.org/downloads). Make sure you save the chromedriver folder in which all your python files are stored after you downloaded python. (For ex: The path for a windows user might look like:- `C:\Python\Chromedriver`) 


## Setup Zone  

### One time settings

As soon as you get hold of the script, you need to make some changes according to your device to make the flow smoother everytime you run this script.

1. Enter your username and Password within the `""` in the `headless.py` file.

2. Select your preferred language from the `language.txt` file and if required write your langauge in the `""` of the `headless.py` file. The default has been set to `GNU G++17 7.3.0`. So C++ users may skip this step :) 

3. Head to `chrome://version` and copy the path given in heading of **Profile path** and paste it in place of:
`options.add_argument(r"C:\Users\Divyansh Mishra\AppData\Local\Google\Chrome\User Data\Default")` in the `headless.py` file. Mention your profile path in place of `C:\Users\Divyansh Mishra\AppData\Local\Google\Chrome\User Data\Default`. 

4. Head towards the chromedriver path from the folder where you saved it and paste it in place of:`driver = webdriver.Chrome('C:\Python\Chromedriver\chromedriver.exe')` in your `headless.py` file. You need to make changes in `C:\Python\Chromedriver\chromedriver.exe` part of the code. Do not tamper the remaining part of the line.


## Running the script

Now that you have made all changes according to your device, a few tips:

* Keep this script in the same folder where your codes for the CodeForces problems are saved.
* This script has been written for practice problemset, in order to use it for contests you need to make the changes: `driver.get('link for your problem'/+st)`. Now run the script from the terminal.

* The script will ask you to enter your problem code: For example:- 1029C or 69D
* Next you need to enter the saved file, for example: 1029C.py or 69D.cpp
* Hit enter and solve the next question now :)
* This sript will submit your code in the background and send you a screenshot of the task done.
* The screenshot will be saved in the same folder as that of this script.

#### For any issues regarding this PR feel free to contact me !
