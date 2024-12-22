# Read the file
with open('D:\Python Sem 6\Dictionary.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Extract Sinhala words
import re

sinhala_words = []
for line in lines:
    # Split line into potential Sinhala words
    words = line.split('-')  # Adjust delimiter based on format
    for word in words:
        # Check if the word contains only Sinhala characters
        if re.fullmatch(r'[\u0D80-\u0DFF]+', word.strip()):
            sinhala_words.append(word.strip())

# Remove duplicates and sort
unique_sinhala_words = sorted(set(sinhala_words))

# Save to a text file
with open('D:\Python Sem 6\Dictionary.txt', 'w', encoding='utf-8') as file:
    file.write(','.join(unique_sinhala_words))
