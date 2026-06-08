# write a program that takes total bill amount and number of people and calculate the amount each person has to pay
total_bill = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))
amount_per_person = total_bill / number_of_people
print("Each person has to pay: ", amount_per_person)
