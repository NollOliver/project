print ("Welcome to Americas Travel Guide")
name = input("what is your name?")
print (f"Welcome{name} lets find you a place to travel too!")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
print(f"You are {age} years old and your gender is {gender}.")      
confirmation = input("Is this correct? (yes/no): ").strip().lower()
if confirmation == "yes":
    print("Thank you for confirming your details.") 
else:
    print("Please restart the program to enter your details again.")
    
print("First lets start off with what you are looking for!")
print("Please fill this question sheet with what you would like to find in your destination")
climate  = input("What climate type are you looking for?")






money = input("Enter the amount of money you are willing to spend: ")
money = float(money)
if money < 10:
    print("You can not afford to go on a trip.")
elif money >= 10 and money < 100:
    print("You can go on a local trip.")
elif money >= 100 and money < 1000:
    print("You can go on a domestic trip.")
elif money >= 1000:
    print("You can go on an international trip.")
destination = input("Enter your desired travel destination: ")
print(f"You have chosen to travel to {destination}. Enjoy your trip!")