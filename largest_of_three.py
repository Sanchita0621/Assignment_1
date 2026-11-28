# Program to find the largest of three numbers

# Take input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Compare the numbers using if-elif-else
if a == b == c:
  print("All numbers are equal")
elif a >= b and a >= c:
  print("a is greatest")
elif b >= a and b >= c:
  print("b is greatest")
else:
  print("c is greatest")
