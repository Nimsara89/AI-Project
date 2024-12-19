# Convert a comma-separated list of words into the required format
input_file = "AI Project/sinhala_dictionary.txt"  # Your original comma-separated list
output_file = "sinhala_dict.txt"  # Output file in SymSpell format

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    words = infile.read().strip().split(",")
    for word in words:
        outfile.write(f"{word.strip()}\t1\n")  # Assign a frequency of 1
