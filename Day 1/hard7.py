# Calculate compound interest: A = P(1 + r/100)^t

# Solution

P = float(input("Please enter the amount of principal: "))
r = float(input("Please enter the rate of interest :"))
t = float(input("Please enter the amount of time in year: "))

A = P*(1 + r/100)**t

CI = A-P

print(f'The compound interest is {CI}')