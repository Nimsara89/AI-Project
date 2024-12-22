import difflib
def extract_words_from_comma_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Split the content by commas, strip whitespace, and convert to lowercase
            words = [word.strip().lower() for word in content.split(',') if word.strip()]
        return words
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{file_path}' not found.")
        return []

# Step 2: Spell corrector function
def spell_corrector(word, dictionary):
    # Normalize the input word by stripping spaces and converting to lowercase
    word = word.strip().lower()
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
            # If no suggestions, add the word as is and inform the user
            print(f"'{word}' is misspelled. No suggestions available.")
            corrected_words.append(word)
    # Join corrected words back into a sentence
    return " ".join(corrected_words)

# Step 4: Main code
word_file_path = "Dictionary.txt"  # Adjust file path as needed

# Load dictionary
sinhala_dict = extract_words_from_comma_file(word_file_path)
if not sinhala_dict:
    # Exit if the dictionary fails to load
    print("Failed to load the dictionary. Exiting.")
else:
    # Display the first 10 words of the loaded dictionary for verification
    print("Sinhala Dictionary Loaded:", sinhala_dict[:10], "...")

    # Interactive spell correction for sentences
    while True:
        # Prompt the user for a sentence
        sentence = input("Enter a sentence (or type 'exit' to quit): ").strip()
        if sentence.lower() == 'exit':
            # Exit the loop if the user types 'exit'
            print("Exiting the spell corrector.")
            break

        # Process the sentence and display the corrected version
        corrected_sentence = process_sentence(sentence, sinhala_dict)
        print("Corrected Sentence:", corrected_sentence)
