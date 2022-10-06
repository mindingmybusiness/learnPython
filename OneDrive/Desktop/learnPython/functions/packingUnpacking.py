#unpacking
print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)
print("abc")
print(*"abc")

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(add(9,10,8,28))


def about(name, age, likes = "python"):
    sentence = "Meet {}! They are {} years old and likes {}".format(name, age, likes)
    return sentence

dict = {"name":"test","age":23,"likes":"Python"}

print(about(**dict))

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{} , {} ".format(key, value))
        
foo(huda = "female", ziyad ="male",john="male")