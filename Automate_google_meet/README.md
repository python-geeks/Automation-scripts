# Automating online classes!

<h2><b><i>About:</i></b></h2>
<p>
  I created this to make the proccess of joining online classes easier. Many students find it difficult to join classes on time while being at home and in their comfort zone.
  Using web-automation you can prevent being late by just running a python file. 
</p>

<h2><b><i>Modules used:</i></b></h2>

<ul>
  <li>pyautogui, sys</li>
  <li>time</li>
  <li>webbrowser</li>
</ul>

<p>
  
  We use pyautogui and sys to control our mouse movements. <br>
  We use time module to take breaks while our program is running.<br>
  We use webbrowser to control website tasks like opening a webpage.
  
</p>

<h2><b><i>To use this source follow the following steps:</i> </b></h2>

<b> 1) </b> The program contains few lines of code that will track your mouse movements as show in the image below. The values that we get are the co-ordinates of the mouse at a specific point on your screen. Lets say you open a webpage...and there is a button that you need to click. Run the mouse tracking function, hover over that button and get the co-ordinates of your mouse at that point. By doing that we now have the location of the specific button on your screen. You can substitue those values in the program where it says: pyautogui.moveTo(x,y). Replace 'x' and 'y' with your values. You would need to get co-ordinates of all the buttons that are going to be used...

<p align="center">
<img src="https://github.com/m4dummies/webAutomation--Python/blob/master/images/img1.PNG" alt="example image" height="400" >
</p>

<b> 2) </b> Now that we have the values and have already substitued them. We can go ahead and format the code so that it looks like the image shown below. This is the finalized code. If you have to locate and click more buttons in order to get your task done u can copy and paste this part of the code: <br>
pyautogui.moveTo(x,y)<br>
pyautogui.click()<br>
you can do this multiple times. Once you are done with the following steps the program will be ready to run. Enjoy :)


<p  align="center">
  <img src="https://github.com/m4dummies/webAutomation--Python/blob/master/images/img2.PNG" alt="example image2" height="400">
</p>

<p>
  <h5>Thanks for dropping by and trying my program. I am open to feedbacks.</h5>
</p>

