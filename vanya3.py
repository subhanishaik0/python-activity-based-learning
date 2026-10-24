# Hospital Billing and Patient Classification System

print("===== HOSPITAL BILLING SYSTEM =====")

# Patient Details
patient_name = input("Enter Patient Name: ")
patient_id = input("Enter Patient ID: ")

try:
    # Charges Input
    consultation_charge = float(input("Enter Consultation Charge: "))
    diagnostic_charge = float(input("Enter Diagnostic Charge: "))
    treatment_charge = float(input("Enter Treatment Charge: "))

    # Validation
    if consultation_charge < 0 or diagnostic_charge < 0 or treatment_charge < 0:
        print("Error: Charges cannot be negative.")
        exit()

    # Total Bill
    total_bill = consultation_charge + diagnostic_charge + treatment_charge

    # Payment Policy Selection
    print("\nPatient Categories:")
    print("1. Senior Citizen (20% Concession)")
    print("2. Government Employee (15% Concession)")
    print("3. Insurance Holder (30% Concession)")
    print("4. General Patient (No Concession)")

    choice = int(input("Enter Category Choice (1-4): "))

    concession = 0
    category = ""

    if choice == 1:
        category = "Senior Citizen"
        concession = total_bill * 0.20

    elif choice == 2:
        category = "Government Employee"
        concession = total_bill * 0.15

    elif choice == 3:
        category = "Insurance Holder"
        concession = total_bill * 0.30

    elif choice == 4:
        category = "General Patient"
        concession = 0
    else:
        print("Invalid category choice.")
        exit()

    # Final Bill
    final_bill = total_bill - concession

    # Patient Classification
    if final_bill >= 50000:
        patient_class = "High Value Patient"
    elif final_bill >= 20000:
        patient_class = "Premium Patient"
    else:
        patient_class = "Regular Patient"

    # Display Bill
    print("\n========== BILL SUMMARY ==========")
    print(f"Patient Name           : {patient_name}")
    print(f"Patient ID             : {patient_id}")
    print(f"Patient Category       : {category}")
    print(f"Consultation Charge    : ₹{consultation_charge:.2f}")
    print(f"Diagnostic Charge      : ₹{diagnostic_charge:.2f}")
    print(f"Treatment Charge       : ₹{treatment_charge:.2f}")
    print(f"Total Bill             : ₹{total_bill:.2f}")
    print(f"Concession Amount      : ₹{concession:.2f}")
    print(f"Final Amount Payable   : ₹{final_bill:.2f}")
    print(f"Patient Classification : {patient_class}")
    print("==================================")

except ValueError:
    print("Error: Please enter valid numeric values.")