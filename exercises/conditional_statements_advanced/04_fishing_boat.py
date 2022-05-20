budget = int(input())
season = input()
number_of_fisherman = int(input())
#Определяме променлива за цена за наем на кораб, което ще се променя в зависимост от сезона/бр рибари/и доп отстъпка
boat_rent = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Winter":
    boat_rent = 2600
else:  #elif season == "Summer" or season == "Autumn"
    boat_rent = 4200
if number_of_fisherman <= 6:
    boat_rent *= 0.9 #10% discount
elif number_of_fisherman <= 11: #elif 7<= number_of_fisherman <=11
    boat_rent *= 0.85
else:
    boat_rent *= 0.75
if season != "Autumn" and number_of_fisherman % 2 == 0: #Ако сезона не е есен и бр. рибари е четен брой
    boat_rent *= 0.95 #5% discount
difference = abs(boat_rent - budget)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
