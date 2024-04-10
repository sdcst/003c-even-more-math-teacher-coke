#!python3

# Heron's formula is a method of finding the area of a any triangle if you know the lengths of 3 sides.

'''
write a program to calculate the area of a triangle provided the 3 sides are known:
sample:
I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 3
Enter the length of side b: 5
Enter the length of side c: 7

Your half perimeter is 7.5
The area of your triangle is 6.495





I will use Heron's formula to find the area of a triangle provided that all 3 sides are known.
You will need to enter the lengths of the 3 sides: a, b and c

Enter the length of side a: 5
Enter the length of side b: 12
Enter the length of side c: 12

Your half perimeter is 14.5
The area of your triangle is 29.342
'''

a = float(input("Enter of a side a: "))
b = float(input("Enter of a side b: "))
c = float(input("Enter of a side c: "))
s = (a+b+c)/2
s = round(s, 2)
A = (s*(s-a)*(s-b)*(s-c))**0.5
A = round(A, 3)
print(f"Your half perimeter is {s}")
print(f"The area of your triangle is {A}")
