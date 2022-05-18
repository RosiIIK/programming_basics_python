holiday_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

num = num_trucks + num_minions + num_puzzles + num_bears + num_dolls

sum_puzzles = num_puzzles * 2.6
sum_dolls = num_dolls * 3
sum_bears = num_bears * 4.1
sum_minions = num_minions * 8.2
sum_trucks = num_trucks * 2

sum = (sum_trucks + sum_minions + sum_bears + sum_dolls + sum_puzzles) * 0.9

if num >= 50:
    sum *= 0.75

difference = abs(sum - holiday_price)

if sum >= holiday_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
