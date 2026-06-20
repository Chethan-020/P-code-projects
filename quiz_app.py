q_b={
    "Expand ROM":"Read Only Memory".lower(),
    "Expand RAM":"Random Access Memory".lower(),
    "Expand CPU":"Central processing UNit".lower(),
    "Expand ALU":"Arithmetic Logic Unit".lower(),
    "Expand GPU":"Graphics Proccessing Unit".lower(),
    "Expand SSD":"Solid-State Drive".lower(),
    "Expand OS":"Operating System".lower()
    }
print("WELCOME TO BASIC COMPUTER SCIENCE QUIZ COMPETITION.")
print(" ")
score=0
k=1
for i,j in q_b.items():
    
        print("     "+f"Q{k}.",i)
        candidate_answer =input("      "+"Answer : ").lower()
        if candidate_answer==j:
            print("     "+"Amazing ! That's the right answer")
            score+=1
        else:
            print("      "+f"your bad luck.That's the wrong answer.The right answer is {j}")
        k+=1
        print(" ")
print(f"The total score of your quiz is {score}/{len(q_b)}.")



