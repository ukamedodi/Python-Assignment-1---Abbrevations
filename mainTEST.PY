# this're' module is for regular expressions 
import re

# i then created my first function to load words from a file and convert them to uppercase
def loadWords(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # specifying for the code to read lines, remove leading/trailing whitespaces, and convert to uppercase
            lines = [line.strip().upper() for line in file.readlines()]
            # here i am converting the list of lines into a tuple
            tuple_of_lines = tuple(lines)
        # Return the tuple of lines
        return tuple_of_lines
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        return None

# Next function created to remove non-alphabetic characters from words
def removeCharacters(words_tuple):
    new_words_list = []
    for line in words_tuple:
        # now i check if the line is a single word with >(no spaces)
        if ' ' not in line:
            # Replace non-alphabetic characters with * as this is what was useful throughout the code
            cleaned_line = re.sub(r'[^a-zA-Z\s]', '*', line)
        else:
            # For compound words, replace non-alphabetic characters with a space (as specified in one of my test cases)
            cleaned_line = re.sub(r'[^a-zA-Z\s]', ' ', line)

        # Remove extra whitespaces
        cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
        # Append the cleaned line to the list
        new_words_list.append(cleaned_line)
    # Return the list of cleaned words
    return new_words_list

# the 3rd Function is to remove non-alphabetic characters from a single word
def removeCharactersFromWord(input_string):
    # then follow up to check if the input string is a single word (no spaces)
    if ' ' not in input_string:
        # Replace non-alphabetic characters with *
        cleaned_line = re.sub(r'[^a-zA-Z]', '*', input_string)
    else:
        # For compound words, replace non-alphabetic characters with a space
        cleaned_line = re.sub(r'[^a-zA-Z\s]', ' ', input_string)

    # Remove extra whitespaces as we have done so far 
    cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
    # Return the cleaned word
    return cleaned_line

# the 4th function to create abbreviations for each word
def createAbbreviations(words_tuple, result_tuple):
    abbreviations_map = {}
    idx = 0
    for line in words_tuple:
        words = line.split()

        word_length = len(line)
        if word_length >= 3:
            first_letter = line[0]
            abbreviations = set()

            for i in range(1, word_length - 1):
                for j in range(i + 1, word_length):
                    abbreviation = first_letter + line[i] + line[j]
                    # Check if the abbreviation contains only alphabets
                    if re.match("^[A-Za-z]+$", abbreviation):
                        abbreviations.add(abbreviation)
            # Add the individual word abbreviations to the map
            abbreviations_map[result_tuple[idx]] = list(set(abbreviations))
            idx += 1

    # Return the map of abbreviations
    return abbreviations_map

# the 5th function here to remove duplicate abbreviations from the map
def removeDuplicatesFromAbbreviationsMap(abbreviations_map):
    unique_abbreviations_map = {}
    abbreviation_to_words = {}

    # following up with building a dictionary mapping each abbreviation to the words containing it
    for word, abbreviations in abbreviations_map.items():
        for abbreviation in abbreviations:
            if abbreviation in abbreviation_to_words:
                abbreviation_to_words[abbreviation].append(word)
            else:
                abbreviation_to_words[abbreviation] = [word]

    # Filter out abbreviations that occur in more than one word
    for word, abbreviations in abbreviations_map.items():
        unique_abbreviations = [abbr for abbr in abbreviations if len(abbreviation_to_words[abbr]) == 1]
        unique_abbreviations_map[word] = unique_abbreviations

    # Return the map of unique abbreviations
    return unique_abbreviations_map

# 6th Function to determine rule indexes for each character in a word
def determineRuleIndexesForWord(sampleText):
    characterPositions = {}
    i = 0

    # Spliting the sampleText by space into a list of words
    words = sampleText.split()

    for word in words:
        word_length = len(word)
        for j in range(word_length):
            char = word[j]

            if j == 0:
                i = 0
            else:
                i += 1

            if i == word_length - 1 and len(word) > 1:
                i = -1

            if char not in characterPositions:
                characterPositions[char] = [i]
            else:
                characterPositions[char].append(i)

    # Return the character positions dictionary
    return characterPositions

# followed up with a 7th Function to map abbreviation characters to their rule indexes
def mapAbbreviationToRuleIndex(characterPositions, abbreviation):
    # Use list comprehension to map characters to their rule indexes
    return [characterPositions[char].pop(0) for char in abbreviation if char in characterPositions and characterPositions[char]]

# 8 th Function to load a score card from a file
def loadScoreCard(file_path):
    score_card = {}
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line, strip whitespaces, and split into key-value parts
            for line in file:
                parts = line.strip().split()
                # Check if there are two parts (key and value)
                if len(parts) == 2:
                    key, value = parts
                    # Convert the value to an integer and add to the score card dictionary
                    score_card[key] = int(value)
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred while loading the score card: {e}")

    # Return the score card dictionary
    return score_card

# 9th Function to compute scores based on the score card and abbreviations dictionary
def computeScore(score_card, abbrevs_dict):
    result = {}
    for word, abbreviations in abbrevs_dict.items():
        scoreData = {}
        for abbreviation in abbreviations:
            # Map abbreviation characters to their rule indexes
            abbreviationIndexes = mapAbbreviationToRuleIndex(determineRuleIndexesForWord(removeCharactersFromWord(word)), abbreviation)
            secondAbbrev = abbreviationIndexes[1]
            thirdAbbrev = abbreviationIndexes[2]
            # Compute scores based on rule indexes and score card values
            secondAbbrevScore = (
                0 if secondAbbrev == 0 else
                20 if secondAbbrev == -1 and abbreviation[1] == 'E' else
                5 if secondAbbrev == -1 else
                1 + score_card.get(abbreviation[1], 0) if secondAbbrev == 1 else
                2 + score_card.get(abbreviation[1], 0) if secondAbbrev == 2 else
                3 + score_card.get(abbreviation[1], 0)
            )
            thirdAbbrevScore = (
                0 if thirdAbbrev == 0 else
                20 if thirdAbbrev == -1 and abbreviation[2] == 'E' else
                5 if thirdAbbrev == -1 else
                1 + score_card.get(abbreviation[2], 0) if thirdAbbrev == 1 else
                2 + score_card.get(abbreviation[2], 0) if thirdAbbrev == 2 else
                3 + score_card.get(abbreviation[2], 0)
            )
            # Compute total abbreviation score
            abbreviationScore = 0 + secondAbbrevScore + thirdAbbrevScore
            # Print debug information
            print(abbreviation)
            print("\n"+str(secondAbbrevScore)+"\n"+str(thirdAbbrevScore)+"\n")
            # Add the abbreviation score to the score data dictionary
            scoreData[abbreviation] = abbreviationScore
        # Add the score data dictionary to the result dictionary
        result[word] = scoreData
    # Return the result dictionary
    return result

# Function to find the lowest scored abbreviations for each word
def find_lowest_scored_abbreviations(scores):
    lowest_scored_abbreviations = {}
    for word, scores_dict in scores.items():
        if scores_dict:  # Check if scores_dict is not empty
            # Find the minimum score
            min_score = min(scores_dict.values())

            # Find abbreviations with the minimum score
            min_score_abbreviations = [abbr for abbr, score in scores_dict.items() if score == min_score]

            # Join multiple abbreviations with commas
            min_score_abbreviation = ', '.join(min_score_abbreviations) if min_score_abbreviations else ' '
        else:
            # If scores_dict is empty, set min_score_abbreviation to ' '
            min_score_abbreviation = ' '

        # Add the lowest scored abbreviation to the dictionary
        lowest_scored_abbreviations[word] = min_score_abbreviation

    # Return the dictionary of lowest scored abbreviations
    return lowest_scored_abbreviations

# Function to write the lowest scored abbreviations to a file
def write_lowest_scored_abbreviations_to_file(lowest_scored_abbreviations, surname, input_file):
    # Generate the output file name based on surname and input file name
    output_file_name = f"{surname.lower()}_{input_file.split('.')[0]}_abbrevs.txt"

    try:
        # Open the output file in write mode
        with open(output_file_name, 'w') as output_file:
            for word, abbreviation in lowest_scored_abbreviations.items():
                # Write each word and its abbreviation to the output file
                output_file.write(f"{word}\n{abbreviation}\n")
        # Print a message indicating the successful write in terms of output
        print(f"Results written to {output_file_name}")
    except Exception as e:
        # Handle errors that may occur during writing to the file
        print(f"An error occurred while writing to the output file: {e}")


# Main execution block
if __name__ == "__main__":
    # Prompt the user to enter the txt file name
    file_path = input("Enter the txt file name: ")
    # Load words from the file and get a tuple of lines
    result_tuple = loadWords(file_path)

    # Check if result_tuple is not None
    if result_tuple is not None:
        # Remove non-alphabetic characters from each line in the tuple
        cleaned_words_list = removeCharacters(result_tuple)
        print("List of cleaned words:")
        for line in cleaned_words_list:
            print(line)
        # Create abbreviations for each word and print the result with duplicates
        abbreviations_result = createAbbreviations(cleaned_words_list, result_tuple)
        print("\nAbbreviations Map (with duplicates):")
        for word, abbreviations in abbreviations_result.items():
            print(f"{word}: {', '.join(abbreviations)}")
        # Remove duplicate abbreviations and print the result
        unique_abbreviations_result = removeDuplicatesFromAbbreviationsMap(abbreviations_result)
        print("\nAbbreviations Map (no duplicates):")
        for word, abbreviations in unique_abbreviations_result.items():
            print(f"{word}: {', '.join(abbreviations)}")

        # Load score card from values.txt
        score_card_path = 'values.txt'
        sample_score_card = loadScoreCard(score_card_path)

        # Compute scores and print debug information
        scores = computeScore(sample_score_card, unique_abbreviations_result)
        print("\nScores:")
        for word, scores_dict in scores.items():
            print(f"{word}: {scores_dict}")

        # Find the lowest scored abbreviations and print the result
        lowest_scored_abbreviations = find_lowest_scored_abbreviations(scores)
        print("Lowest Scored Abbreviations:")
        for word, abbreviation in lowest_scored_abbreviations.items():
            print(f"{word}: {abbreviation}")

        # Write the lowest scored abbreviations to a file as specified by assignment brief 
        surname = "Edodi"
        output_file_path = write_lowest_scored_abbreviations_to_file(lowest_scored_abbreviations, surname, file_path)
