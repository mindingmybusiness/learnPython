students = {"Alice": ["001",25,"A"],
            "Bob": ["002",20,"B"], 
            "Clarie": ["003",34,"C"],
            "Dan": ["004",29,"D"],
            "Fred": ["005",25,"E"]
            }

print(students["Clarie"])
print(students["Clarie"][2])

print(students["Bob"][0:1:1])

students = {"Alice":{"id":"001", "Age":26, "grade":"A"},
            "Bob":{"id":"002", "Age":20, "grade":"B"}, 
            "Dan":{"id":"003", "Age":29, "grade":"C"},
            }

print(students["Dan"]["Age"])

print(students.get("Alice"))