month = input()
number_of_nights = int(input())
apartment_price = 0
studio_price = 0
if month == 'May' or month == 'October':
    apartment_price = 65
    studio_price = 50
    if 7 <number_of_nights <= 14:
        studio_price *= 0.95
    elif number_of_nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == 'June' or month == 'September':
    apartment_price = 68.70
    studio_price = 75.20
    if number_of_nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == 'July' or month == 'August':
    apartment_price = 77
    studio_price = 76
    if number_of_nights > 14:
        apartment_price = 77 * 0.90
total_apartment = apartment_price * number_of_nights
total_studio = studio_price * number_of_nights
print(f'Apartment: {total_apartment:.2f} lv.')
print(f'Studio: {total_studio:.2f} lv.')
