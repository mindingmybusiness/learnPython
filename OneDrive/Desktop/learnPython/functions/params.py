#the function has default argument
def about(name, age, likes = "python"):
    sentence = "Meet {}! They are {} years old and likes {}".format(name, age, likes)
    return sentence

test = about("shubha",32,"python")
print(test)

test1 = about("Shubha", 32)
print(test1)