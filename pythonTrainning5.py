x = int(input ("Enter a positive integar        :   "))
sum = 0
for i in range(1, x + 1):
    sum  += i
print("Your sum = ", sum)

#___________________________________________________________

n = int(input("Enter a positive integar        :   "))
for i in range (1, 11):
     multiply = n*i
     print(n, " x ", i, " = ", multiply)

#___________________________________________________________

y = int(input("Enter a positive integar        :   "))
count = 0
for i in range(1, y + 1):
    if (i%2 == 0):
        count += 1
print("There are ", count, " even numbers")

#___________________________________________________________

secretNumber = 15
m = int(input("Guess the number     :   "))
while m != secretNumber :
    print("Try again")
    m = int(input())
else:
    print("Congratulations! You guessed it!") 

#___________________________________________________________   

s = int(input("Enter the size of a square       :   "))
i = 0 
d = "*"
while i != s :
    print(d*s)
    i+=1

#__________________________________________________________________

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
#_________________________________________________________________
#shopping cart program
def Menu ():
  print("""1-Add Product
2-Remove Product
3-View Cart
4-Checkout
5-Exit""")
dict1=[]
Menu()
choice = int(input("Enter your choice: "))
while choice != 5:
  if(choice==1):
    product_name = input("Enter the product name: ")
    product_price = float(input("Enter the product price: "))
    dict1.append({"product name":product_name,"price":product_price})
    print("The product has been added successfully!")
  elif(choice==2):
    remove_product = input("Enter the product name to remove: ")
    for i in dict1:
      if(i["product name"]==remove_product):
        dict1.remove(i)
    print("The product has been removed successfully!")
  elif(choice==3):
    print("The cart contains the following products:")
    print(dict1)
  elif(choice==4):
    total_price = 0
    discount_amount = 0
    final_price = 0
    for i in dict1:
      total_price += i["price"]
    if(total_price > 500):
      discount_amount = total_price * 0.1
      final_price = total_price - discount_amount
      print("Total price: ",total_price)
      print("Discount amount: ",discount_amount)
      print("Total price after discount: ",final_price)
  elif(choice==5):
    print("Exit")
  else:
    print("Invalid choice")
  print()
  Menu()
  choice = int(input("Enter your choice: "))
print("End shopping!")

#_____________________________________________________________________________________

#Employee Salary System
dict1 = {}

employee_name = input("Enter the employee name: ")
employee_department = input("Enter the employee department: ")
employee_salary = float(input("Enter the employee salary: "))

dict1[employee_name] = {"department":employee_department,"salary":employee_salary}
print("The employee has been added successfully!")
print()

tax = employee_salary * 0.1
bouns = employee_salary * 0.15
net_salary = employee_salary - tax + bouns

print("The employee has the following salary information:")
print("Basic Salary: ",employee_salary)
print("Tax: ",tax)
print("Bouns: ",bouns)
print("The net salary of the employee is: ",net_salary)

#________________________________________________________________________________________________________

#Bank Account System
balance = 0
transactions = []

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    balance += amount
    transactions.append("Deposited: " + str(amount))
    print("Deposit successful!\n")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful!\n")
    else:
        print("Insufficient balance!\n")

def check_balance():
    print("\nCurrent Balance:", balance)
    print()

def transaction_history():
    print("\n===== Transaction History =====")
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for transaction in transactions:
            print(transaction)
    print("Current Balance:", balance)
    print()

def menu():
    while True:
        print("===== Bank Account System =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you for using our bank system!")
            break
        else:
            print("Invalid choice!\n")
menu()

#_______________________________________________________________________________________________________

#Hospital Patient System
patients = {}
def add_patient(patients):
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    disease = input("Enter disease: ")
    doctor = input("Enter doctor name: ")
    patients[name] = {"Age": age,"Disease": disease,"Doctor": doctor}
    print("Patient added.")

def search_patient(patients):
    name = input("Enter patient name: ")
    if name in patients:
        print("Name:", name)
        print("Age:", patients[name]["Age"])
        print("Disease:", patients[name]["Disease"])
        print("Doctor:", patients[name]["Doctor"])
    else:
        print("Patient not found.")

def delete_patient(patients):
    name = input("Enter patient name: ")
    if name in patients:
        del patients[name]
        print("Patient deleted.")
    else:
        print("Patient not found.")

def display_patients(patients):
    if len(patients) == 0:
        print("No patients.")
    else:
        for name in patients:
            print("Name:", name)
            print("Age:", patients[name]["Age"])
            print("Disease:", patients[name]["Disease"])
            print("Doctor:", patients[name]["Doctor"])

while True:
    print("\nHospital Patient System")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Delete Patient")
    print("4. Display All Patients")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_patient(patients)
    elif choice == "2":
        search_patient(patients)
    elif choice == "3":
        delete_patient(patients)
    elif choice == "4":
        display_patients(patients)
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")