d = {'One', 'Один', 'Two', 'Два', 'Three', 'Три', 'Four', 'Четыре'}
with open('my_text_03.txt', 'r', encoding='utf-8') as f:
    with open('my_text_03.txt', 'w', encoding='utf-8') as f2:
        f2.writelines([line.replace(line.split()[0], d.get(line.split()[0]))for line in f])
