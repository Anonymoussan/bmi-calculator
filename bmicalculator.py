Height = float(input("Enter height in meters: "))
Weight = float(input("Enter weight in kg: "))

Bmi = (Weight/Height**2)

print("your bmi is :" , Bmi )

if Bmi <= 16:
    print("your in Severe thickness","try to have something")
elif Bmi > 16 and Bmi <=17:
    print("your in Moderate thinness")
elif Bmi > 17 and Bmi <=18.5:
    print("your in mild thinnes")
elif Bmi > 18.5 and Bmi <=25:
    print("your normal")
elif Bmi > 25 and Bmi <=30:
    print("your over weight","please try to reduce your weigth")
elif Bmi > 30 and Bmi <=35:
    print("your in Obese class 1","please do excercise")
elif Bmi > 35 and Bmi <=40:
    print("your in Obese class 2","your really heavy ")
elif Bmi > 40:
    print("your in obese class 3","please consult a doctor")
