budget = float(input())
sex = input()
age = int(input())
sport = input()

card_price = 0
if sex == "m" and sport == "Gym":
    card_price = 42
elif sex == "m" and sport == "Boxing":
    card_price = 41
elif sex == "m" and sport == "Yoga":
    card_price = 45
elif sex == "m" and sport == "Zumba":
    card_price = 34
elif sex == "m" and sport == "Dances":
    card_price = 51
elif sex == "m" and sport == "Pilates":
    card_price = 39
if sex == "f" and sport == "Gym":
    card_price = 35
elif sex == "f" and sport == "Boxing":
    card_price = 37
elif sex == "f" and sport == "Yoga":
    card_price = 42
elif sex == "f" and sport == "Zumba":
    card_price = 31
elif sex == "f" and sport == "Dances":
    card_price = 53
elif sex == "f" and sport == "Pilates":
    card_price = 37

if age <= 19:
    card_price *= 0.8

diff = abs(budget - card_price)
if budget >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")
