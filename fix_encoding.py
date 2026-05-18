import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace corrupted characters
replacements = {
    'A': '°',
    '?"': '—',
    '+\'': '→',
    ',': '₹',
    ' ?': '═',
    'dYs-': '🚗',
    'dY?~': '🐅',
    '>': '⛰',
    'dY?"': '📍',
    'dY"?': '📍',
    'dYO': '🌿',
    'dY?': '🍵',
    'dYO,': '🌅',
    'dYc': '🍲',
    'o.': '✅',
    'o^': '✈',
    '+-': '🌐',
    'dYs,': '🚆',
    'dYs"': '🚨',
    'dY?3': '🍛',
}

for k, v in replacements.items():
    text = text.replace(k, v)

# Fix some specifics that might be messed up
text = text.replace('°C', '°C').replace('°C°C', '°C')
text = text.replace('Day 7 ° Tuesday', 'Day 7 · Tuesday')
text = text.replace('Day 8 ° Wednesday', 'Day 8 · Wednesday')
text = text.replace('Ooty ° Coonoor ° Tea ° Trains', 'Ooty · Coonoor · Tea · Trains')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done replacing.')
