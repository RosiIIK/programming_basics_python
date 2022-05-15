number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())
price_per_chicken_menu = 10.35
price_per_fish_menu = 12.40
price_per_vegetarian_menu = 8.15
delivery = 2.50
dessert = ((number_of_chicken_menus * price_per_chicken_menu) + \
            (number_of_fish_menus * price_per_fish_menu) + \
            (number_of_vegetarian_menus * price_per_vegetarian_menu)) * 0.2
needed_sum = (number_of_chicken_menus * price_per_chicken_menu) + \
            (number_of_fish_menus * price_per_fish_menu) + \
            (number_of_vegetarian_menus * price_per_vegetarian_menu) + \
    dessert + delivery
print(needed_sum)
