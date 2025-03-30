import calendar
from typing import List
from expense import Expense
from datetime import datetime
import csv


def main():
    expense_path = "expense.csv"
    budget = 2000

    # Get user Input expense
    expense = get_user_expense()

    # Write user expense
    save_user_expense(expense, expense_path)

    # Read file and Summarize user expense
    summarize_user_expense(expense_path, budget)


def get_user_expense():
    expense_name = input("Enter the name of expense: ").strip()
    try:
        expense_amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return get_user_expense()

    expense_categories = [
        "😋 Food",
        "🥛 Beverage",
        "🏡 Home",
        "🏢 Work",
        "😂 Fun",
        "🎧 Music"
    ]

    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_categories, start=1):
            print(f"{i}. {category_name}")
        try:
            selected_index = int(
                input(f"Select category [1-{len(expense_categories)}]: ")) - 1
            if 0 <= selected_index < len(expense_categories):
                selected_category = expense_categories[selected_index]
                return Expense(name=expense_name, category=selected_category, amount=expense_amount)
        except (ValueError, IndexError):
            print("Invalid selection. Please try again.")


def save_user_expense(expense: Expense, expense_path):
    print(f"Saving expense: {expense}")
    try:
        with open(expense_path, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([expense.name, expense.category, expense.amount])
    except Exception as e:
        print(f"Error saving expense: {e}")


def summarize_user_expense(expense_path, budget):
    expenses: List[Expense] = []

    try:
        with open(expense_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    try:
                        expense_name = row[0].strip()
                        expense_category = row[1].strip()
                        expense_amount = float(row[2])
                        expenses.append(
                            Expense(expense_name, expense_category, expense_amount))
                    except ValueError:
                        print(f"Skipping row with invalid amount: {row}")
                else:
                    print(f"Skipping malformed row: {row}")
    except FileNotFoundError:
        print(f"No expense file found at {expense_path}.")
        return
    except Exception as e:
        print(f"Error reading expenses: {e}")
        return

    # Summarize expenses by category
    amount_by_category = {}
    for expense in expenses:
        amount_by_category[expense.category] = amount_by_category.get(
            expense.category, 0) + expense.amount

    print("Expense Summary by Category:")
    for category, amount in amount_by_category.items():
        print(f"{category}: LKR {amount:.2f}")

    total_spent = sum(exp.amount for exp in expenses)
    print(f"You have spent LKR {total_spent:.2f} this month.")

    remaining_budget = budget - total_spent
    print(f"Budget Remaining: LKR {remaining_budget:.2f} this month.")

    today = datetime.today()
    _, days_in_month = calendar.monthrange(today.year, today.month)
    remaining_days = days_in_month - today.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(f"Remaining Days in Month: {remaining_days}")
        print(f"Daily Budget: LKR {daily_budget:.2f}")
    else:
        print("No remaining days in the current month.")


if __name__ == "__main__":
    main()
