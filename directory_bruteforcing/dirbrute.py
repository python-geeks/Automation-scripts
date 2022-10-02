# importing requests python module
import requests
                                    
# enter your ip or domain which youre gonna search for
url = input("Enter domain or IP with / at end:")

# path for the wordlists
path = input("Enter Wordlist path :")

#opening the wordlists in read mode
file = open(path, "r")

#sending the requests and with url, wordlists 
for i in range(len(file)):
   wls = file.readline()
   r = requests.get(url+wls)
   stats = r.status_code

# if the status code is 200 then it is success and there is folder exists
if stats == 200:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)
    
# if the status code is 404 then it is not found means there is no such folder exists
elif stats == 404:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)

# else if none of the above things exists
else:
   print("_"*50)
   print("Path :"+url+wls, (stats))
   print("_"*50)

# closing the file
file.close()
