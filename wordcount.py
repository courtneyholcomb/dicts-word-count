from collections import defaultdict

def count_word(text_file):
    """Counts number of occurrences of each word in `text_file`."""

    # open file in line
    with open(text_file) as text_data:
        # read file to create string, replace new line chars with strings
        # then split into list of words
        words = text_data.read().replace("\n", " ").split(" ")
    
        # create a dictionary, loop thru each word, check if in dict
        # counts_of_words = {}
        counts_of_words = defaultdict(int)
        # switched from using .get() on a normal dict
        # to defaultdict -> sets value of a new key to default 0 (for int)

        for word in words:
            # already in dict - create + add one, 
            # not already in dict - just add one
            # counts_of_words[word] = counts_of_words.get(word, 0) + 1
            counts_of_words[word] += 1

    del counts_of_words['']

    for word, count in dict(counts_of_words).items():
        print(word, count)

    

count_word("test.txt")
