import difflib
def spell_corrector(word, dictionary):
    word = word.strip()
    if word in dictionary:
        # If the word exists in the dictionary, it is correct
        return "Correct", word
    else:
        # Use difflib to find close matches to the misspelled word
        matches = difflib.get_close_matches(word, dictionary, n=3, cutoff=0.8)
        if matches:
            # Return suggestions if matches are found
            return "Suggestions", matches
        else:
            # Indicate no suggestions available
            return "No suggestions", None

# Step 3: Process a sentence
def process_sentence(sentence, dictionary):
    corrected_words = []  # List to store corrected words
    # Split the sentence into individual words
    for word in sentence.split():
        # Check each word using the spell corrector
        status, result = spell_corrector(word, dictionary)
        if status == "Correct":
            # If the word is correct, add it as is
            corrected_words.append(word)
        elif status == "Suggestions":
            # If suggestions are available, display them to the user
            print(f"'{word}' is misspelled. Suggestions: {', '.join(result)}")
            # Allow the user to select a replacement or keep the original
            choice = input(f"Choose a replacement for '{word}' or press Enter to keep it as is: ").strip()
            corrected_words.append(choice if choice else word)
        else:
            return "No suggestions available"
