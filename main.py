'''
Agam Cheema
Mar 17, 2025
2.3 D) Make Chatbot
'''

#imports


#variables
# Below, a string is being assigned to each of the variables.
name = "Agam"
favSubject = "Math"
favFood = "Blue"
favCarMake = "Mercedes"

#functions


#main code
#This stores the user's name into the variable name
name = input("Hi, what is your name")
# This is a message that mentions the name the user inputs and it uses \n to add a line break.
print("\nI hope you are doing well " + name)
#This is a way to add a space or in other words, a blank line.
print()
# This statement just tells the user what is about to happen
print("I will now ask you three questions about your personality.")
#This also adds a space.
print()
# In the three lines below, a question is being input into the three different variables; favSubject, favFood and favCarMake.
favSubject = input("What is your favourite subject in school?")
favFood = input("What is your favourite food to eat?")
favCarMake = input("What is your favourite car make?")
#This adds a blank line.
print()
# In the three lines blow, the print statement is outputing a response to each of the questions one by one, while also using the user's name that was first stored in the name variable.
# These lines also use f-string to make the spacing clear and organized.
print(f"Yes {name}, {favSubject} is an interesting subject.")
print(f"Wow {name}, {favFood} sounds delicious!")
print(f"Nice choice {name}, {favCarMake} definitely manufactures some awesome cars.")
#This line outputs a summary of all the user's answers in one sentence, it uses \n to add a line break and \t to add an indent.
print(f"\n\tThis is the personality of the user: The user's name is {name}, favourite subject is {favSubject}, favourite food is {favFood} and favourite car make is {favCarMake}.")




