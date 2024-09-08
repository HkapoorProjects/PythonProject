# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
split_among = int(input("How many people to split the bill? "))
tip_percentage = (tip / 100) + 1
result = round((bill / split_among) * tip_percentage, 2)
print(f"Each person should pay: ${result}")
