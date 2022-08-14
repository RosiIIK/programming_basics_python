budget = float(input())
nights= int(input())
price_per_night = float(input())
percent_add_charges = float(input())

if nights > 7:
    price_per_night *= 0.95


total_price_for_nights = nights * price_per_night
add_charges_price = (budget * percent_add_charges) / 100
final_price_for_all_nights = total_price_for_nights + add_charges_price

if final_price_for_all_nights <= budget:
    diff = abs(final_price_for_all_nights - budget)
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    diff = abs(final_price_for_all_nights - budget)
    print(f"{diff:.2f} leva needed.")
