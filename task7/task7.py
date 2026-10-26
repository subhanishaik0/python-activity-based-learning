# Retail Billing with Multiple Discount Rules

print("=" * 80)
print("             RETAIL BILLING SYSTEM")
print("=" * 80)

# Tax rates by category
tax_rates = {
    "Grocery": 5,
    "Electronics": 18,
    "Clothing": 12,
    "Books": 0
}

# Discount Rules
DISCOUNT_THRESHOLD = 5000      # Bill amount above this gets discount
DISCOUNT_RATE = 10             # 10% discount
MAX_DISCOUNT = 2000            # Maximum concession

num_products = int(input("Enter number of products: "))

items = []

subtotal = 0
total_tax = 0

for i in range(num_products):

    print(f"\nProduct {i+1}")
    name = input("Product Name: ")

    print("Categories: Grocery, Electronics, Clothing, Books")
    category = input("Category: ")

    if category not in tax_rates:
        print("Invalid Category! Defaulting to Grocery.")
        category = "Grocery"

    price = float(input("Unit Price (₹): "))
    quantity = int(input("Quantity: "))

    item_total = price * quantity
    tax_amount = item_total * tax_rates[category] / 100

    subtotal += item_total
    total_tax += tax_amount

    items.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "item_total": item_total,
        "tax": tax_amount
    })

# Discount Calculation
discount = 0

if subtotal >= DISCOUNT_THRESHOLD:
    discount = subtotal * DISCOUNT_RATE / 100

    if discount > MAX_DISCOUNT:
        discount = MAX_DISCOUNT

# Final Bill
grand_total = subtotal + total_tax - discount

# Invoice Generation
print("\n")
