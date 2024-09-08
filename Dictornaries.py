numbers = [10, 50, 30, 20, 40]
first = second = 0

for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print("Second largest element:", second)
