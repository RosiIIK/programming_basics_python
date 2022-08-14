hot_drink = input()
sugar = input()
number_drinks = int(input())

price = 0
if hot_drink == "Espresso":
    if sugar == "Without":
        price = (number_drinks * 0.90) * 0.65
    elif sugar == "Normal":
        price = (number_drinks * 1.00)
    elif sugar == "Extra":
        price = (number_drinks * 1.20)
elif hot_drink == "Cappuccino":
    if sugar == "Without":
        price = (number_drinks * 1.00) * 0.65
    elif sugar == "Normal":
        price = (number_drinks * 1.20)
    elif sugar == "Extra":
        price = (number_drinks * 1.60)
elif hot_drink == "Tea":
    if sugar == "Without":
        price = (number_drinks * 0.50) * 0.65
    elif sugar == "Normal":
        price = (number_drinks * 0.60)
    elif sugar == "Extra":
        price = (number_drinks * 0.70)

if hot_drink == "Espresso" and number_drinks >= 5:
    price *= 0.75

if price > 15:
    discount = price * 0.20
    price -= discount

print(f"You bought {number_drinks} cups of {hot_drink} for {price:.2f} lv.")
