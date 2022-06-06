vegetables_per_kilo = float(input())
fruits_per_kilo = float(input())
total_vegetables = int(input())
total_fruits = int(input())


course_euro_per_lev = 1.94
price_vegetables = vegetables_per_kilo * total_vegetables
price_fruits = fruits_per_kilo * total_fruits
total_sum = (price_vegetables + price_fruits) / course_euro_per_lev
print(f"{total_sum:.2f}")
