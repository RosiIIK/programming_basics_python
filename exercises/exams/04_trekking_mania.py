number_of_groups = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for n in range(1, number_of_groups + 1):
    number_of_people = int(input())
    if number_of_people <= 5: #Musala
        p1 += number_of_people
    elif 6 <= number_of_people <= 12: #Monblan
        p2 += number_of_people
    elif 13 <= number_of_people <= 25: #Kilimandjaro
        p3 += number_of_people
    elif 26 <= number_of_people <= 40: #K2
        p4 += number_of_people
    elif number_of_people >= 41: #Everest
        p5 += number_of_people

total_people = p1 + p2 + p3 + p4 + p5

percent_people_musala = (p1 / total_people) * 100
percent_people_monblan = (p2 / total_people) * 100
percent_people_kilimandjaro = (p3 / total_people) * 100
percent_people_k2 = (p4 / total_people) * 100
percent_people_everest = (p5 / total_people) * 100

print(f"{percent_people_musala:.2f}%")
print(f"{percent_people_monblan:.2f}%")
print(f"{percent_people_kilimandjaro:.2f}%")
print(f"{percent_people_k2:.2f}%")
print(f"{percent_people_everest:.2f}%")
