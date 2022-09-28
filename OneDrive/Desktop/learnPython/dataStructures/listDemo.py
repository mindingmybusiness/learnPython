our_list = [34,321,342,564,76]
print(our_list)
print(type(our_list))

test = ["A","B",1,2,"Test", True, False]
print(test)
print(test[6])
print(test[-2])

#slicing a list
#list[start:end:step]

store = test[2:5:1]
print(store)

#Lists can have other lists inside the list
test_list = [1,2,3,[4,5,6],[7,8],9,10]
print(test_list[3])
print(test_list[3][2]) #prints 6
print(test_list[3][0::2])
del test_list[0]
print(test_list)


#adding an element in the list
test_list = test_list + [[5,6,4,3,2]]
print(test_list)

test_list.insert(3, 'A')
print(test_list)
