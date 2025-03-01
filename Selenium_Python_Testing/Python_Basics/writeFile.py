# Read the file and store all the lines in list
# Reverse the list
# write the list back to the file


with open("harshil.txt", "r") as reader:  # To read use 'r' and to write use 'w'
    content = reader.readlines()
    reversed(content)
    with open("harshil.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)
