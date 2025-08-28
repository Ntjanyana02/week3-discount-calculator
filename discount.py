#!/usr/bin/env python3
"""
Week 3 Assignment: Discount Calculator

- Function: calculate_discount(price, discount_percent)
  * If discount_percent >= 20, return price after applying the discount.
  * Otherwise, return the original price unchanged.

- Script flow:
  * Prompt user for original price and discount percentage.
  * Print the final price (or original if no discount applied).
"""

def calculate_discount(price: float, discount_percent: float) -> float:
    """Return the discounted price if discount_percent >= 20, else original price."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def fmt_money(x: float) -> str:
    """Format a number as money with 2 decimal places."""
    return f"{x:.2f}"

def main() -> None:
    try:
        price_str = input("Enter the original price: ").strip()
        disc_str = input("Enter the discount percentage: ").strip()

        price = float(price_str)
        discount_percent = float(disc_str)

        if price < 0:
            print("Error: Price cannot be negative.")
            return
        if discount_percent < 0:
            print("Error: Discount percentage cannot be negative.")
            return

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(f"Final price after {discount_percent:.0f}% discount: {fmt_money(final_price)}")
        else:
            print(f"No discount applied (<20%). Original price: {fmt_money(final_price)}")

    except ValueError:
        print("Error: Please enter numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()
