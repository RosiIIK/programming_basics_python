budget = float (input())
season = input()

total = 0
if budget <= 100 and season == "summer":
    budget *= 0.3
    print(f"Somewhere in Bulgaria")
    print(f"Camp - {budget:.2f}")
elif budget <= 100 and season == "winter":
    budget *= 0.7
    print(f"Somewhere in Bulgaria")
    print(f"Hotel - {budget:.2f}")
elif budget <= 1000 and season == "summer":
    budget *= 0.4
    print(f"Somewhere in Balkans")
    print(f"Camp - {budget:.2f}")
elif budget <= 1000 and season == "winter":
    budget *= 0.8
    print(f"Somewhere in Balkans")
    print(f"Hotel - {budget:.2f}")
elif budget > 1000:
    budget *= 0.9
    print(f"Somewhere in Europe")
    print(f"Hotel - {budget:.2f}")
