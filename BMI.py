def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5: #18.5 a 25
        result = "underweight"
    elif bmi > 25:
        result = "overweight"
    else: