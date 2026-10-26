# Campus Event Financial Planning System

import math

print("=" * 70)
print("            CAMPUS EVENT FINANCIAL PLANNING")
print("=" * 70)

# Event Details
event_name = input("Enter Event Name: ")

# Fixed Costs
venue_cost = float(input("Enter Venue Cost (₹): "))
equipment_cost = float(input("Enter Equipment Cost (₹): "))
transport_cost = float(input("Enter Transport Cost (₹): "))

# Per Participant Costs
catering_cost_per_person = float(
    input("Enter Catering Cost per Participant (₹): ")
)
certificate_cost_per_person = float(
    input("Enter Certificate Cost per Participant (₹): ")
)

# Participants
participants = int(
    input("Enter Expected Number of Participants: ")
)

registration_fee = float(
    input("Enter Registration Fee per Participant (₹): ")
)

# Sponsorship
sponsorship_amount = float(
    input("Enter Sponsorship Amount Received (₹): ")
)

# Cost Calculation
catering_cost = catering_cost_per_person * participants
certificate_cost = certificate_cost_per_person * participants

total_cost = (
    venue_cost +
    equipment_cost +
    transport_cost +
    catering_cost +
    certificate_cost
)

# Revenue Calculation
participant_contribution = registration_fee * participants

total_revenue = (
    participant_contribution +
    sponsorship_amount
)

# Profit / Loss
profit_loss = total_revenue - total_cost

# Sponsorship Shortfall
if sponsorship_amount < total_cost:
    sponsorship_shortfall = total_cost - sponsorship_amount
else:
    sponsorship_shortfall = 0

# Break-Even Analysis
variable_cost_per_participant = (
    catering_cost_per_person +
    certificate_cost_per_person
)

fixed_costs = (
    venue_cost +
    equipment_cost +
    transport_cost
)

contribution_per_participant = (
    registration_fee - variable_cost_per_participant
)

if contribution_per_participant > 0:
    break_even_count = math.ceil(
        (fixed_costs - sponsorship_amount) /
        contribution_per_participant
    )

    if break_even_count < 0:
        break_even_count = 0
else:
    break_even_count = "Not Possible"

# Report
print("\n")
print("=" * 70)
print("                 EVENT FINANCIAL REPORT")
print("=" * 70)

print(f"Event Name                   : {event_name}")

print("\nCOST DETAILS")
print("-" * 70)
print(f"Venue Cost                   : ₹{venue_cost:,.2f}")
print(f"Equipment Cost               : ₹{equipment_cost:,.2f}")
print(f"Transport Cost               : ₹{transport_cost:,.2f}")
print(f"Catering Cost                : ₹{catering_cost:,.2f}")
print(f"Certificate Cost             : ₹{certificate_cost:,.2f}")
print(f"Total Cost                   : ₹{total_cost:,.2f}")

print("\nREVENUE DETAILS")
print("-" * 70)
print(f"Participant Contributions    : ₹{participant_contribution:,.2f}")
print(f"Sponsorship Amount           : ₹{sponsorship_amount:,.2f}")
print(f"Total Revenue                : ₹{total_revenue:,.2f}")

print("\nFINANCIAL ANALYSIS")
print("-" * 70)
print(f"Profit / Loss                : ₹{profit_loss:,.2f}")

if profit_loss > 0:
    print("Status                       : PROFIT ✅")
elif profit_loss < 0:
    print("Status                       : LOSS ❌")
else:
    print("Status                       : BREAK EVEN")

print(f"Sponsorship Shortfall        : ₹{sponsorship_shortfall:,.2f}")

print("\nBREAK-EVEN ANALYSIS")
print("-" * 70)
print(f"Minimum Registrations Needed : {break_even_count}")

print("=" * 70)