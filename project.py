age = input("Enter your age: ")
gender = input("Enter your gender: ")
print(f"You are {age} years old and your gender is {gender}.")      
confirmation = input("Is this correct? (yes/no): ").strip().lower()
if confirmation == "yes":
    print("Thank you for confirming your details.") 
else:
    print("Please restart the program to enter your details again.")
    money = input("Enter the amount of money you are willing to spend: ")
money = float(money)
if money < 10:
    print("You can not afford to go on a trip.")
elif money >= 10 and money < 100:
    print("You can go on a local trip.")
elif money >= 100 and money < 5000:
    print("You can go on a domestic trip.")
destination = input("Enter your desired travel destination: ")
print(f"You have chosen to travel to {destination}. Enjoy your trip!")
list_of_items = []
for i in range(3):
    item = input("Enter an item to pack for your trip: ")
    list_of_items.append(item)
print("You have packed the following items for your trip:")
for item in list_of_items: 
    print(f"- {item}")
    


print("Here is a list of all 50 U.S. states:")
file = open ("states.txt","r")
States = file.readlines()

file.close()
for i in range(len(States)):
    States[i] = States[i].strip
pick = input("Pick a state between 1 and 50: ")