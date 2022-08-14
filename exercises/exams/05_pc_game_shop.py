sale_games = int(input())

counter_hearthstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_other = 0
for games in range(1, sale_games + 1):
    name_game = input()
    if name_game == "Hearthstone":
        counter_hearthstone += 1
    elif name_game == "Fornite":
        counter_fornite += 1
    elif name_game == "Overwatch":
        counter_overwatch += 1
    elif name_game != "Hearthstone" or name_game != "Fornite" or name_game != "Overwatch":
        counter_other += 1

percent_sale_game_h = (counter_hearthstone / sale_games) * 100
percent_sale_game_f = (counter_fornite / sale_games) * 100
percent_sale_game_o = (counter_overwatch / sale_games) * 100
percent_sale_game = (counter_other / sale_games) * 100
print(f"Hearthstone - {percent_sale_game_h:.2f}%")
print(f"Fornite - {percent_sale_game_f:.2f}%")
print(f"Overwatch - {percent_sale_game_o:.2f}%")
print(f"Others - {percent_sale_game:.2f}%")
