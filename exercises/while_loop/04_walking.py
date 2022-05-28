command = input()
target_steps = 10000
total_steps = 0

while command != 'Going home':

    walked_steps = int(command)
    total_steps += walked_steps
    if total_steps >= target_steps:
        break
    command = input()

else:
    steps_to_home = int(input())
    total_steps += steps_to_home

if total_steps >= target_steps:
    print ('Goal reached! Good job!')
    print (f'{total_steps - target_steps} steps over the goal!')
else:
    print(f'{target_steps - total_steps} more steps to reach goal.')
