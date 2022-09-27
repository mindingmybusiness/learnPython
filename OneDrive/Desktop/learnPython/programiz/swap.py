num1 = (int)(input("Input the num1 "))
num2 = (int)(input("Input the num2 "))


temp = num1
num1 = num2
num2= temp
print("Num1 is {} and num2 is {}".format(num1,num2))


num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("Num1 is {} and Num2 is {}".format(num1,num2))
