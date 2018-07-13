import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    for i in range(len(age)):
        age[i] = pow(age[i], 2)
    total = sum(age)
    return int(math.sqrt(total) / 2)


print(predict_age(65, 60, 75, 55, 60, 63, 64, 45))
