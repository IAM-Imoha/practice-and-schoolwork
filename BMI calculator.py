weight = int(input('Enter your weight in kg: '))
height = int(input('Enter your height in cm: '))
#check for zero input to avoid dividing by zero
if height == 0:
    print('N/A')
else:
    bmi = weight/(height/100)**2
    print("Your BMI is", bmi)