initial_balance = float(input("Enter your initial balance: ₹"))
balance = initial_balance
income = {}
expenses = {}

while True:
    print("\n--- Budget Manager Menu ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Display Final Budget")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        category = input("Enter income category: ")
        amount = float(input("Enter income amount: ₹"))
        if category in income:
            income[category] += amount
        else:
            income[category] = amount
        balance += amount
    elif choice == '2':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: ₹"))
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        balance -= amount
    elif choice == '3':
        print("\n--- Budget Final Budget ---")
        print(f"Starting Balance: ₹{initial_balance:.2f}")
        print("\nIncome:")
        for category, amount in income.items():
            print(f"{category}: ₹{amount:.2f}")
        print("\nExpenses:")
        for category, amount in expenses.items():
            print(f"{category}: ₹{amount:.2f}")
        print("\nFinal Remaining Balance: ₹{:.2f}".format(balance))
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
print("\n--- End ---")
