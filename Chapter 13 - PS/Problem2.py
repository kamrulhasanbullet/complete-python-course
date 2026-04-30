# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Harry, his marks are 72 and phone number is 99999888"

name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
phoneNubmer = int(input("Enter Your Phone Number: "))


result = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phoneNubmer)

print(result)