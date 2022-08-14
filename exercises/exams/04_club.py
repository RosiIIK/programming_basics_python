club_profit = float(input())

cocktail = input()
final_sum = 0
diff = 0
while cocktail != "Party!":
    current_cocktail = str(cocktail)
    number_of_cocktails = int(input())
    price_per_cocktail = len(current_cocktail)
    total_cocktail = number_of_cocktails * price_per_cocktail

    if total_cocktail % 2 == 1:  #нечетно число
        total_cocktail *= 0.75

    final_sum += total_cocktail
    if final_sum >= club_profit:
        break

    cocktail = input()


diff = abs(final_sum - club_profit)
if final_sum >= club_profit:
    print("Target acquired.")
    print(f"Club income - {final_sum:.2f} leva.")
else:
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {final_sum:.2f} leva.")
