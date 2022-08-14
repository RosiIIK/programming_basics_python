gamer_name = input()

max_points = 0
winner_name = ""
while gamer_name != "Stop":
    new_gamer = gamer_name
    player_points = 0
    for letter in new_gamer:
        number = int(input())
        if number == ord(letter): #ord очаква буква и преобр в цифра/ch очаква цифра и преобр в буква
            player_points += 10
        else:
            player_points += 2

    if player_points >= max_points:
        max_points = player_points
        winner_name = new_gamer

    gamer_name = input()

print(f"The winner is {winner_name} with {max_points} points!")
