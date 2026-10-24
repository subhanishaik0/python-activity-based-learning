# Employee Payroll and Deduction Analysis

print("=" * 60)
print("        EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS")
print("=" * 60)

# Employee Details
emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")

try:
    # Salary Inputs
    basic_pay = float(input("Enter Basic Pay: ₹"))
    allowances = float(input("Enter Allowances: ₹"))
    overtime = float(input("Enter Overtime Pay: ₹"))
    incentives = float(input("Enter Incentives: ₹"))

    # Validation
    if basic_pay < 0 or allowances < 0 or overtime < 0 or incentives < 0:
        print("\nError: Salary components cannot be negative.")
        exit()

    # Gross Salary Calculation
    gross_salary = basic_pay + allowances + overtime + incentives

    # Progressive Tax Deduction
    if gross_salary <= 30000:
        tax = gross_salary * 0.05
    elif gross_salary <= 60000:
        tax = gross_salary * 0.10
    else:
        tax = gross_salary * 0.15

    # Other Deductions
    provident_fund = basic_pay * 0.12
    insurance = gross_salary * 0.02

    # Total Deductions
    total_deductions = tax + provident_fund + insurance

    # Net Salary
    net_salary = gross_salary - total_deductions

    # Employee Classification
    if net_salary >= 80000:
        category = "Grade A"
    elif net_salary >= 50000:
        category = "Grade B"
    elif net_salary >= 30000:
        category = "Grade C"
    else:
        category = "Grade D"

    # Salary Statement
    print("\n")
    print("=" * 60)
    print("                  SALARY STATEMENT")
    print("=" * 60)

    print(f"Employee ID            : {emp_id}")
    print(f"Employee Name          : {emp_name}")

    print("\nEARNINGS")
    print("-" * 60)
    print(f"Basic Pay              : ₹{basic_pay:,.2f}")
    print(f"Allowances             : ₹{allowances:,.2f}")
    print(f"Overtime Pay           : ₹{overtime:,.2f}")
    print(f"Incentives             : ₹{incentives:,.2f}")
    print(f"Gross Salary           : ₹{gross_salary:,.2f}")

    print("\nDEDUCTIONS")
    print("-" * 60)
    print(f"Income Tax             : ₹{tax:,.2f}")
    print(f"Provident Fund (12%)   : ₹{provident_fund:,.2f}")
    print(f"Insurance (2%)         : ₹{insurance:,.2f}")
    print(f"Total Deductions       : ₹{total_deductions:,.2f}")

    print("\nFINAL SALARY")
    print("-" * 60)
    print(f"Net Salary             : ₹{net_salary:,.2f}")
    print(f"Employee Grade         : {category}")

    print("=" * 60)

except ValueError:
    print("\nError: Please enter valid numeric values.")