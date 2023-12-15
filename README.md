# Python-Assignment-1---Abbrevations
This is my python assignment Repo to be submitted for marking 


Objective:
The provided Python code effectively meets the specified conditions for reading a file containing names, generating three-letter abbreviations, scoring them based on predefined rules, and outputting the results to a file. Below is an analysis of how each condition is satisfied:

File Input and Output:

The code utilizes the loadWords function to read a file with a list of names, ensuring that it handles potential file-related errors, such as FileNotFoundError. The write_lowest_scored_abbreviations_to_file function generates an output file with the correct naming convention.
Character Cleaning:

The removeCharacters function uses regular expressions to clean non-alphabetic characters, ensuring that the abbreviations consist entirely of uppercase letters. Apostrophes are correctly ignored.
Abbreviation Generation:

The createAbbreviations function generates three-letter abbreviations for each name, following the specified rules. It correctly considers the first letter and subsequent two letters, excluding undesirable combinations.
Duplicate Exclusion:

The code effectively removes abbreviations that can be formed from more than one name, ensuring that the output contains unique abbreviations for each name.
Scoring Mechanism:

The computeScore function accurately calculates scores for each abbreviation based on the defined rules. The scores reflect the position of letters in a word and their commonness in English.
Handling Multiple Abbreviations:

In cases where an abbreviation can be formed in more than one way, the code correctly selects the one with the lowest score, as required.
Output Format:

The output file includes the original names and their corresponding abbreviations, following the specified format. If there is no acceptable abbreviation for a name, a blank line is included.
User Interaction:

The main function prompts the user for the input filename, interacts with the user throughout the process, and provides informative messages, enhancing user experience.
Data Structures and Iteration:
The code utilizes tuples, lists, and dictionaries appropriately. Loops and iterators are employed efficiently for iterating over lines, words, and positions within words.
 
