total_km = int(input())
day_or_night = input()

taxi = 0.70
bus = 0.09
train = 0.06
day_or_night_price = 0

if total_km < 20 and day_or_night == "day":
    taxi += total_km * 0.79
    print(f"{taxi:.2f}")
elif total_km < 20 and day_or_night == "night":
    taxi += total_km * 0.90
    print(f"{taxi:.2f}")
elif 20 <= total_km < 100:
    bus *= total_km
    print(f"{bus:.2f}")
elif total_km >= 100:
    train *= total_km
    print(f"{train:.2f}")
