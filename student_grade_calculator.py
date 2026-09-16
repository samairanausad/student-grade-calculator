#Student Grade Calculator

print("===Student Grade Calculator===")

Name = input("Enter name of the student:")

English = float(input("Enter english marks:"))
Maths = float(input("Enter maths marks:"))
Hindi = float(input("Enter hindi marks:"))
Science = float(input("Enter science mmarks:"))
Sst = float(input("Enter Sst marks:"))
Total = English + Maths + Hindi + Science + Sst

Percentage = Total/5

if Percentage >= 90:
    grade = "A+"

elif Percentage >= 80:
    grade = "B+"

elif Percentage >= 70:
    grade = "C+"

elif Percentage >= 50:
    grade = "D+"

else:
    grade = "F"

print("RESULT")
print("Student name is",Name)
print("Total marks",Total)
print("Total percentage",Percentage)
print("Grade secured",grade) 
