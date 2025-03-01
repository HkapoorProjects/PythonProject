marks = int(input("Enter the marks: "))
if marks >= 90:
    print("A Grade")
elif 90 > marks >= 80:
    print("B Grade")
elif 80 > marks >= 70:
    print("C Grade")
elif 70 > marks:
    print("D Grade")
else:
    print("Enter valid marks")
