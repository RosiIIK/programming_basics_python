import math

days = int(input())
food_kg = int(input())
food_dog_kg = float(input())
food_cat_kg = float(input())
food_turtle_gr = float(input())

food_turtle_kg = food_turtle_gr / 1000

food_dog_kg *= days
food_cat_kg *= days
food_turtle_kg *= days
total_food  = food_dog_kg + food_cat_kg + food_turtle_kg
rest_food = 0
if total_food <= food_kg:
    rest_food = abs(food_kg - total_food)
    print(f"{math.floor(rest_food)} kilos of food left.")
elif total_food > food_kg:
    rest_food = abs(total_food - food_kg)
    print(f"{math.ceil(rest_food)} more kilos of food are needed.")
