def format_name(a,b):
    if a=="" and b=="":
        return"Enter a valid string"
    else:
        formated_a=a.title()
        formated_b=b.title()
        return f"{formated_a} {formated_b}"
var1=input("Enter the value of var1:")
var2=input("Enter the value of var2:")
print(format_name(var1,var2))
        