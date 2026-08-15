                    #Question 1
name = input("Please enter your name                :   ")
age =  input("Please enter your age                 :   ")
def student_info(name,age):
    print("My name is ", name + " and I am ", age , "years old.")
student_info(name,age)

                    #Question 2
a = input("Enter 1ST number                     :   ") 
b = input("Enter 2ND number                     :   ")
def swap(a,b):
    a, b = b, a
    print("The 1ST number after swaping         :   ", a)
    print("The 2ND number after swaping         :   ", b)
swap(a, b)

                    #Question 3
items = ["Mohamed", 20, 2029, "Python", 2.5, "M", 2006]
def firstAndLast(items):
    print("The 1ST item                         :   ", items[0])
    print("The last item                        :   ", items[-1])
firstAndLast(items)

                    #Question 4
grades = {"Ahmed": "B", "Mohamed":"A+", "Hassan":"D", "Ali":"C+", "Mahmoud": "F"}
def getGrade(student,grades):
    if student in grades:
        return grades[student]
    else:
        return "student not found"
print("Mohamed's grade                      :   ", getGrade("Mohamed",grades))
print("Hussien's grade                      :   ", getGrade("Hussien",grades))

                    #Question 5
listOfNumbers =[1,2,3,4,4,5,6,7,7,8,9,10,10]
print("Yor numbers are                      :   ", listOfNumbers)
def removeDuplicates(numbers):
    return set(numbers)
print("your numbers after removing duplicate:   ", removeDuplicates(listOfNumbers))
#------------------------------------------------------------------------------------




