import os
import json
from datetime import datetime

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            return json.load(file)
    else:
        return {"expenses": []}

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)

def add_expense(expenses, amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expense = {"date": date, "amount": amount, "category": category, "description": description}
    expenses["expenses"].append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def display_expenses(expenses):
    if not expenses["expenses"]:
        print("No expenses found.")
    else:
        for index, expense in enumerate(expenses["expenses"], start=1):
            print(f"{index}. Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def view_spending_pattern(expenses):
    total_spent = sum(expense['amount'] for expense in expenses["expenses"])
    print(f"Total amount spent: {total_spent}")

    # You can add more analysis or visualization of spending patterns here based on your needs.

def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Pattern")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            description = input("Enter a description (optional): ")
            add_expense(expenses, amount, category, description)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            view_spending_pattern(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
