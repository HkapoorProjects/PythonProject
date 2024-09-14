str = "Welcome to python programming"
words = str.split(" ")
print(words)
revstr = words[-1::-1]
print(revstr)
final = " ".join(revstr)
print(final)
