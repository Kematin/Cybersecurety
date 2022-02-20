def first():
    text = [f'{i}_ylaseke_'for i in range(100, 0, -1)]
    text = 'ugra_' + ''.join(text)
    with open('key.txt', 'w', encoding='utf-8') as file:
        file.write(text)
print(first())
