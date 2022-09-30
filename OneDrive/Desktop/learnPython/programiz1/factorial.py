num = (int)(input("Please enter a number: ").strip())

print(" factorial of %d is: "%num)
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    
print(factorial)
