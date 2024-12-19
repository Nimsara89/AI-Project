import os
from symspellpy.symspellpy import SymSpell, Verbosity

# Initialize SymSpell with default parameters
max_edit_distance = 2
prefix_length = 7
sym_spell = SymSpell(max_edit_distance, prefix_length)

# Path to the preprocessed Sinhala dictionary file
dictionary_path = "sinhala_dict.txt"

# Load the dictionary
if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
    print("Failed to load dictionary file.")
    exit()

# Function to correct a given Sinhala sentence
def correct_sentence(input_sentence):
    words = input_sentence.split()
    corrected_words = []

    for word in words:
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)
    
    return " ".join(corrected_words)

# Example usage
input_sentence = "ඔබේ වැරදි වාක්‍යයකි"
corrected_sentence = correct_sentence(input_sentence)
print("Original:", input_sentence)
print("Corrected:", corrected_sentence)
