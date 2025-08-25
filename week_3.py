#PART 1  
def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price.

    :param price: Original price of the item.
    :param discount_percent: Discount percentage to be applied.
    :return: Price after discount.
    """
    if  not (20 <= discount_percent <= 100):
        return price
    else:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount  

#PART 2
input_price = float(input("Enter the original price: "))
input_discount = float(input("Enter the discount percentage (20-100): "))   
if input_discount >20 or input_discount <100:
    final_price = calculate_discount(input_price, input_discount)
    print(f"The price after a {input_discount}% discount is: ${final_price:.2f}")
else:
    print(f"The discount percentage must be between 20 and 100. No discount applied. Final price is: ${input_price:.2f}")   
