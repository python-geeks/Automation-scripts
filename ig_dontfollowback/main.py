# Made by Maxim Iliouchenko (https://github.com/maxily1)

# Importing Libraries
import instaloader
import argparse

# Get instance
L = instaloader.Instaloader()

# Creating an argument parser
parser = argparse.ArgumentParser(description='Process log-in data')

# Adding arguments
parser.add_argument('-u', type=str, required=True, help="Enter a username which will be used in the app.")
parser.add_argument('-p', type=str, required=True, help="Enter a password which will be used in the app.")

# Parsing the args
args = parser.parse_args()

# Defining the args into variables
user_name = args.u
pass_word = args.p

# Login data and load session
L.login(user_name, pass_word)

# Obtaining profile metadata
profile = instaloader.Profile.from_username(L.context, username=user_name)

# Making a list with the usernames of the followers
followers_list = []
for follower in profile.get_followers():
    username = follower.username
    followers_list.append(username)

# Making a list with all of the people who you're following
following_list = []
for following in profile.get_followees():
    username = following.username
    following_list.append(username)

# Find people who don't follow back
not_following_back = []
for following in following_list:
    if following not in followers_list:
        not_following_back.append(following)

print(not_following_back)

choice = input("Would you like to save the people who don't follow you as a file? (y/n): ")
if choice == "y":
    f = open("dont_follow_back.txt", "w")
    for person in not_following_back:
        f.write(person + "\n")
else:
    exit
