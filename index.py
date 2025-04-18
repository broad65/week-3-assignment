def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print result
    if final_price == original_price:
        print(f"No discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")