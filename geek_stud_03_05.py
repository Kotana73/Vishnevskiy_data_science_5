with open('my_file.txt', 'r', encoding='utf-8') as f:
    names = []
    medium_income = 0
    num = 0
    for line in f:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        medium_income += income
    medium_income /= num
print(*names)
print(medium_income)
