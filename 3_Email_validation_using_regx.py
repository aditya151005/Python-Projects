#a-z
#0-9
#. -time 1(before @)
#@-time 1
#. 2,3
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email: ")
if re.search(email_condition,user_email):
    print("Email is valid")
else:
    print("Email is Invalid")