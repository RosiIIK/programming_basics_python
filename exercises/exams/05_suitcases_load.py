cargo_capacity = float(input())

available_space = cargo_capacity
command = input()
cargo_is_full = False
counter = 0
total_loaded = 0
while command != "End":
    suitcase_volume = float(command)
    counter += 1
    if counter % 3 == 0:
        suitcase_volume *= 1.10
    available_space -= suitcase_volume
    total_loaded += suitcase_volume

    if cargo_capacity < total_loaded:
        cargo_is_full = True
        counter -=1
        break

    command = input()

if cargo_is_full:
    print("No more space!")
else:
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {counter} suitcases loaded.")
