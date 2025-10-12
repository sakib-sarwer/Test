# Calculate distance between two points (x1,y1) and (x2,y2): √((x2-x1)² + (y2-y1)²)

# Solution

import math

x1 = float(input("Please enter the value of x1 "))
y1 = float(input("Please enter the value of y1 "))
x2 = float(input("Please enter the value of x2 "))
y2 = float(input("Please enter the value of y2 "))

distance = round(math.hypot(x2 - x1, y2 - y1), 2)
print("Distance between points:", distance)