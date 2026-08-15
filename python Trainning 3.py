                                    #Student dictionary
student = { "name": "Ahmed Ali", "age": 20, 
            "department": "computer science", "gpa": "3.5",
                "courses": ["Python", "Database", "AI"] 
                }
                                    #print name & gpa
print("Student name     :   " + student["name"])
print("GPA              :   " + student["gpa"])
                                    #Modifications
student.update({"gpa": 3.9})
student["level"]= 3
student["courses"].append("Machine Learning")
print(student.keys())
print(student.values())
                                    #Copying informations
student2 = student.copy()
student2["name"] = "Mohamed Ali"
                                    #printing both students
print("First student    :   ", student)
print("Second Student   :   ", student2)
                                    #Modification2
student.pop("level")
student2.pop("level")
                                    #Printing final dictionaries
print("First student    :   ", student)
print("Second Student   :   ", student2)
#--------------------------------------------------------------------------------------------------------------------------------------------
                            #Colors set
colors = {"Red", "Blue", "Green", "Yellow"}
print(colors)
colors.add("Black")
colors.add("White")
colors.remove("Green")
print("Blue" in colors)
print("The set length       :   ", len(colors))
                           #Task 2 in sets
newColors = {"Blue", "Pink", "Orange"}
print("All colors           :   ", colors.union(newColors))
print("The intersection     :   " , colors.intersection(newColors))
print("The diffrence        :   ", colors.difference(newColors))
                            #Task 3 in sets
studentIDS = {101, 102, 103, 104, 105}
studentIDS.add(106)
studentIDS.remove(103)
print(101 in studentIDS)
print(studentIDS)
print(len(studentIDS))
                             #Task 4 in sets
newIDS = {104, 105, 106, 107}
print("Common IDS           :   ", studentIDS.intersection(newIDS))
print("All IDS              :   ", studentIDS.union(newIDS))
print("IDS only in the first:   ", studentIDS.difference(newIDS))
newIDS.clear()








                        

 


