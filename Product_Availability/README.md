A Product Availability Checker will help you to check the availability for all your favorite products and whenever the product becomes available
it will automatically send you an email.

Following is the Procedure to run the Script:
--Open the terminal in same directory of the script and run the command-
           pip install -r requirements.txt
In file send_email.py, enter the mail as written in the file and you need to make sure that the email you are using have less secure apps access.
In file product_availability.py, scroll down and enter the URLs from amazon on which you want notification.

Then comeback to terminal to run this python script-

    python product_availability.py

It will notify you if the product is available, otherwise you will get a mail, once it is made available.
If you want stop the process press ctrl+z