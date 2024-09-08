print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
temp = 0
temp_2 = 0
final_name = name1.upper() + name2.upper()
T = final_name.count("T")
R = final_name.count("R")
U = final_name.count("U")
E = final_name.count("E")
first_digit = T + R + U + E
L = final_name.count("L")
O = final_name.count("O")
V = final_name.count("V")
E = final_name.count("E")
second_digit = L + O + V + E
Love_Score = int(str(first_digit) + str(second_digit))
if (Love_Score < 10) and (Love_Score > 90):
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif (Love_Score < 40) and (Love_Score <= 50):
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"You score is {Love_Score}.")
