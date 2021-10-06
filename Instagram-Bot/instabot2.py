from instapy import InstaPy

bot = InstaPy(username="enter-your-username-here", password="enter-your-password-here")
bot.login()
bot.set_skip_users(skip_private=False, skip_no_profile_pic=True)
bot.follow_user_followers('nitb.creators', amount=50,
                          randomize=False, sleep_delay=10)
