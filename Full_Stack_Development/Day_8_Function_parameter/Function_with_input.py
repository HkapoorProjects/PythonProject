# # TODO-1 Create a Function called greet(), write 3 print statements include the function.
# #  Call the greet() function and run your code.
#
#
# def greet():
#     print("Hello  Harshil Kapoor.")
#     print("Python programming is awesome.")
#     print("Python is future.")
#
#
# greet()


# def life_in_weeks(age):
#     Weeks_remaining = (90 - age) * 52
#     print(f"You have {Weeks_remaining} weeks left.")
#
#
# life_in_weeks(56)


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
#
# greet_with(location="Harshil", name="varanasi")


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
#
# greet_with("Harshil", "Varanasi")
# greet_with(location="Jammu", name="Razia")

name1 = input("Enter first name").upper()
name2 = input("Enter second name").upper()
Final_name = name1 + name2
print(Final_name)
print(len(Final_name))
count = 0
for letter in "TRUE":
    count += Final_name.count(letter)
print(count)
