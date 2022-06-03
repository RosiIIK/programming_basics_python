jury_number = int(input())
name_of_presentation = input()

sum_of_grades = 0
sum_of_grades_per_person = 0
counter = 0
while name_of_presentation != "Finish":
    for i in range(1, jury_number + 1):
        individual_grade = float(input())
        sum_of_grades += individual_grade
        sum_of_grades_per_person += individual_grade
        counter += 1

    average_grade = sum_of_grades_per_person / jury_number
    print(f"{name_of_presentation} - {average_grade:.2f}.")
    sum_of_grades_per_person = 0
    name_of_presentation = input()
average_total = sum_of_grades / counter
print(f"Student's final assessment is {average_total:.2f}.")
