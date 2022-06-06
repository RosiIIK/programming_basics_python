x = float(input())
y = float(input())
h = float(input())

#sides
sideway_wall = x * y
window = 1.5 * 1.5
total_side = 2 * sideway_wall - 2 * window
backside_wall = x * x
entry = 1.2 * 2
total_backside = 2 * backside_wall - entry
total_wall_square = total_side + total_backside
green_paint = total_wall_square / 3.4
print(f"{green_paint:.2f}")

#roof
roof_rectangles = 2 * (x * y)
roof_triangle = 2 * (x * h / 2)
total_roof_square = roof_rectangles + roof_triangle
red_paint = total_roof_square / 4.3
print(f"{red_paint:.2f}")
