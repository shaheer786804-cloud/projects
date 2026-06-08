# Expense tracker project
expenses = [] # list of all expenses in form of dictionaries
print("Welcome to the Expense Tracker!")
while True:
    print("\nPlease select an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total amount of expenses")
    print("4. Exit")

    choice = input("Enter your choice:") 
    if choice == "1":
        name = input("Enter the name of the expense: ")
        amount = float(input("Enter the amount of the expense: "))
        category = input("Enter the category of the expense: ")


        expense = {"name": name,
                    "amount": amount, 
                    "category": category}
        

        expenses.append(expense)
        print("\n Expense added successfully!")


    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses to show.")
        else:
            print("\nAll expenses:")
            for i in expenses:
                print(expenses.index(i)+1, ". ", i["name"], ": $", i["amount"], " (", i["category"], ")")

                
    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print("\nTotal amount of expenses: $", total)

    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")