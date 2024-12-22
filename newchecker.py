from rapidfuzz.distance import Levenshtein

# Load Sinhala dictionary
def load_dictionary(file_path):
    with open(file_path, encoding="utf-8") as f:
        return set(line.strip() for line in f)

# Tokenize a Sinhala sentence into words
def tokenize(sentence):
    # Basic whitespace-based tokenization
    return sentence.strip().split()

# Check if a word is correctly spelled
def is_correct(word, dictionary):
    return word in dictionary

# Generate spelling suggestions for a single word
def get_suggestions(word, dictionary, max_suggestions=5, max_distance=2):
    suggestions = []
    for valid_word in dictionary:
        distance = Levenshtein.distance(word, valid_word)
        if distance <= max_distance:  # Only consider words within a max distance
            suggestions.append((valid_word, distance))
    
    # Sort suggestions by distance and alphabetically
    suggestions.sort(key=lambda x: (x[1], x[0]))
    
    # Return top suggestions
    return [s[0] for s in suggestions[:max_suggestions]]

# Correct a sentence
def correct_sentence(sentence, dictionary):
    words = tokenize(sentence)
    corrected_words = []
    suggestions_dict = {}

    for word in words:
        if is_correct(word, dictionary):
            corrected_words.append(word)  # Keep the original word if it's correct
        else:
            # Generate suggestions and pick the best match
            suggestions = get_suggestions(word, dictionary)
            if suggestions:
                best_match = suggestions[0]  # Choose the highest-ranked suggestion
                corrected_words.append(best_match)
                suggestions_dict[word] = suggestions  # Save suggestions for display
            else:
                corrected_words.append(word)  # If no suggestions, keep the original word

    # Join corrected words into a sentence
    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence, suggestions_dict

# Main Script
if __name__ == "__main__":
    # Path to Sinhala dictionary
    dictionary_path = r"Dict.txt"

    # Load the dictionary
    sinhala_words = load_dictionary(dictionary_path)

    # Input sentence
    input_sentence = "ලංකාව ඉන්ඩියන් සකාගරයෙන් වරවී ඇක"

    # Correct the sentence
    corrected_sentence, suggestions = correct_sentence(input_sentence, sinhala_words)

    # Display results
    print("Original Sentence:", input_sentence)
    print("Corrected Sentence:", corrected_sentence)
    print("Suggestions for Misspelled Words:")
    for word, suggestion_list in suggestions.items():
        print(f"  {word}: {', '.join(suggestion_list)}")
