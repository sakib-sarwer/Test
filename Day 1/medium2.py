# Find the remainder when dividing two numbers

# Solution


dividend = float(input("please enter the dividend: "))
divisor = float(input("please enter the divisor: "))
quotient = int((dividend/divisor))
remainder = dividend - (divisor*quotient)

print(f"the remainder is:  {remainder}")