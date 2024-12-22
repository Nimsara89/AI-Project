import difflib

# Load the dictionary
with open('Dict.txt', 'r', encoding='utf-8') as file:
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

def correct_text(text, suggestions):
    words = text.split()
    corrected_words = []
    for word in words:
        if word in suggestions:
            # Use the best suggestion if available, otherwise keep the original word
            corrected_words.append(suggestions[word][0] if suggestions[word] else word)
        else:
            corrected_words.append(word)
    return ' '.join(corrected_words)

# Example usage
input_text = input("Enter text in Sinhala: ")
misspelled_words = check_spelling(input_text)
if misspelled_words:
    print("Misspelled words:", misspelled_words)
    suggestions = suggest_corrections(misspelled_words)
    for word, opts in suggestions.items():
        print(f"Suggestions for '{word}': {opts}")
    corrected_text = correct_text(input_text, suggestions)
    print("Corrected text:", corrected_text)
else:
    print("No spelling errors found.")
