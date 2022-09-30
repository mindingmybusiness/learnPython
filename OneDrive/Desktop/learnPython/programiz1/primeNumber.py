number = (int)(input("Please enter a number").strip())
flag = False

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            flag = True
            break
if(flag):
    print("%d is a not prime number"%(number))
else:
    print("%d is a prime number"%(number))
