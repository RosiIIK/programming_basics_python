import sys

n = int(input())

max_num = -sys.maxsize  #сравнява ни числото с най-малкото такова число
min_num = sys.maxsize #сравнява ни числото с най-голамата стойност
for i in range(n): # ot 0 do n
    value = int(input())

    if value > max_num:
        max_num = value

    if value < min_num:
        min_num = value

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
