# A script to find who is not following back in Instagram
This simple code, will connect to your Instagram account using your provided login data, will scan your account for your followers and your followings, and then will search for people who are not following you back. 

## Dependencies
Firstly, Install the required library using the following command:
```sh
python -m pip install instaloader
```

## Steps for running the script:
1. Run the script using the following command - make sure to change `<username>` and `<password>` appropriately without the "<>" symbols:
```sh
python3 main.py -u <username> -p <password>
```
2. Wait a few seconds for the program to finish, and there will be a list of all of the people who don't follow back.
3. That's it.

## Troubleshoot:
* If you get a problem "Checkpoint required" or something samiliar. Do the following: Seems like the only problem was to just confirm it was by following the link which is stated in the error message. All I did was logging out of my main account, running the program, getting the error, pressing the link, confirming that I did try, and it was fixed.

## NOTE: If you stalk in any errors, Please open an issue / contact me (https://github.com/maxily1)

