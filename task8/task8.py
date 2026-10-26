# Manufacturing Cost and Profitability Analysis

print("=" * 70)
print("     MANUFACTURING COST AND PROFITABILITY ANALYSIS")
print("=" * 70)

# Product Details
product_name = input("Enter Product Name: ")
units_produced = int(input("Enter Number of Units Produced: "))

# Cost Inputs
material_cost_per_unit = float(input("Enter Material Cost per Unit (₹): "))
labour_cost_per_unit = float(input("Enter Labour Cost per Unit (₹): "))
machine_cost = float(input("Enter Total Machine Cost (₹): "))
wastage_percentage = float(input("Enter Wastage Percentage (%): "))
selling_price_per_unit = float(input("Enter Selling Price per Unit (₹): "))

# Profit Target
profit_target = float(input("Enter Target Profit (₹): "))

# Calculations

# Material Cost
total_material_cost = material_cost_per_unit * units_produced

# Labour Cost
total_labour_cost = labour_cost_per_unit * units_produced

# Wastage Cost
wastage_cost = total_material_cost * (wastage_percentage / 100)

# Total Manufacturing Cost
total_cost = (
    total_material_cost +
    total_labour_cost +
    machine_cost +
    wastage_cost
)

# Revenue
total_revenue = selling_price_per_unit * units_produced

# Profit/Loss
profit = total_revenue - total_cost

# Profit Percentage
if total_cost > 0:
    profit_percentage = (profit / total_cost) * 100
else:
    profit_percentage = 0

# Determine Status
if profit > 0:
    status = "PROFIT"
elif profit < 0:
    status = "LOSS"
else:
    status = "BREAK-EVEN"

# Target Verification
target_status = "ACHIEVED ✅" if profit >= profit_target else "NOT ACHIEVED ❌"

# Output Report
print("\n")
print("=" * 70)
print("                MANUFACTURING REPORT")
print("=" * 70)

print(f"Product Name                : {product_name}")
print(f"Units Produced              : {units_produced}")

print("\nCOST ANALYSIS")
print("-" * 70)
print(f"Material Cost               : ₹{total_material_cost:,.2f}")
print(f"Labour Cost                 : ₹{total_labour_cost:,.2f}")
print(f"Machine Cost                : ₹{machine_cost:,.2f}")
print(f"Wastage Cost                : ₹{wastage_cost:,.2f}")
print(f"Total Manufacturing Cost    : ₹{total_cost:,.2f}")

print("\nREVENUE ANALYSIS")
print("-" * 70)
print(f"Selling Price per Unit      : ₹{selling_price_per_unit:,.2f}")
print(f"Total Revenue               : ₹{total_revenue:,.2f}")

print("\nPROFITABILITY ANALYSIS")
print("-" * 70)
print(f"Profit / Loss               : ₹{profit:,.2f}")
print(f"Profit Percentage           : {profit_percentage:.2f}%")
print(f"Production Status           : {status}")

print("\nTARGET ANALYSIS")
print("-" * 70)
print(f"Target Profit               : ₹{profit_target:,.2f}")
print(f"Target Status               : {target_status}")

print("=" * 70)
