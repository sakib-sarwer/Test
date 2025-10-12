# Calculate simple interest: SI = (P * R * T) / 100

# Solution

P = float(input("enter the principal amount: "))
R = float(input("enter the rate of interest: "))
T = float(input("enter the time in years: "))

SI = (P*R*T)/100

print(f"The simple interest is:  {SI}")