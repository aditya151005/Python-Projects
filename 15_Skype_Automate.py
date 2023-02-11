from skpy import Skype
import os.path
#send image
slogin=Skype("skypeusername","password")
contact=slogin.contacts["live:.cid.91f4190f44c59a8e"]
with open("C:/Users/Aditya Ranjan/Pictures/Screenshots/skp.png","rb") as f:
    contact.chat.sendFile(f,'skp.png',image=True)
#creating group
# group=slogin.chats.create(["live:.cid.91f4190f44c59a8e"])
#sending msg
# contact=slogin.contacts["live:.cid.91f4190f44c59a8e"]
# contact.chat.sendMsg("Welcome to WsCube tech")
#Accessing the contact list
# for i in contact:
#     print(i)
