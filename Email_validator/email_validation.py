email = input("Enter your Email : ")   # minimum charecter = a@b.in (i.e 6 charecters)
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():                                              # first letter of the email should be an alphabet
        if ("@" in email) and (email.count("@")==1):                         # @ should be present in email and only once
            if (email[-4]==".") ^ (email[-3]=="."):                      # . should be at 3rd position from last in .in and 4th position from last in .com .. here we use ^(XOR) operator because it might be possible that someone writes ..in . in that case if or operator is used it will show correct but in reality it is wrong
                for i in email:
                    if (i==i.isspace()):                              # our email should not contain spaces
                        k=1
                    elif i.isalpha():
                        if i.isupper():
                            j=1
                    elif i.isdigit():                                 # email should not contain digits
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Cookie says Email should not contain spaces and should not contain uppercase letters and should not contain any other alphanumeric charecters")
                else:
                    print("Cookie Says Right Email")
            else:
                print("Cookie says position of . is invalid")
        else:
            print("Cookie says @ should be present only once in email")
    else:
        print("Cookie says First letter of the email should be an alphabet")

else:
    print("Cookie says Email length too short")


