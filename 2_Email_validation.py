#Emailvalidation using string
email=input("Enter your Email: ")#g@g.in(.=-3),wscube@gmail.com(.=-4)
k,j,d=0,0,0
#minimum length of the email should be 6
if len(email)>=6:
    #first letter of the email should be alphabet 
    if email[0].isalpha():
        #email contains only 1 @ symbol
        if ("@" in email) and (email.count('@')==1):# @ condition
            #position of . symbol in email must be either 3rd and 4th from right to left
            if (email[-4]=='.')^(email[-3]=='.'): #. condition(Exor Any 1  true then true only)
                for i in email:
                    #Email does not contain space
                    if i==i.isspace():
                        k=1
                    #Email does not have uppercase character
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=='@':
                        continue
                    #Any other conditions which violates the email validations
                    else:
                        d=1
                #Email does not contain space condition violates
                #Email does not have uppercase character violates
                #Any other conditions which violates the email validations
                if k==1 or j==1 or d==1:
                    print("Wrong Email 5")
                # valid Emails 
                else:
                    print("Valid Email")
                    
            else:
                print("Wrong Email 4")#position of . symbol in email must be either 3rd and 4th from right to left violates
        else:
            print("Wrong Email 3") #email contains only 1 @ symbol violates
            
    else:
        print("Wrong Email 2") #first letter of the email should be alphabet violates
else:
    print("Wrong Email 1")#if the length of email violates.