# gmeet_zoom_bot.py

This python script will help you to join daily repetitive classes easily.

- It'll join google meet or zoom meeting as per given time and link.

## Setup instructions


- Firstly clone the project to the desired location, and locate it in the terminal. You would have to download the required modules, you can do this by doing:
  `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

- You can now modify the script slightly according to your schedule:
	1) If you are using chrome as you browser then, in `gMeet()` function replace the `for i in range(4)` with `for i in range(5)`. ( If you are using safari do not change the script.)

	2) Now you can assign your links to `url1` and `url2` variables.

	3) You can replace the timings in main function.

	4) Lastly you can replace 'command' with 'ctrl' if you are on windows.

- This script will let you run two meetings that you have on a daily bases, still you can add more if you wish.

- Please note: The following program supports python3

## Detailed explanation of script, if needed

Below two key modules of this script.

*   `pyautogui` module is used for automation
*   `schedule` module is used to schedule meeting

## Output

Join meeting as per given time and link
