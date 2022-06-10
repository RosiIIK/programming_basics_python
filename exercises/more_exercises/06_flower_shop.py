import math

magnoliums = int(input())
zumbuls = int(input())
roses = int(input())
cactuses = int(input())
gift_price = float(input())

magnoliums_price = magnoliums * 3.25
zumbuls_price = zumbuls * 4
roses_price = roses * 3.5
cactuses_price = cactuses * 8

total_flowers = magnoliums_price + zumbuls_price + roses_price + cactuses_price
taxes = 0.05 * total_flowers
profit = total_flowers - taxes
money_left = 0
if profit >= gift_price:
    money_left = abs(gift_price - profit)
    print(f"She is left with {math.floor(money_left)} leva.")
elif profit < gift_price:
    money_left = abs(profit - gift_price)
    print(f"She will have to borrow {math.ceil(money_left)} leva.")
