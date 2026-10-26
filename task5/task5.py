# Multi-Plan Telecommunications Cost Optimization

print("=" * 65)
print("      MULTI-PLAN TELECOMMUNICATIONS COST OPTIMIZER")
print("=" * 65)

# Mobile Plans Database
plans = [
    {
        "name": "Basic Plan",
        "price": 299,
        "data_limit": 20,      # GB
        "call_limit": 500,     # Minutes
        "sms_limit": 100,
        "validity": 28
    },
    {
        "name": "Standard Plan",
        "price": 499,
        "data_limit": 50,
        "call_limit": 1000,
        "sms_limit": 300,
        "validity": 56
    },
    {
        "name": "Premium Plan",
        "price": 799,
        "data_limit": 100,
        "call_limit": 2000,
        "sms_limit": 1000,
        "validity": 84
    }
]

# Excess Charges
EXTRA_DATA_RATE = 10      # ₹ per GB
EXTRA_CALL_RATE = 0.50    # ₹ per minute
EXTRA_SMS_RATE = 0.25     # ₹ per SMS

# User Requirements
print("\nEnter Monthly Usage Requirements:")

data_used = float(input("Data Usage (GB): "))
call_used = int(input("Call Usage (Minutes): "))
sms_used = int(input("SMS Usage: "))
required_validity = int(input("Required Validity (Days): "))
budget = float(input("Maximum Budget (₹): "))

print("\n" + "=" * 65)
print("PLAN ANALYSIS")
print("=" * 65)

best_plan = None
lowest_cost = float('inf')

for plan in plans:

    # Calculate excess usage
    extra_data = max(0, data_used - plan["data_limit"])
    extra_calls = max(0, call_used - plan["call_limit"])
    extra_sms = max(0, sms_used - plan["sms_limit"])

    excess_charge = (
        extra_data * EXTRA_DATA_RATE +
        extra_calls * EXTRA_CALL_RATE +
        extra_sms * EXTRA_SMS_RATE
    )

    total_cost = plan["price"] + excess_charge

    eligible = (
        plan["validity"] >= required_validity and
        total_cost <= budget
    )

    print(f"\nPlan Name       : {plan['name']}")
    print(f"Base Price      : ₹{plan['price']:.2f}")
    print(f"Validity        : {plan['validity']} Days")
    print(f"Extra Data      : {extra_data:.2f} GB")
    print(f"Extra Calls     : {extra_calls} Minutes")
    print(f"Extra SMS       : {extra_sms}")
    print(f"Excess Charges  : ₹{excess_charge:.2f}")
    print(f"Total Cost      : ₹{total_cost:.2f}")
    print("Status          :", "Eligible ✅" if eligible else "Not Eligible ❌")

    if eligible and total_cost < lowest_cost:
        lowest_cost = total_cost
        best_plan = plan["name"]

print("\n" + "=" * 65)
print("OPTIMIZATION RESULT")
print("=" * 65)

if best_plan:
    print(f"Most Economical Eligible Plan: {best_plan}")
    print(f"Total Expected Cost: ₹{lowest_cost:.2f}")
else:
    print("No plan satisfies the specified validity and budget constraints.")

print("=" * 65)