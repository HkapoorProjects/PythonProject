print("Welcome to the rollercoaster !!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride :) ")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
    elif 12 < age < 18:
        bill = 7
    elif 18 < age < 45:
        bill = 12
    elif 45 < age < 55:
        print("Everything is going to be ok. Have a free ride on us!")

    photo = input("You want photos? ").lower()
    if photo == "y":
        bill += 3
    print(f"You total bill is ${bill}")
else:
    print("I am sorry you can not ride")
