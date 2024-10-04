#user inputs starting hour (0-23) and how long it lasts (hours)
A_start = int(input('Enter start hour for event A: '))
A_duration = int(input('Enter duration of event A (in hours): '))
B_start = int(input('Enter start hour for event B: '))
B_duration = int(input('Enter duration of event B (in hours): '))

#create end points
A_end = A_start + A_duration
B_end = B_start + B_duration

#determine if events overlap
if A_end <= B_start or B_end <= A_start:
    print('Events do not overlap')
else:
    print('Events overlap')

#events that end and start on the same hour aren't considered overlapping