import math

record_in_seconds = float(input())
distance_in_m = float(input())
time_seconds_per_meter = float(input())

joro_distance_time = distance_in_m * time_seconds_per_meter
delay = math.floor(distance_in_m // 50)
delay_time = delay * 30
joro_total_time = joro_distance_time + delay_time

if joro_total_time >= record_in_seconds:
    diff = abs(joro_total_time - record_in_seconds)
    print(f"No! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {joro_total_time:.2f} seconds.")
