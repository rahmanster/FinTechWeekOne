# print("Hello World")
# print("What's up?")

# #Datatypes
# #anything between quotes is a string
# print("There is no mistake here.")

# #integers/numbers
# print(7)
# print(7 + 9)
# print(7+9)

# print(4-8) #-4
# print(3*3) #9
# print(25/5) #5
# print(25/6) #4.something
# print(4**2) #16

# print(23%4) #3

# #functions and methods
# name = "John Jacob Jingleheimer Schmidt"
# print(name)

# print("Hello" + str(4))
# print(int("4"))

#Inputs!
# firstName = "Tamim"
# lastName = input("What is your last name?\n")
# print("Hello "+firstName+" "+lastName.lower().capitalize()+"!")
# print("Hello "+firstName[0:1]+lastName[0:1].upper())

# age = input("What is your age?\n")
# ageNow = int(age)
# ageInThree = int(age)+3
# print("You will be "+str(ageInThree)+" in three years.")
# if ageInThree >= 21:
#     print("You can drink in three years.")
# else:
#     print("You cannot drink in three years.")
# ageTillSixtyFive = 65-int(age)
# ageYear = 2019+ageTillSixtyFive
# print("You will be 65 on "+str(ageYear)+".")
#ControlFlow
try:
    number = int(input("What's your favorite number?\n"))
    if number%2 == 0:
        print("Your number is even!\n")
    else:
        print("Your number is odd!\n")
except:
    print("Please enter a numerical value.")
    number = int(input("What's your favorite number?\n"))
    if number%2 == 0:
        print("Your number is even!\n")
    else:
        print("Your number is odd!\n")
    
#For Loops!
favAnimal = "Ostriches"
for i in range(0,len(favAnimal)):
    if i == 0:
        print("The 1st letter is "+favAnimal[i])
    elif i == 1:
        print("The 2nd letter is "+favAnimal[i])
    elif i ==2:
        print("The 3rd letter is "+favAnimal[i])
    else:
        print("The "+str(i+1)+"th letter is "+favAnimal[i])
print("")

userAge = int(input("What is your age?\n"))
nextAge = userAge+1;
if nextAge >= 18:
    if nextAge == 18:
        month = int(input("What month is your birthday in 2020?"))
        if month >= 11:
            print("You can vote in the 2020 election!")
        else:
            print("You can't vote yet :(.")
    else:
        print("You can vote in the 2020 election!")
else:
    print("You cannot vote yet :(.\n")
    


    

