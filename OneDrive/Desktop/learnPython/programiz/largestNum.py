num1 = (int) (input("Enter num1: "))
num2 = (int) (input("Enter num2: "))
num3 = (int) (input("Enter num3: "))

if((num1> num2)and(num1>num3)):
    largest = num1;
elif((num2> num1) and (num2 > num3)):
    largest = num2;
elif((num3> num1)and (num3>num2)):
    largest = num3;

print("%d is largest of the three"%(largest))

