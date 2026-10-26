# Railway Fare and Reservation Calculator

print("=" * 70)
print("          RAILWAY FARE AND RESERVATION CALCULATOR")
print("=" * 70)

# Number of Passengers
num_passengers = int(input("Enter Number of Passengers: "))

total_fare = 0

# Travel Class Selection
print("\nTravel Classes")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
print("4. AC 1 Tier")

class_choice = int(input("Enter Travel Class (1-4): "))

# Distance Input
distance = float(input("Enter Distance (in km): "))

# Distance Slab Rates (per km)
if distance <= 100:
    base_rate = 1.5
elif distance <= 500:
    base_rate = 2.0
elif distance <= 1000:
    base_rate = 2.5
else:
    base_rate = 3.0

# Class Multipliers
if class_choice == 1:
    class_name = "Sleeper"
    multiplier = 1.0
    reservation_fee = 20
elif class_choice == 2:
    class_name = "AC 3 Tier"
    multiplier = 1.8
    reservation_fee = 40
elif class_choice == 3:
    class_name = "AC 2 Tier"
    multiplier = 2.5
    reservation_fee = 60
elif class_choice == 4:
    class_name = "AC 1 Tier"
    multiplier = 3.5
    res_fee = 80