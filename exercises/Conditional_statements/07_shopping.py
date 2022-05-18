price_of_video_card = 250

budget = float(input())
num_of_video_cards = int(input())
num_of_cpu = int(input())
num_of_ram = int(input())

price_of_cpu = 0.35 * (num_of_video_cards * price_of_video_card)
price_of_ram = 0.10 * (num_of_video_cards * price_of_video_card)

total_price = num_of_video_cards * price_of_video_card + \
              num_of_cpu * price_of_cpu + num_of_ram * price_of_ram

if num_of_video_cards > num_of_cpu:
    total_price = total_price * 0.85

needed_sum = abs(total_price - budget)

if budget >= total_price:
    print(f"You have {needed_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {needed_sum:.2f} leva more!")
