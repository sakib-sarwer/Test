# Check if a number is divisible by both 3 and 5 (print a boolean)

#Solution

num = int(input("Enter a number: "))

is_divisible = (num % 3 == 0) and (num % 5 == 0)

print(is_divisible)
