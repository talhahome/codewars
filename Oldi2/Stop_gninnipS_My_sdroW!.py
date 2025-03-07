# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    sentence = sentence.split(' ')
    for i in sentence:
        if len(i) >= 5:
            sentence[sentence.index(i)] = i[::-1]
    print(' '.join(sentence))

spin_words("Hey fellow warriors")

# Clever #
# def spin_words(sentence):
#     return ' '.join(i[::-1] if len(i) >= 5 else i for i in sentence.split(' '))
