PIN="1234"
trials=1
while trials<=3:
    user_input=input(f"trial{trials}|PIN>>")
    if user_input==PIN:
        #print("CORRECT PIN")
        break
        print("CORRECT PIN")
    else:
        print("WRONG PIN")
    trials+=1