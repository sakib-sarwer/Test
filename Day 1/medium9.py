# Convert minutes to hours and minutes

# Solution

minutes = int(input("Please enter the amount of minutes "))

hours = int(minutes/60)
minutes = minutes - (hours*60)

print(f'The amount of hour is {hours} and the amount of minutes is {minutes}')