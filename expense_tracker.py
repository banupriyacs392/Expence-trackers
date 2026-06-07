import csv
import os
from datetime import date

FILE = "expenses.csv"

def initialize():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Description", "Amount"])

def add_expense():
    category = input("Category (Food/Travel/Shopping/Other): ")
    description = input("Description: ")
    amount = input("Amount (Rs): ")
    today = date.today()
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([today, category, description, amount])
    print("Expense added successfully.")

def view_expenses():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if len(rows) <= 1:
        print("No expenses found.")
        return
    print("\n{:<12} {:<12} {:<20} {}".format("Date", "Category", "Description", "Amount"))
    print("-" * 55)
    total = 0
    for row in rows[1:]:
        print("{:<12} {:<12} {:<20} Rs.{}".format(row[0], row[1], row[2], row[3]))
        total += float(row[3])
    print("-" * 55)
    print("Total Spent: Rs.{}".format(total))

def delete_expense():
    view_expenses()
    try:
        line = int(input("\nEnter row number to delete (1 = first expense): "))
        with open(FILE, "r") as f:
            rows = list(csv.reader(f))
        if line < 1 or line >= len(rows):
            print("Invalid row number.")
            return
        rows.pop(line)
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print("Expense deleted.")
    except ValueError:
        print("Enter a valid number.")

def main():
    initialize()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose (1-4): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
