# Progressive Electricity Billing System

FIXED_CHARGE = 100          # Fixed monthly charge
SURCHARGE_RATE = 0.05       # 5% surcharge
REBATE_RATE = 0.10          # 10% rebate for low consumption

# Function to calculate energy charge based on slabs
def calculate_energy_charge(units):
    bill = 0

    if units <= 100:
        bill = units * 1.5

    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)

    elif units <= 500:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

    else:
        bill = (100 * 1.5) + (100 * 2.5) + (300 * 4) + ((units - 500) * 6)

    return bill


# Function to calculate total bill
def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    subtotal = energy_charge + FIXED_CHARGE

    # Apply surcharge for heavy usage
    surcharge = 0
    if units > 500:
        surcharge = subtotal * SURCHARGE_RATE

    # Apply rebate for low usage
    rebate = 0
    if units < 100:
        rebate = subtotal * REBATE_RATE

    total_bill = subtotal + surcharge - rebate

    return round(total_bill, 2)


# Monthly consumption data
monthly_units = {
    "January": 180,
    "February": 195,
    "March": 220,
    "April": 260,
    "May": 450,
    "June": 600
}

# Calculate bills
monthly_bills = {}

print("Electricity Bill Report")
print("-" * 50)

for month, units in monthly_units.items():
    bill = calculate_bill(units)
    monthly_bills[month] = bill

    print(f"{month:<10} Units: {units:<5} Bill: ₹{bill}")

print("\nBill Comparison and Increase Analysis")
print("-" * 50)

months = list(monthly_bills.keys())

for i in range(1, len(months)):
    previous_bill = monthly_bills[months[i - 1]]
    current_bill = monthly_bills