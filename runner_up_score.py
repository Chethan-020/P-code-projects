records=[]
S=list([])
for i in range(int(input("Enter the range of:"))):
    name=input("Enter the name:")
    score=int(input("Enter the score:"))
    records.append([name,score])
    S.append(score)
S.sort()
second_lowest=S[1]
print(records)
print(S)
print(f"The second lowest score is :{second_lowest}")

second_low_name=""
for name,score in records:
    if score==second_lowest:
        second_low_name=name
print(f" The second lowest scorer name is {second_low_name} with score of{second_lowest}")