students = [("Ali", 80), ("Sara", 95), ("Ahmed", 40), ("Omar", 70), ("Mona", 100)]

# Filter students with marks >= 60
filtered_students = filter(lambda s: s[1] >= 60, students)

# Increase each remaining student's mark by 5
updated_students = map(lambda s: (s[0], s[1] + 5), filtered_students)

#Convert the map object to a list
final_result = list(updated_students)

print(final_result)

#_________________________________________________________________________

#Function to calculate the square of a number
def square(x):
    return x * x

user_input = input("Enter 5 integers        :   ")

original = list(map(int, user_input.split()))

squared = list(map(square, original))

#Display the results
print("Original         :   ", original)
print("Squared          :   ", squared)

#____________________________________________________________________________

#Check if a number is even
def is_even(n):
    return n % 2 == 0

#User entering 10 numbers
user_input = input("Enter 10 numbers        :   ")

original = list(map(int, user_input.split()))   
#Filter the list
even_numbers = list(filter(is_even, original))

# Display the results
print("Original         :   ", original)
print("Even Numbers     :   ", even_numbers)
print("Count            :   ", len(even_numbers))

#_____________________________________________________________________________

from functools import reduce

#Entering grades for 8 students
user_input = input("Enter 8 grades      :    ")
original_grades = list(map(int, user_input.split()))

#Adding 5 bonus marks to every grade
after_bonus = list(map(lambda grade: grade + 5, original_grades))

#Filter passing grades (>= 60) 
passing_grades = list(filter(lambda grade: grade >= 60, after_bonus))

#Sort passing grades from highest to lowest
sorted_grades = sorted(passing_grades, reverse=True)

#Calculate total
total = reduce(lambda x, y: x + y, passing_grades)
average = total / len(passing_grades)

# Display results
print("Original Grades      :   ", original_grades)
print("After Bonus          :   ", after_bonus)
print("Passing Grades       :   ", passing_grades)
print("Sorted               :   ", sorted_grades)
print("Total                :   ", total)
print("Average              :   ", average)