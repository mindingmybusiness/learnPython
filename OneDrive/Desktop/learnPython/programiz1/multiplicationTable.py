number = (int)(input("Please enter a number: ").strip())

for i in range(1,11):
    print("%d * %d = %d"%(number,i,number*i))