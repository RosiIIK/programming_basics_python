failed_scores = int(input())

failed_times = 0
solved_problems_count = 0
total_grades = 0
last_task = ""
has_failed = True

while failed_times < failed_scores:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    total_grades += grade
    solved_problems_count += 1
    last_task = problem_name

if has_failed:
    print(f"You need a break, {failed_scores} poor grades.")
else:
    print(f"Average score: {total_grades / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_task}")
