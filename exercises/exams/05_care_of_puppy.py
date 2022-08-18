food_kg = int(input())
food_in_grams = food_kg * 1000

command = input()
food_is_enough = True
eaten_food = 0
while command != "Adopted":
    current_food = int(command)
    eaten_food += current_food
    if eaten_food > food_in_grams:
        food_is_enough = False

    command = input()
food_left = abs(food_in_grams - eaten_food)

if food_is_enough:
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    print(f"Food is not enough. You need {food_left} grams more.")
