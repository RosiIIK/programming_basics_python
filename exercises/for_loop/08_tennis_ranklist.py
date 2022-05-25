import math

number_of_tournaments = int(input())
ranglist_points = int(input())
winning_points = 0
wins = 0

for tournaments in range(number_of_tournaments):
    final_place = input()
    if final_place == "W":
        ranglist_points += 2000
        winning_points += 2000
        wins += len(final_place)
    elif final_place == "F":
        ranglist_points += 1200
        winning_points += 1200
    elif final_place == "SF":
        ranglist_points += 720
        winning_points += 720
print(f"Final points: {ranglist_points}")
average_points = winning_points / number_of_tournaments
print(f"Average points: {math.floor(average_points)}")
percent_wins = (wins / number_of_tournaments) * 100
print(f"{percent_wins:.2f}%")
