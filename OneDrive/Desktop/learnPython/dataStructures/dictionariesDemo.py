#it can be looked up using keys

students = {"Alice":25, "Bob":20, "Clarie" : 34, "Dan": 29}
students["Fred"] = 25
students["Alice"] = 26
print(students)

del students["Fred"]
print(students)

print(students.keys())
#when we convert the keys to list we can index it

list1 = list(students.keys())
print(list1[3])

values1 = list(students.values())
print(values1[0:4:1])

