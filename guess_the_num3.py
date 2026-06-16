import random
t=(3,5)
print("***THINK THE NUMBER BETWEEN 1 TO 10*** ")
difficulty=input("Choose the level of difficulty i.e, 'easy' or 'hard' : ").lower()
if difficulty=="easy":
    attempts=t[1]
elif difficulty=="hard":
    attempts=t[0]
if difficulty=="easy" or difficulty=="hard":
    num=random.randint(1,10)
    guessed_num=0
    while guessed_num!=num:
        print(f"You have {attempts} attempts remaining to guess the num.")
        guessed_num=int(input("Guess the num : "))
        if guessed_num>num:
            if attempts==1:
                print("You last the game")
                break
            else:
                print("High value ")
                print("Guess the num again.")
            attempts-=1
        elif guessed_num<num:
            if attempts==1:
                print("You last the game")
                break
            else:
                print("Low value ")
                print("Guess the num again.")
            attempts-=1
        else:
            print(f" You guessed the right num i.e, {num}")
else:
    print("Invalid level of difficalty.")   