price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))
discount_price = price * discount/100
final_price = price - discount_price
print("Discount amount",discount_price)
print("Final Price",final_price)