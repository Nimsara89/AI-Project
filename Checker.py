import re
from symspellpy import SymSpell, Verbosity

# Path to your comma-separated Sinhala dictionary file
dictionary_path = "D:\\Python Sem 6\\AI Project\\sinhala_dictionary.txt"

# Initialize SymSpell
def initialize_symspell(dictionary_path, max_edit_distance=2, prefix_length=7):
    sym_spell = SymSpell(max_dictionary_edit_distance=max_edit_distance, prefix_length=prefix_length)
    # Load the dictionary file with UTF-8 encoding
    if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1, separator=","):
        raise FileNotFoundError(f"Dictionary file not found or could not be loaded from {dictionary_path}")
    return sym_spell


# Function to correct a paragraph
def correct_paragraph(paragraph, sym_spell):
    # Split the paragraph into words (using regex to keep punctuation)
    words = re.findall(r'\w+|[^\w\s]', paragraph)
    
    # Correct each word using SymSpell
    corrected_words = []
    for word in words:
        # Skip punctuation or symbols that are not words
        if re.match(r'^\W+$', word):
            corrected_words.append(word)
            continue
        
        # Get the best correction
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)  # Use the original word if no suggestions
    
    # Join the corrected words back into a paragraph
    corrected_paragraph = ''.join([
        f" {w}" if not re.match(r'^\W$', w) and corrected_words[i - 1] not in ['(', '[', '{'] else w
        for i, w in enumerate(corrected_words)
    ]).strip()
    
    return corrected_paragraph

# Main execution
if __name__ == "__main__":
    # Initialize SymSpell
    sym_spell = initialize_symspell(dictionary_path)
    
    # Example paragraph
    test_paragraph = "මෙය අකෘ දෙසැම්බර් අරමුණයි. එය වැරදි ගමනක් බවයි."
    
    # Correct the paragraph
    corrected_paragraph = correct_paragraph(test_paragraph, sym_spell)
    
    print(f"Original Paragraph: {test_paragraph}")
    print(f"Corrected Paragraph: {corrected_paragraph}")
