number_non_working_days = int(input())

game_non_working_days = number_non_working_days * 127
game_working_days = (365 - number_non_working_days) * 63
total_play_time = game_non_working_days + game_working_days
time_for_play = 30000
rest_time = 0
if time_for_play > total_play_time:
    rest_time = abs(time_for_play - total_play_time)
    hours = rest_time // 60
    minutes = rest_time % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
elif time_for_play < total_play_time:
    rest_time = abs(time_for_play - total_play_time)
    hours = rest_time // 60
    minutes = rest_time % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
