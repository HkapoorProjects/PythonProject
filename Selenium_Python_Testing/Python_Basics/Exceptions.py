# ItemInCart = 0
#
# # if ItemInCart != 2:
# # raise Exception("Item in the cart does not match the count")
# assert ItemInCart == 0

# Try Except block
# In python we do not have catch block instead we use Except block
# Why we use Exceptions?
# When we know the error before hand and do not want to fail the test case
# Below code is to show how this is working
# try:
#     with open("harshil_1.txt", "r") as reader:
#         reader.read()
# except:
#     print("Some how I reached to this block because there is a failure in try block")


# Now below is the correct block of code and this is why except block will not get executed
try:
    with open("harshil.txt", "r") as reader:
        print(reader.read())
except:
    print("Some how I reached to this block because there is a failure in try block")


# Above you see  we set the customised message when try get fails but what if I want the real message

try:
    with open("ghar.txt", "r") as reader:
        print(reader.read())
except Exception as e:
    print(e)

# We have another block called "Finally", whatsoever happened in try except blow finally will run

try:
    with open("tettly.txt", "r") as reader:
        print(reader.read())
except Exception as e:
    print(e)
finally:
    print("This code will run all the time")
