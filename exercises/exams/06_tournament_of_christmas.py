days = int(input())

win_is_more = False
total_price = 0
total_counter_wins = 0
total_counter_lose = 0
for num_day in range(1, days + 1):
    command = input()
    price_per_day = 0
    counter_wins = 0
    counter_lose = 0
    while command != "Finish":
        current_sport = str(command)
        result = input()
        if result == "win":
            price_per_day += 20
            counter_wins += 1
            total_counter_wins += counter_wins
        else:
            counter_lose += 1
            total_counter_lose += counter_lose
            
        # total_counter_wins += counter_wins
        # total_counter_lose += counter_lose
        command = input()

    if counter_wins > counter_lose:
        win_is_more = True
        price_per_day *= 1.10

    total_price += price_per_day

if total_counter_wins > total_counter_lose:
    total_price *= 1.20
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_price:.2f}")
