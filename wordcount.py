def count_word(text_file):
    """Counts number of occurrences of each word in `text_file`."""

    # open file in line
    with open(text_file) as text_data:
        # read file to create string, replace new line chars with strings
        # then split into list of words
        words = text_data.read().replace("\n", " ").split(" ")
    
        # create a dictionary, loop thru each word, check if in dict
        counts_of_words = {}
        
        for word in words:
            # already in dict - create + add one, 
            # not already in dict - just add one
            counts_of_words[word] = counts_of_words.get(word, 0) + 1

    return counts_of_words
    

count_word("test.txt")
