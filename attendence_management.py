student_list=["Aradya","Baalu","Charan","Dhanush","Ekanth","Farid","Gana","Hruthik","Iqbal","Jagan","Kalki","Lava","Marc","Nani","Omkar","Partha","Raghav","Surya","Thanuj","Umesh","Venky","Yash","Zuber"]
attendence={}
present_count=0
absent_count=0
detained_count=0
def attendence_management(names):
    global present_count,absent_count,detained_count
    print("     ","ABCD Institute of Technology".upper())
    print("\n",names)
    present_absent=input("If student is present say 'present' else say 'absent' : ").lower()
    if present_absent=="p":
        present_count+=1
        return "present"
    elif present_absent=="a":
        absent_count+=1
        return "absent"
    else:
        detained_count+=1
        return "The student is detained "
for names in student_list:
    call_name=attendence_management(names)
    attendence[names]=call_name

print("\n",attendence)
print("\n   "+f"The number of students present in today's class is {present_count}.")
print("\n   "+f"The number of students absent today's class is {absent_count}.")
print("\n   "+f"The number of students datained is {detained_count}.")