import math

x_area = int(input())
y_grape_area = float(input())
z_needed_wine = int(input())
worker = int(input())

total_grape = x_area * y_grape_area
wine = 0.4 * total_grape / 2.5

if wine >= z_needed_wine:
    rest_wine = abs(wine - z_needed_wine)
    wine_per_worker = rest_wine / worker
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(rest_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
elif wine < z_needed_wine:
    not_enough = abs(z_needed_wine - wine)
    print(f"It will be a tough winter! More {math.floor(not_enough)} liters wine needed.")
