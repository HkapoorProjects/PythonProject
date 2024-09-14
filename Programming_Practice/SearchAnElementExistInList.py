mylist = [1, 3, 5, 7, 4, 9]
ele = 6
flag = 0

# for i in mylist:
#     if i == ele:
#         print("Element found")
#         flag = 1
#         break
# if flag == 0:
#     print("ELmeent not found")

# Approach 2 in operator

if ele in mylist:
    print("Element is found")
else:
    print("Element not found")
