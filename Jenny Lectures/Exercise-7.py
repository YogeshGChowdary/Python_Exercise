# BMI = weight/((height)**2)
 
wt = float(input('enter weight in kgs: '))
ht = float(input('enter height in mts: '))

bmi = wt/((ht)**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print('your bmi is', bmi, 'and you are normal weight')
elif bmi < 30:
    print("your bmi is", bmi, 'and you are over weight')
elif bmi < 35:
    print(f"your bmi is {bmi} and you are obese")
else:
    print(f'your bmi is {bmi} and you are clinically obese')
