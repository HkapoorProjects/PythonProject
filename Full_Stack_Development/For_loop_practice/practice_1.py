# Write a for loop to iterate over the numbers 1 through 10 and print whether each number is even or odd.

for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
