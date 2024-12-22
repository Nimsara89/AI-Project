Spell Checker and Corrector 
Spell Checker Uses the Difflib Library for the purpose of spell Checking and correcting them. 
It provides suggestions based on the misspelled words by searching them through the 
dictionary and replaces them with the most probable word from the list. 
• Word Existence Check: 
o Checks if the input word exists in the given dictionary. 
o If the word exists, it directly returns the word. 
• Suggest Closest Match: 
o If the word is not found in the dictionary, it uses the get_close_matches 
function to find the closest match to the word in the dictionary. 
• Return Closest Suggestion: 
o If a close match is found, the function returns the closest suggestion. 
• Fallback to Original Word: 
o If no close match is found, the function returns the original word as is. 
Grammer Checker and Corrector 
The Grammar Checker has the following approach. We are using a rule-based approach to 
find and correct grammatical errors. The rules that are used to check grammar are as 
follows. 
1. Rule 1: Subject "මම" (I) 
o If the subject is "මම", the verb must end with "මි". 
o If the verb does not end with "මි", the function suggests a correction by 
replacing the verb ending with "මි". 
o If the verb already ends with "මි", the sentence is considered grammatically 
correct. 
2. Rule 2: Subject "අපි" (We) 
o If the subject is "අපි", the verb must end with "මු". 
o If the verb does not end with "මු", the function suggests a correction by 
replacing the verb ending with "මු". 
o If the verb already ends with "මු", the sentence is considered grammatically 
correct. 
3. Rule 3: Other Subjects 
o If the subject is not "මම" or "අපි", the verb must end with "යි". 
o If the verb does not end with "යි", the function suggests a correction by 
replacing the verb ending with "යි". 
o If the verb already ends with "යි", the sentence is considered grammatically 
correct. 
