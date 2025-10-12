# Check if a number is even or odd (without if! Use boolean and print)

# Solution

number = float(input("Please enter a number "))

# True -> Even, False -> Odd
is_even = (number % 2 == 0)

# Use boolean indexing (tuple trick)
print(("Odd", "Even")[is_even])
