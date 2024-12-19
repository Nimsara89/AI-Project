# spell_checker.py
from symspellpy import SymSpell, Verbosity

# Initialize SymSpell
max_edit_distance = 2  # Maximum number of edits
prefix_length = 7  # Prefix length for indexing
sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)

# Function to load words with default frequency (1)
def load_dictionary_with_default_frequency(path):
    with open(path, "r", encoding="utf-8") as file:
        words = file.read().split(',')
    
    # Prepare the words with a default frequency of 1
    word_list = [(word.strip(), 1) for word in words if word.strip()]
    
    # Add words to SymSpell
    for word, frequency in word_list:
        sym_spell.create_dictionary_entry(word, frequency)

# Function to correct individual word
def correct_spelling(word):
    suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=max_edit_distance)
    if suggestions:
        # Get the closest suggestion (first item in the list)
        corrected_word = suggestions[0].term
        return corrected_word
    else:
        return word  # Return the original word if no correction is found

