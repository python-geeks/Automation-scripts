This is an automated calling script genrated using python it uses twilio for
making calls thus to use this script you have to create twilio account

To create twilio account log in to twilio website

after completing the registration you will receive various credentials 
such as auth_token , account s_id and one auto_generated mobile number

**note since it is a trail version you will only able to call to only verified no.
once your plan get upgraded you will able to call any number without any restriction


requirement :

twilio client

installation :  pip install twilio

client.calls.create will be responsible for the call process 
also here url is the reponse urls , i.e whatever you want to
give as a response to the reciever you can give by simply creating your
own at twilio.com, since it is a trail we have used trail response     
'to' attribute specifies whom you want to dial
'from' attribute specifies from which number the receiver will receive the call
**note that number will be auto genrated in the trail process