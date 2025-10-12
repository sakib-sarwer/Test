# Swap two numbers without a third variable (using arithmetic)

# Solution

number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))

number1 = number1+number2
number2 = number1-number2
number1 = number1-number2

print(f"The value of first number is changed to:  {number1}")
print(f"The value of second number is changed to:  {number2}")