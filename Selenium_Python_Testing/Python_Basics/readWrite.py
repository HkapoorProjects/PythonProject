file = open("harshil.txt")


# another way to read a file is: in the below way we need not to close the file manually
# with open('harshil.txt', 'r') as file:


# print(file.read())  # To read the complete content of the file
# print(file.read(2))  # To read two character of the file
# print(file.readline())  # Read one single line at a time using readline() method
# print(file.readline())

# Interview Question
# Write a program to print line by line using readline method

# First Method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# Second method is to put the file text into the list and iterate
# to put all the data in the list is to use readlines() method

# print(file.readlines()) # this way is to create a list

for line in file.readlines():
    print(line)

file.close()
