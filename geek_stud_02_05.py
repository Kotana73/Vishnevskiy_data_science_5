with open('my_text_02.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        words = len(value.split())
    print(f'В {index} строках содержится, примерно, по {words} слова')
