
from data import DICTIONARY, LETTER_SCORES

def load_words():
    words = []
    dictionary = open(DICTIONARY, 'r')

    for line in dictionary.readlines():
        line = line.rstrip()
        words.append(line)

    dictionary.close()
    return words
    
def calc_word_value(word):
    letters = []
    value = []
    for letter in word:
        letters.append(letter)

    for char in LETTER_SCORES:
        for letter in letters:
            if letter.lower() == char.lower():
                value.append(LETTER_SCORES.get(char))
        else:
            pass
    
    score = sum(value)
    return score

 def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    dictionary = load_words()
    all_scores = {}
    for word in dictionary:
        score = calc_word_value(word)
        all_scores.update({word : score})
    
    return max(zip(all_scores.values(), all_scores.keys()))

# if __name__ == "__main__":
    # pass # run unittests to validate



value = max_word_value()

print(value)
