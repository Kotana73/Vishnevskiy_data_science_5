my_dict = {}
with open('my_text_05.txt', encoding='utf-8') as f:
    for line in f:
        discip, status = line.split(':')
        discip_sum = sum(map(int, ' '.join([i for i in status if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[discip] = discip_sum
    print(f'{my_dict}')
