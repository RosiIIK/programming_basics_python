first_number = int(input())
second_number = int(input())

for current_num in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    current_num_as_string = str(current_num) 
    for index, digit in enumerate(current_num_as_string):
        if index % 2 == 0: #0246 = 1357
            odd_digits_sum += int(digit) 
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(current_num_as_string, end=" ")
