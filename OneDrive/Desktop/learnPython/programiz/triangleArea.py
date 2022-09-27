#The area of a triangle if sides a, b, c are
#s = (a+b+c)/2
#area = Sqrt((s(s-a)*(s-b)*(s-c)))

side1 = (int)(input("Please enter the length of side 1 in cms"))
side2 = (int)(input("Please enter the length of side 2 in cms"))
side3 = (int)(input("Please enter the length of side 3 in cms"))

s = (side1+side2+side3)/2

area = ((s*(s-side1)*(s-side2)*(s-side3)))** 0.5
print(area)