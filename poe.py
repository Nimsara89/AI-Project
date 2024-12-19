import difflib

# Load the dictionary
with open('sinhala_dictionary.txt', 'r', encoding='utf-8') as file:
    dictionary = set(file.read().split(','))

def check_spelling(text):
    words = text.split()
    misspelled = [word for word in words if word not in dictionary]
    return misspelled

def suggest_corrections(misspelled):
    suggestions = {}
    for word in misspelled:
        close_matches = difflib.get_close_matches(word, dictionary, n=3)
        suggestions[word] = close_matches
    return suggestions

# Example usage
input_text = input("Enter text in Sinhala: ")
misspelled_words = check_spelling(input_text)
if misspelled_words:
    print("Misspelled words:", misspelled_words)
    suggestions = suggest_corrections(misspelled_words)
    for word, opts in suggestions.items():
        print(f"Suggestions for '{word}': {opts}")
else:
    print("No spelling errors found.")