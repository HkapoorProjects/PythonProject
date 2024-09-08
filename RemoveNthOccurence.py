# input = ["geeks", "for", "geeks"]
# word = geeks,N = 2
# output = ["geeks", "for"]
mylist = ["geeks", "for", "geeks"]
word = "geeks"
n = 2
count = 0

for i in range(0, len(mylist)):
    if mylist[i] == word:
        count += 1
        if count == n:
            del mylist[i]
print(mylist)
