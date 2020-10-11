# Made by Maxim Iliouchenko (https://github.com/maxily1)

# Importing Libraries
import instaloader

# Get instance
L = instaloader.Instaloader()

# Login and load session
user_name = "" # Change the user_name appropriately
pass_word = "" # Change the pass_word appropriately
L.login(user_name, pass_word) 

# Obtaining profile metadata
profile = instaloader.Profile.from_username(L.context, username=user_name)

# Making a list with all of the followers.
followers_list = []
for follower in profile.get_followers(): # FOR loop to get the usernames and then appen them to the list
    username = follower.username # Getting the user name
    followers_list.append(username) # Appending the user name

# Making a list with all of the followings.
following_list = []
for following in profile.get_followees():
    username = following.username
    following_list.append(username)

# Find persons who don't follow back
not_following_back = []
for following in following_list:
    if following not in followers_list:
        not_following_back.append(following)

print(not_following_back) # Printing who is not following you back

