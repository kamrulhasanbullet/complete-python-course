# Write a program to calculate the grade of a student from his marks

marks = int(input("Enter the marks of the student: "))

if marks >= 90 and marks <= 100:
    grade = "Excellent"
elif marks >= 80 and marks < 90:
    grade = "A+"
elif marks >= 70 and marks < 80:
    grade = "A-"
elif marks >= 60 and marks < 70:
    grade = "B"
elif marks >= 50 and marks < 60:
    grade = "C"
else:
    grade = "Fail"

print(f"The grade of the student is: {grade}")
