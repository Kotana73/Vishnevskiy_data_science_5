import json

my_dict = dict()
med_gesheft = 0
num = 0
with open('my_text_06.txt', encoding='utf-8') as f:
    for line in f:
        company, name, income, cost = line.split()
        gesheft = int(income) - int(cost)
        if gesheft >= 0:
            med_gesheft += gesheft
            num += 1
        my_dict[company] = gesheft
med_gesheft /= num
with open('json7.json', 'w', encoding='utf-8') as f:
    json.dump([my_dict, {'средний доход': med_gesheft}], f, ensure_ascii=False)