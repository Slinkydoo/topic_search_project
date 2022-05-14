import os


def auto_correct_word(word):  # already implemented, you need not do anything

    from autocorrect import Speller
    spell = Speller(lang='en')
    return spell(word)

#remove or improve autocorrect
# go through preprocess



def get_useful_words(preprocessed_string):
    # this separates the words in cleaned content into a list to be iterated over
    cleaned_content_words = preprocessed_string.split()
    # this creates a list of all the words that are not in stop words
    with open(os.path.join(os.getcwd(), 'stop_words.txt'), 'r', encoding='utf8') as stop_word_file:
        stop_word_file= stop_word_file.read()
        preprocessed_string = stop_word_file.split()
        useful_word_list = [word for word in cleaned_content_words if word not in preprocessed_string]

    return useful_word_list


def preprocess(original_content):
    # makes a DEEP copy of the original_content, so the original original_content remains unchanged
    cleaned_content = original_content[:]
    # made entire file lowercase to make comparisons easier
    cleaned_content = cleaned_content.lower()
    alphabet_string = "abcdefghijklmnopqrstuvwxyz '"

    # scanning the string from left to right, once you find a double space, replace all double spaces
    # with a single space, then continue from where you left off at this point we know all elements
    # to the left of that point do not have double spaces, so we do not need to check them again
    # now go through the rest of the string with this same logic

    # Here we are starting with the first character in the string
    character_index = 0

    # we find the length of the string
    last_index = len(cleaned_content)

    # this will run for as many characters exist in the string
    # we are constantly updating the length when elements are removed
    while character_index < (last_index-1):

        # if the current character under consideration is not in the defined string of wanted
        # characters it replaces all occurrences of that character in the entire string with a space
        if cleaned_content[character_index] not in alphabet_string:
            cleaned_content = cleaned_content.replace(cleaned_content[character_index], ' ')

        # if the character under consideration is a space and the character after it is a space
        # then we replace all double spaces in the string with a single space then move to the next character
        elif cleaned_content[character_index] == ' ' == cleaned_content[character_index+1]:
                cleaned_content = cleaned_content.replace('  ', ' ')
                last_index = len(cleaned_content)
        character_index += 1

    # cleaned_content = auto_correct_word(cleaned_content)
    return cleaned_content


def get_keywords(useful_word_list):
    possible_keywords_count = {}
    possible_keywords = []

    # in this loop we are counting the words that are in the useful_word_list
    # and adding them to a dictionary if they do not exist in it already
    # if they already exist then the count is increased by 1
    for word in useful_word_list:
        if word not in possible_keywords_count:
            possible_keywords_count[word] = 1
        else:
            possible_keywords_count[word] += 1

    # This loop goes through the dictionary to find the count of the word that is most frequent
    # this will be used in the following loop as a point to start from
    max_frequency = 0
    for word in possible_keywords_count:
        if possible_keywords_count[word] > max_frequency:
            max_frequency = possible_keywords_count[word]

    # This loop will run while there are at least six items in the possible_keywords
    # here old represents the current count we are comparing all counts to.
    old = max_frequency
    while len(possible_keywords) < 6: # need another condition here
        new = 0

        for word in possible_keywords_count:
            # if the word currently under consideration has the same count as the current max frequency
            # then add that word to the list
            if word not in possible_keywords and possible_keywords_count[word] == old:
                possible_keywords.append((word, possible_keywords_count[word]))

            # if the count of the word currently under consideration is less than the current old
            # and greater than the new at this point then that is the next frequency we check for
            # once the outer loop runs again
            elif new < possible_keywords_count[word] < old:
                new = possible_keywords_count[word]
        old = new

    return possible_keywords