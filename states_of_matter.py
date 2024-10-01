input_temp = float(input('Enter a temperature in Celsius: '))

if input_temp <= 0:
  print('Water is solid')
elif input_temp >= 100:
  print('Water is gaseous')
elif input_temp > 0 and input_temp < 100:
  print('Water is liquid')