student_record={}
def detail_entry():
    student=input("\nEnter the name of the student : ")
    student_detail={}
    for i in range(2):
        key=input("Enter the key: ")
        value=input("Enter the value : ")
        student_detail[key]=value
        student_record[student]=student_detail
    condition=input("\nIf you have more student continue entry...To continue the entry enter 'continue' else 'exit' : ").lower()
    if condition=="exit":
        print("\nDetail entry is completed")
        return
    else:
        detail_entry()
detail_entry()
print("\n****Here is the record of the students****")
print(student_record)
