# input: arr[] = {10, 20, 30}
# output: 30
# output = 10

arr = [1, 2, 3, 4, 5, 6]
max = arr[0]

for i in arr:
    if i > max:
        max = i
print(max)
