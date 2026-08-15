print("==========Student informations==========\n")

                                #NAME
name = input (          "Full name                :   " )                                  
print(                  "Upper name               :   "    + name.upper()             )
print(                  "Lower name               :   "    + name.lower()             )
print(                  "Title name               :   "    + name.title()             )
print(                  "Name length              :   "    + str(len(name))           )
print(                  "First character          :   "    + name[0]                  )
print(                  "Last character           :   "    + name[-1]                 )
print(                  "First name               :   "    + name.split()[0]          )
print(                  "Reversed name            :   "    + name[::-1]               )
print("\n")

                               #EMAIL
email = input(          "Email                    :   " )
print(                  "@ Position               :   "    + str(email.find("@"))     )
print(                  "Domain                   :   "    + str(email.split("@")[1]) )

domain = str(email.split("@")[1])
print(                  "Domain length            :   "    + str(len(domain))         )
print("\n")

                              #LANGUAGE
language =input(        "Programming language     :   ")
print(                  "Upper                    :   "    + language.upper()         )
print(                  "Lower                    :   "    + language.lower()         )
print(                  "Capitalize               :   "    + language.capitalize()    )
print("\n")

print("\n Welcome " + name +" to " + language +" programing course\n ======================================")





