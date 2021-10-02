# Auto SMS
Easy CLI interface for users looking to test their SMS campaign integration with Kaleyra 

The requirements for any user are :-
* A kaleyra account and api key, secret key
* python3 installed
* pip packages required are requests, json

To get the API key from Kaleyra follow these steps:

* Go to the kaleyra.com
* Click on the register button and follow the registration process and complete it.
* The follow the prompt for KYC verification.
* The you will be directed to your dashboard
* On the bottom left corner click the option `developers`
* In the `developers` tab you will get a option for generating `API KEY`
* After API key generation please copy those key to `line no. 10,11,12`
* Click on Billing to make sure your billing details are up-to-date. If they not, follow this link.
For futhers details of the API please refer to the official documentation https://developers.kaleyra.io/docs/getting-started-with-kaleyra-cloud-apis

##### Please replace the comments in main.py with your SID, API Key, SenderID

To run the program, write the following code in the terminal

    python main.py

The program is up and running