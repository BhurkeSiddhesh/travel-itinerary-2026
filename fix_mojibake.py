with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('â€”', '—')
text = text.replace('â€œ', '“')
text = text.replace('â€\u009d', '”')
text = text.replace('â€™', '’')
text = text.replace('ðŸš—', '🚗')
text = text.replace('ðŸŒ¿', '🌿')
text = text.replace('ðŸ\u008f¨', '🏨')
text = text.replace('ðŸ\u008d´', '🍴')
text = text.replace('â‚¹', '₹')
text = text.replace('â†’', '→')
text = text.replace('A\u009d', '”')
text = text.replace('', '·')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Mojibake fixed via script!')
