with open('index.html', 'r', encoding='utf-8-sig') as f:
    text = f.read()

text = text.replace('<meta charset="UTF-8">', '<meta charset="utf-8">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Saved without BOM')
