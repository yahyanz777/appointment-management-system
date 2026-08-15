                        #Knowing user informations
student = {}
student["name"] = input(      "Enter your name            :     ")
student["age"] = int(input(   "Enter your age             :     "))
student["gpa"] = float(input( "Enter your gpa             :     "))
student["department"] = input("Enter your department      :     ")
                        #Take courses from user
courses = []
for i in range(3):
    course = input(           "Enter course               :     ")
    courses.append(course)
student["courses"] = courses
                        #Take grades from user
grades = []
for i in range(3):
    grade = float(input(      "Enter grades               :     "))
    grades.append(grade)
student["grades"] = grades
                        #Calculate total and average
total = sum(student["grades"])
average = total / len(student["grades"])
#Print all student information
print("\n--- Student Information ---")
print("Name       :", student["name"])
print("Age        :", student["age"])
print("GPA        :", student["gpa"])
print("Department :", student["department"])
print("Courses    :", student["courses"])
print("Grades     :", student["grades"])
print("Total Grade:", total)
print("Average    :", average)
                        #Evaluation based on average grade
if average >= 90:
    print("Evaluation : Excellent")
elif average >= 75:
    print("Evaluation : Very Good")
elif average >= 60:
    print("Evaluation : Good")
else:
    print("Evaluation : Fail")
                        #Check if "Python" exists in the courses list
if "Python" in student["courses"]:
    print("Python Course: Enrolled in Python")
elif "python"in student["courses"]:
     print("Python Course: Enrolled in Python")
else:
    print("Python Course: Not enrolled in Python")
                        #Check age status
if student["age"] >= 18:
    print("Age Status : Adult")
else:
    print("Age Status : Minor")
                        #Pass/Fail status
status = "Passed" if average >= 60 else "Failed"
print("Pass Status:", status)


#--------------------------------------------------------------------------------------------------------------------------


#number of students
num_students = int(input("How many students? "))
#Students names
students = []
for i in range(num_students):
    name = input(f"Enter name {i + 1}: ")
    students.append(name)
#Print all names
print("\n--- Student Names ---")
for name in students:
    print(name)
#Print names in uppercase
print("\n--- Names in Uppercase ---")
for name in students:
    print(name.upper())
#Replace a name
name_to_replace = input("\nReplace: ")
if name_to_replace in students:
    new_name = input("New Name: ")
    # Find the index of the old name and update it
    index = students.index(name_to_replace)
    students[index] = new_name
else:
    print(f"'{name_to_replace}' was not found in the list.")
#Remove a name entered by the user
name_to_remove = input("\nRemove: ")
if name_to_remove in students:
    students.remove(name_to_remove)
else:
    print(f"'{name_to_remove}' was not found in the list.")
#Print the final list
print("\n--- Final Student List ---")
print(students)



#---------------------------------------------------------------------------------------------------------------------------



#Ask the user to enter 10 numbers
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
#Print all numbers
print("\n--- All Numbers ---")
for num in numbers:
    print(num)
#Print even numbers
print("\n--- Even Numbers ---")
for num in numbers:
#Checking integer numbers that are divisible by 2
    if num % 2 == 0:
        print(num)
#Print odd numbers
print("\n--- Odd Numbers ---")
for num in numbers:
    if num % 2 != 0:
        print(num)
#Find the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("\nLargest Number :", largest)
#Find the smallest number 
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest Number:", smallest)
#Calculate total and average 
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Total          :", total)
print("Average        :", average)
#Replace one number with another number
print("\n--- Replace a Number ---")
old_num = float(input("Enter the number you want to replace: "))
if old_num in numbers:
    new_num = float(input("Enter the new number: "))
    index = numbers.index(old_num)
    numbers[index] = new_num
    print("Replacement successful!")
else:
    print(f"{old_num} is not in the list.")
#Print the updated list
print("\n--- Updated List ---")
print(numbers)


 #-------------------------------------------------------------------------------


#Ask the user to enter 5 cities
cities_list = []
for i in range(5):
    city = input(f"Enter city {i + 1}: ")
    cities_list.append(city)
#Store them in a tuple
cities_tuple = tuple(cities_list)
#Print all cities using a loop
print("\n--- All Cities ---")
for city in cities_tuple:
    print(city)
#Search for a city
search_city = input("\nEnter a city to search for: ")
found = False
for city in cities_tuple:
    if city.lower() == search_city.lower():
        found = True
        break
if found:
    print(f"'{search_city}' was found in the tuple!")
else:
    print(f"'{search_city}' was not found.")
#Convert the tuple to a list
cities_mutable = list(cities_tuple)
#Replace one city
print("\n--- Replace a City ---")
old_city = input("Enter the city you want to replace: ")
city_replaced = False
for index in range(len(cities_mutable)):
    if cities_mutable[index] == old_city:
        new_city = input("Enter the new city name: ")
        cities_mutable[index] = new_city
        city_replaced = True
        print("City replaced successfully!")
        break
if not city_replaced:
    print(f"'{old_city}' is not in the list.")
#Add a new city
additional_city = input("\nEnter a new city to add: ")
cities_mutable.append(additional_city)
#Convert the list back to a tuple
cities_tuple = tuple(cities_mutable)
#Print the updated tuple
print("\n--- Updated Tuple ---")
# print(cities_tuple)



#--------------------------------------------------------------------------------------


#Read student information from the user
student = {}
student["Name"] = input("Enter student name       : ")
student["Age"] = int(input("Enter student age        : "))
student["GPA"] = float(input("Enter student GPA        : "))
student["Department"] = input("Enter student department : ")
#Print all keys
print("\n--- Dictionary Keys ---")
for key in student.keys():
    print(key)
#Print all values
print("\n--- Dictionary Values ---")
for value in student.values():
    print(value)
#Print key and value together
print("\n--- Key-Value Pairs ---")
for key, value in student.items():
    print(f"{key}: {value}")
#Update GPA
new_gpa = float(input("\nEnter updated GPA: "))
student["GPA"] = new_gpa
#Add Level
level = input("Enter student Level: ")
student["Level"] = level
#Remove Age
if "Age" in student:
    del student["Age"]
#Print the updated dictionary
print("\n--- Updated Dictionary ---")
print(student)



