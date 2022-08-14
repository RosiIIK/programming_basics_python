team_name = input()
games_total = int(input())

counter_w = 0
counter_d = 0
counter_l = 0
total_points = 0
for r in range(1, games_total + 1):
    result = input()
    if result == "W":
        total_points += 3
        counter_w += 1
    elif result == "D":
        total_points += 1
        counter_d += 1
    elif result == "L":
        total_points += 0
        counter_l += 1

if games_total == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    percent_won_games = (counter_w / games_total) * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {counter_w}")
    print(f"## D: {counter_d}")
    print(f"## L: {counter_l}")
    print(f"Win rate: {percent_won_games:.2f}%")
