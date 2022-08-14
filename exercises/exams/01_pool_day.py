import math

people = int(input())
entry_tax = float(input())
bed_price = float(input())
umbrella_price = float(input())

total_entry_tax = people * entry_tax
total_beds = math.ceil(people * 0.75)
price_for_total_beds = total_beds * bed_price

total_umbrellas = math.ceil(people * 0.50)
price_for_total_umbrellas = total_umbrellas * umbrella_price

final_sum = total_entry_tax + price_for_total_beds + price_for_total_umbrellas
print(f"{final_sum:.2f} lv.")
