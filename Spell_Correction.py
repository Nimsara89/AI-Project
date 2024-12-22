import difflib
def extract_words_from_comma_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            words = [word.strip().lower() for word in content.split(',') if word.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    #spell correction
def spell_corrector(word, dictionary):
    word = word.strip().lower()  
    if word in dictionary:
        return "Correct"
    else:
        matches = difflib.get_close_matches(word, dictionary, n=3, cutoff=0.8)
        if matches:
            return matches
        else:
            return "No suggestions available"


word_file_path = "Dict.txt" 
sinhala_dict = extract_words_from_comma_file(word_file_path)
if not sinhala_dict:
    print("Failed to load the dictionary. Exiting.")
else:
    print("Sinhala Dictionary Loaded:", sinhala_dict[:10], "...") 

    while True:
        misspelled_word = input("Enter a word (or type 'exit' to quit): ").strip()
        if misspelled_word.lower() == 'exit':
            print("Exiting the spell corrector.")
            break

        result = spell_corrector(misspelled_word, sinhala_dict)
        if result == "Correct":
            print(f"'{misspelled_word}' is a correct word!")
        elif isinstance(result, list):
            print(f"'{misspelled_word}' is misspelled. Suggest word(s): {', '.join(result)}")
        else:
            print(f"'{misspelled_word}' is misspelled. {result}")
