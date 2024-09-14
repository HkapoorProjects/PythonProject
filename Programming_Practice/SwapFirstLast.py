a = [12, 35, 9, 56, 24]
# b = [24, 35, 9, 56, 12]

# Approach 1
# size = len(a)
# temp = a[0]
# a[0] = a[size - 1]
# a[size - 1] = temp
#
# print(a)


# Approach 2

# a[0], a[-1] = a[-1], a[0]
# print(a)


# Approach 3 using tuple
#
# get = (a[-1], a[0])
# a[0], a[-1] = get
# print(a)


# Approach 4 * operand
# start, *middle, end = a
# a = [end, *middle, start]
# print(a)


# Approach 5 using pop()

first = a.pop(0)
last = a.pop(-1)
a.insert(0, last)
a.append(first)
print(a)
