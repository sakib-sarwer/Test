# Reverse a 3-digit number (e.g., 123 → 321)

# Solution

number = int(input("Please enter a three digit number "))

reverse_number = int(str(number)[::-1])
print(reverse_number)
