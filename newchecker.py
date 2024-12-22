import difflib

# Load the dictionary
with open('Dict.txt', encoding='utf-8') as file:
    sinhala_dict = set(file.read().split(','))

def spell_check_and_correct(text):
    words = text.split()
    corrected_text = []
    for word in words:
        if word in sinhala_dict:
            corrected_text.append(word)
        else:
            suggestions = difflib.get_close_matches(word, sinhala_dict, n=3, cutoff=0.8)
            if suggestions:
                corrected_text.append(suggestions[0])  # Automatically use the best suggestion
            else:
                corrected_text.append(word)  # Leave as is if no suggestion found
    return ' '.join(corrected_text)

# Example Usage
input_text = "ලංකව ඉන්දයන් සගරයෙන් වටව ඇත"
corrected_text = spell_check_and_correct(input_text)
print("Corrected Text:", corrected_text)
