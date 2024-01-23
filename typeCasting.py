#TypeCasting - process of converting a value of one data type another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

#Explicit
name = "raphael"
age = 0
gpa = 1.8
student = True

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

student = str(student)
print(student)

age = bool(age)
print(age)

#Implicit
print()

x = 2
y = 2.0

x = x / 2

print(f"implicit {x}")
