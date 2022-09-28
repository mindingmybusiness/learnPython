known_users = ["Alice","Bob","Claire","Toad","Fred","Harry"]
print(len(known_users))

while True:
    print("Hi, My name is Travis")
    name = input("Please enter your name: ").strip().capitalize()
    if name in known_users:
        print("Hello {} recognized".format(name))
        remove = input("Would you like to be Removed from the system? y/n: ").lower()
        if(remove == 'y'):
            known_users.remove(name)  
        elif(remove == 'n'):
            print("No problem, I didn't want you to leave anyway")

    else:
        print("Hmmm... I don't think I have met you yet {}".format(name))   
        add_me = input("Would you like to be added to the system? y/n").strip().lower()
        if(add_me == 'y'):
            known_users.append(name)
        elif(add_me == 'n'):
            print("No worries, see you around..")
