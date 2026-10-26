# Progressive Electricity Billing System

print("=" * 70)
print("           PROGRESSIVE ELECTRICITY BILLING")
print("=" * 70)

# Constants
FIXED_CHARGE = 100
SURCHARGE_RATE = 0.10      # 10%
REBATE_RATE = 0.05         # 5%

monthly_bills = []

# Number of months
months = int(input("Enter number of months to analyze: "))

for i in range(months):

    print(f"\nMonth {i + 1}")
    units = int(input("Enter electricity consumption (units): "))

    energy_charge = 0

    # Progressive Slab Calculation
    if units <= 100:
        energy_charge = units * 1.5

    elif units <= 300:
        energy_charge = (100 * 1.5) + ((units - 100) * 2.5)

    elif units <= 500:
        energy_charge = (100 * 1.5) + (200 * 2.5) + ((units - 300) * 4)

    else:
        energy_charge = (
            (100 * 1.5) +
            (200 * 2.5) +
            (200 * 4) +
            ((units - 500) * 6)
        )

    bill = energy_charge + FIXED_CHARGE

    # Rebate for low usage
    rebate = 0
    if units < 100:
        rebate = bill * REBATE_RATE
        bill -= rebate

    # Surcharge for high usage
    surcharge = 0
    if units > 500:
        surcharge = bill * SURCHARGE_RATE
        bill += surcharge

    monthly_bills.append(bill)

    print("\nBill Details")
    print("-" * 40)
    print(f"Units Consumed : {units}")
    print(f"Energy Charge  : ₹{energy_charge:.2f}")
    print(f"Fixed Charge   : ₹{FIXED_CHARGE:.2f}")
    print(f"Rebate         : ₹{rebate:.2f}")
    print(f"Surcharge      : ₹{surcharge:.2f}")
    print(f"Final Bill     : ₹{bill:.2f}")

# Bill Comparison
print("\n" + "=" * 70)
print("                MONTHLY BILL COMPARISON")
print("=" * 70)

for i in range(months):
    print(f"Month {i + 1}: ₹{monthly_bills[i]:.2f}")

# Identify Unusual Increase
print("\n" + "=" * 70)
print("               UNUSUAL INCREASE ANALYSIS")
print("=" * 70)

for i in range(1, len(monthly_bills)):

    previous = monthly_bills[i - 1]
    current = monthly_bills[i]

    increase_percent = ((current - previous) / previous) * 100

    print(f"\nMonth {i} → Month {i+1}")
    print(f"Change: {increase_percent:.2f}%")

    if increase_percent > 25:
        print("⚠ Unusual increase detected!")
    else:
        print("Normal variation.")

# Summary
highest_bill = max(monthly_bills)
lowest_bill = min(monthly_bills)
average_bill = sum(monthly_bills) / len(monthly_bills)

print("\n" + "=" * 70)
print("                     BILL SUMMARY")
print("=" * 70)
print(f"Highest Bill : ₹{highest_bill:.2f}")
print(f"Lowest Bill  : ₹{lowest_bill:.2f}")
print(f"Average  : ₹{average_bill:.2f}")
print("=" * 70)