check = False
while check == False:
    print ("Welcome to America's Travel Guide")
    name = input("what is your name?").split() 
    age = int (input("Enter your age:"))
    
    if age < 18:
        print("You can not go on a trip.")   
        print("You a are too young") 
        print("Sorry kiddo :(")  
   
    if age > 17:
        gender = input("Enter your gender: ")
        print (f"Welcome{name}")
        print(f"You are {age} years old and you're gender is {gender} and you're current location is Towson, Maryland")
        confirmation = input("Is this correct? (yes/no): ").strip().lower()
        
        if confirmation == "yes":
            print("Thank you for confirming your details.") 
            print("Lets find you a place to travel too!")
            check = True
        else:
            print("Please restart the program to enter your details again.")
    
 
    
money = input("Enter the amount of money you are willing to spend: ")
money = float(money)

if money < 500:
    print("You can not afford to go on a trip.")
    print("sorry")
    
elif money >= 500 and money < 1000:
    print("You can go on a local trip.")
    print('Here is a list of Local States you can travel too')
    file = open ("Local States.txt","r")
    LocalStates = file.readlines()
    file.close()
    
    
    for i in range(len(LocalStates)):
        LocalStates[i] = LocalStates[i].strip().lower()
    print(LocalStates)
    pick = input("Pick a Local State you would like to Travel too!:").strip().lower()
    
    if pick == "Delaware".strip().lower():
        print("Here is a list of things to do while you are here!")
        file = open ("Delaware.txt","r")
        Delaware = file.readlines()
        print(Delaware)
        
        activity = input("What would you like to do?").strip()
        if activity =="Relax at Rehoboth Beach":
            print("awesome!")
        
        if activity =="Walk the Riverfront in Wilmington":
            print("awesome!")
        
        if activity =="Visit Cape Henlopen State Park":
            print("awesome!")   
        
    
    if pick == "Virginia".strip().lower():
            print("Here is a list of things to do while you are here!")
            file = open ("Virginia.txt","r")
            Virginia = file.readlines()
            print(Virginia)
   
   
   
            activity1 = input("What would you like to do?").strip()
            if activity1 =="Tour historic Colonial Williamsburg":
                print("awesome!")
            
            if activity1 =="Hike Shenandoah National Park":
                print("awesome!")
            
            if activity1 =="Visit the Smithsonian museums in Northern Virginia":
                print("awesome!")
            
            
            
            
    if pick == "Maryland".strip().lower():
            print("Here is a list of things to do while you are here!")
            file = open ("Maryland.txt","r")
            Maryland = file.readlines()
            print(Maryland)
            activity2 = input("What would you like to do?").strip()
            if activity2 =="Visit the Inner Harbor in Baltimore":
                print("awesome!")
            
            if activity2 =="Explore Assateague Island and see the wild horses":
                print("awesome!")
            
            if activity2 =="Tour the National Aquarium":
                print("awesome!") 
            



""""
list_of_items = []
for i in range(3):
    item = input("Enter an item to pack for your trip: ")
    list_of_items.append(item)
print("You have packed the following items for your trip:")
for item in list_of_items: 
    print(f"- {item}")
""""""""""""""""""

"file.close()"""""""""
