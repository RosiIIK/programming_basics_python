days = int(input())
room = input()
evaluation = input()

nights = days - 1
price = 0
if room == "room for one person":
    price = 18
elif room == "apartment":
    price = 25
    if days < 10:
        price *= 0.70
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room == "president apartment":
    price = 35
    if days < 10:
        price *= 0.90
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8
total = price * nights
if evaluation == "positive":
    total *= 1.25
elif evaluation == "negative":
    total *= 0.9
print (f"{total:.2f}")
