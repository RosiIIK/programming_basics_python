fuel_type = input()
fuel_quantity = float(input())
club_card = input()

gasoline = 2.22
diesel = 2.33
gas = 0.93

discount = 0
if fuel_type == "Gas" and club_card == "Yes":
    discount = 0.08
    gas_price = gas - discount
    total_price = gas_price * fuel_quantity
elif fuel_type == "Gas" and club_card == "No":
    discount = 0
    gas_price = gas
    total_price = gas_price * fuel_quantity
if fuel_type == "Gasoline" and club_card == "Yes":
    discount = 0.18
    gasoline_price = gasoline - discount
    total_price = gasoline_price * fuel_quantity
elif fuel_type == "Gasoline" and club_card == "No":
    discount = 0
    gasoline_price = gasoline
    total_price = gasoline_price * fuel_quantity
if fuel_type == "Diesel" and club_card == "Yes":
    discount = 0.12
    diesel_price = diesel - discount
    total_price = diesel_price * fuel_quantity
elif fuel_type == "Diesel" and club_card == "No":
    discount = 0
    diesel_price = diesel
    total_price = diesel_price * fuel_quantity
if 20 < fuel_quantity <= 25:
    total_price *= 0.92
elif fuel_quantity > 25:
    total_price *= 0.90
print(f"{total_price:.2f} lv.")
