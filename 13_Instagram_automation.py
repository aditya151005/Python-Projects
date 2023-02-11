from instabot import Bot 
bot=Bot()
bot.login(username="username",password="password")
# bot.follow("wscubetechindia")
# bot.upload_photo("C:/Users/Aditya Ranjan/Pictures/Screenshots/1.png",caption="I love python")
# bot.unfollow("wscubetechindia")
# bot.send_message("Hi testing",["itzshashi_singh"])
# followers=bot.get_user_followers("adityaranjan22")
# for follower in followers:
#     print(bot.get_user_info(follower))
followings=bot.get_user_following("adityaranjan22")
for following in followings:
    print(bot.get_user_info(following))