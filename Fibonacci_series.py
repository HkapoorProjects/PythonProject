# 0 1 1 2 3 5 8 13 21 34

num_1 = 0
num_2 = 1

for i in range(2, 10):
    sum = num_1 + num_2
    print(sum)
    num_1 = num_2
    num_2 = sum
