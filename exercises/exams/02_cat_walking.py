walk_minutes = int(input())
num_daily_walks = int(input())
calories_per_day = int(input())

total_time_daily_walks = walk_minutes * num_daily_walks
burn_daily_calories = total_time_daily_walks * 5
percent_calories_per_day = calories_per_day * 0.5

if burn_daily_calories >= percent_calories_per_day:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_daily_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_daily_calories}.")
