from symspellpy import SymSpell, Verbosity

# Initialize SymSpell object
def initialize_spell_checker(dictionary_path):
    max_edit_distance_dictionary = 2  # Maximum distance for fuzzy matching
    prefix_length = 7  # Prefix length for SymSpell
    sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance_dictionary, prefix_length=prefix_length)

    # Load the custom Sinhala dictionary
    if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
        print("Error loading dictionary.")
        return None
    return sym_spell

# Check for misspelled words
def check_and_correct_text(sym_spell, input_text):
    corrected_text = []
    misspelled = []
    words = input_text.split()

    for word in words:
        # Get suggestions for each word
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            # Append the best suggestion if corrections exist
            corrected_text.append(suggestions[0].term)
        else:
            # Append the original word if no suggestion is found
            corrected_text.append(word)
            misspelled.append(word)

    return misspelled, " ".join(corrected_text)

# Main workflow
dictionary_path = "sinhala_dictionary.txt"  # Ensure dictionary is in a compatible format: word <TAB> frequency
sym_spell = initialize_spell_checker(dictionary_path)

if sym_spell:
    input_text = input("Enter text in Sinhala: ")
    misspelled_words, corrected_text = check_and_correct_text(sym_spell, input_text)
    if misspelled_words:
        print("Misspelled words:", misspelled_words)
        print("Corrected text:", corrected_text)
    else:
        print("No spelling errors found.")
