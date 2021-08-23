A Price Tracker will help you to track the price for all your favorite products and whenever the price drops down it will automatically send you an email

# Procedure to run the Script

open the terminal in same directory and run
 
  ```
   pip install -r requirements.txt
  ```
 
 In file send_email.py, enter the mail as written in the file ( make sure that the email you are using have less secure apps access 
 follow this link to turn on this setting <a href="https://support.google.com/accounts/answer/6010255?hl=en">Click here</a> ) <br/>
 In file priceTrackerScript.py, scroll down and enter the URLs from amazon and limit on below which you want notification
 
 Then comeback to terminal run python script
 
   ```
   python priceTrackerScript.py
  ```
  
 Then it will continuously running till the price drop. If you want stop the process press ctrl+z 
