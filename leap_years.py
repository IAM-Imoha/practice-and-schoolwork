year = int(input('Enter a year: '))

#check for not divisible by 4 == common
if (year % 4) != 0:
  print('Common year')

#check for divisible by 4 but not 100 == leap
elif (year % 100) != 0:
  print('Leap year')

#check for divisible by 100 but not 400 == common
elif (year % 400) != 0:
  print('Common year')

#check for divisible by 400 == leap
elif (year % 400) == 0:
  print('Leap year')