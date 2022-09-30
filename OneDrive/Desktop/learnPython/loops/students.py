students = {
    "male":["Tom","Charlie","Harry", "Frank"],
    "female": ["Sarah","Huda","Samantha","Emily", "Elizebath"]
    }

for key in students.keys():
    print(students[key])
    for name in students[key]:
        if "a" in name.lower():
            print(name)