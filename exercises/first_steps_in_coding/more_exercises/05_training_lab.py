room_w = float(input())  
room_h = float(input())  

#Restrictions: 3 ≤ h ≤ w ≤ 100.
room_w_cm = room_w * 100
room_h_cm = room_h * 100
working_place_cm = 70 * 120
row_seats = (room_h_cm - 100) // 70
column_seats = room_w_cm // 120
total_seats = row_seats * column_seats - 3
print(total_seats)
