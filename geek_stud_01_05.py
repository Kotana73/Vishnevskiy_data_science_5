my_file = open('my_text_01.txt', 'w', encoding='utf-8')
line = ' '
while line:
    line = input('Вводим текст до полного удовлетворения: ')
    my_file.write(f'{line}\n') if line != '' else my_file.close()
