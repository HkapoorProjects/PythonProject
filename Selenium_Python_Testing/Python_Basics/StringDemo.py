str1 = "HarshilKapoor.com"
str2 = "SoftwareEngineer"
str3 = "Harshil"
str4 = "Harshil "  # One extra space in the end
str5 = " Harshil"  # One extra space in the beginning
print(str1[1])  # For single char
print(str1[0:7])  # For getting substring
print(str1 + " " + str2)  # For concatenating two string
print(str3 in str1)  # Finding data from str to str
var = str1.split(".")  # Splitting the string using split method
print(var)
print(var[0])  # To extract the first element of the list
print(str4.strip())  # To remove extra space
print(str5.strip())  # To remove extra space

# To specifically remove left trailing or right end space we have lstrip and rstrip method
print(str5.rstrip())
print(str5.lstrip())
