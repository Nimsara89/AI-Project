import difflib
def spell_corrector(word, dictionary):
    word = word.strip()
    if word in dictionary:
        return "Correct"
    else:
        matches = difflib.get_close_matches(word, dictionary, n=3, cutoff=0.8)
        if matches:
            return matches
        else:
            return "No suggestions available"
