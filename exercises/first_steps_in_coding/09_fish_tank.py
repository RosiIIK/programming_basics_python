lenght_sm = int(input())
width_sm = int(input())
height_sm = int(input())
percent = float(input())

V_aquarium = lenght_sm * width_sm * height_sm
V_liters = V_aquarium * 0.001
filled_place = percent * 0.01

needed_liters = V_liters * (1 - filled_place)
print(needed_liters)
