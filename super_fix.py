import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Emojis were broken into \ufffd. Let's fix them with context.
# We can just replace all \ufffd with nothing first, or replace specific patterns.

text = text.replace('A\ufffd', '·')
text = text.replace('12\ufffdC', '12°C')
text = text.replace('360\ufffd', '360°')
text = text.replace('\ufffd?"', '—') # em dash
text = text.replace('\ufffd+\'', '→')
text = text.replace('\ufffd,', '₹')
text = text.replace(' \ufffd?\ufffd?\ufffd', ' ════') # Day separators
text = text.replace('dYs-', '🚗')
text = text.replace('dY?~', '🐅')
text = text.replace('\ufffd>', '⛰')
text = text.replace('dY?"', '📍')
text = text.replace('dY"?', '📍')
text = text.replace('dYO', '🌿')
text = text.replace('dY?', '🍵')
text = text.replace('dYO,', '🌅')
text = text.replace('dYc', '🍲')
text = text.replace('\ufffdo.', '✅')
text = text.replace('\ufffdo^', '✈')
text = text.replace('\ufffd+-', '🌐')
text = text.replace('dYs,', '🚆')
text = text.replace('dYs"', '🚨')
text = text.replace('dY?3', '🍛')
text = text.replace('\ufffd', '') # Remove any other dangling replacement chars

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Super fixed!")
