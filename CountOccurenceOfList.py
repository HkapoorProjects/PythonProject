# mylist = [15, 6, 7, 10, 23, 33, 10.38, 10]
# x = 10
# output = 3
# 10 appear in 3 times


# using loop

# mylist = [15, 6, 7, 10, 23, 33, 10, 38, 10]
# x = 10
# count = 0
# for ele in mylist:
#     if ele == x:
#         count += 1
# print("{} has occurred {} times".format(x, count))


# using count method

# mylist = [15, 6, 7, 10, 23, 33, 10, 38, 10]
# x = 10
# print("{} has occurred {} times".format(x, mylist.count(x)))


# using counter()
from collections import Counter

mylist = [15, 6, 7, 10, 23, 33, 10, 38, 10]
x = 10
dic = Counter(mylist)
print("{} has occurred {} times".format(x, dic[x]))
