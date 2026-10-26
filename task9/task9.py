# Multi-Currency Travel Budget Analysis

print("=" * 70)
print("          MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("=" * 70)

# Base Currency
base_currency = input("Enter Base Currency (e.g., INR): ").upper()

# Travel Budget
budget = float(input(f"Enter Travel Budget in {base_currency}: "))

# Conversion Fee Percentage
conversion_fee_percent = float(
    input("Enter Currency Conversion Fee (%): ")
)

# Number of Expense Categories
num_categories = int(
    input("Enter Number of Expense Categories: ")
)

expenses = {}

total_expense = 0

for i in range(num_categories):

    print(f"\nExpense Category {i + 1}")

    category = input("Category Name: ")

    amount = float(input("Expense Amount: "))

    currency = input("Currency (USD/EUR/GBP/etc.): ").upper()

    exchange_rate = float(
        input(
            f"Exchange Rate (1 {currency} = ? {base_currency}): "
        )
    )

    # Conversion
    converted_amount = amount * exchange_rate

    # Conversion Fee
    conversion_fee = (
        converted_amount * conversion_fee_percent / 100
    )

    final_amount = converted_amount + conversion_fee

    expenses[category] = final_amount

    total_expense += final_amount

# Budget Analysis
difference = budget - total_expense

# Largest Expense Category
largest_category = max(expenses, key=expenses.get)
largest_amount = expenses[largest_category]

# Report
print("\n")
print("=" * 70)
print("                TRAVEL EXPENSE REPORT")
print("=" * 70)

print(f"{'Category':<25}{'Expense (' + base_currency + ')'}")
print("-" * 70)

for category, amount in expenses.items():
    print(f"{category:<25}{amount:,.2f}")

print("-" * 70)

print(f"Total Expenses        : {base_currency} {total_expense:,.2f}")
print(f"Travel Budget         : {base_currency} {budget:,.2f}")

if total_expense <= budget:
    print(f"Budget Status         : Within Budget ✅")
    print(f"Amount Remaining      : {base_currency} {difference:,.2f}")
else:
    print(f"Budget Status         : Over Budget ❌")
    print(f"Amount Exceeded       : {base_currency} {abs(difference):,.2f}")

print("\nLARGEST EXPENSE CATEGORY")
print("-" * 70)
print(f"Category              : {largest_category}")
print(f"Amount                : {base_currency} {largest_amount:,.2f}")

print("=" * 70)