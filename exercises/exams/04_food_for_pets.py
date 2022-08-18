days = int(input())
total_quantity_food = float(input())

total_eaten_food = 0
total_food_dog = 0
total_food_cat = 0
total_biscuits = 0
total_eaten_food_per_day = 0
for i in range(1, days + 1):
    food_dog = int(input())
    food_cat = int(input())
    total_food_dog += food_dog
    total_food_cat += food_cat
    if i % 3 == 0:
        biscuits = (food_dog + food_cat) * 0.10
        total_biscuits += biscuits
        total_eaten_food_per_day = food_dog + food_cat
        # print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
    else:
        total_eaten_food_per_day = food_dog + food_cat

    total_eaten_food += total_eaten_food_per_day
percent_eaten_food = total_eaten_food / total_quantity_food * 100
percent_eaten_food_dog = total_food_dog / total_eaten_food * 100
percent_eaten_food_cat = total_food_cat / total_eaten_food * 100
print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_food_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_food_cat:.2f}% eaten from the cat.")
