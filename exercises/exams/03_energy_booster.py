fruit = input()
gel_set = input()
total_gel_sets = int(input())

price_per_gel_set = 0
total_set_price = 0
if fruit == "Watermelon":
    if gel_set == "small":
        price_per_gel_set = 56
        total_set_price = price_per_gel_set * 2
    elif gel_set == "big":
        price_per_gel_set = 28.7
        total_set_price = price_per_gel_set * 5
elif fruit == "Mango":
    if gel_set == "small":
        price_per_gel_set = 36.66
        total_set_price = price_per_gel_set * 2
    elif gel_set == "big":
        price_per_gel_set = 19.60
        total_set_price = price_per_gel_set * 5
elif fruit == "Pineapple":
    if gel_set == "small":
        price_per_gel_set = 42.10
        total_set_price = price_per_gel_set * 2
    elif gel_set == "big":
        price_per_gel_set = 24.80
        total_set_price = price_per_gel_set * 5
elif fruit == "Raspberry":
    if gel_set == "small":
        price_per_gel_set = 20
        total_set_price = price_per_gel_set * 2
    elif gel_set == "big":
        price_per_gel_set = 15.20
        total_set_price = price_per_gel_set * 5
total_price = total_set_price * total_gel_sets
final_price = 0
if 400 <= total_price <= 1000:
    final_price = total_price * 0.85
elif total_price > 1000:
    final_price = total_price * 0.50
else:
    final_price = total_price
print(f"{final_price:.2f} lv.")
