films = { "finding dory": [3,5],
         "tarzan":[18,1],
         "ghost buster":[6,5],
         "bourne":[17,5]
        }

while True:
    choice = input("What film do you want to watch? : ").strip().lower()
    if choice in films:
        age = (int)(input("How old are you? ").strip())
        if age >= films[choice][0]:
            if(films[choice][1]>0):
                print("Enjoy your film")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are too young to see that film")
    else:
        print("We don't have that film")
        
