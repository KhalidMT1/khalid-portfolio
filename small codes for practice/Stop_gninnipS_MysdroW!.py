# Practice:
# Write a function that takes in a string of
# one or more words, and returns the same string,
# but with all five or more letter words reversed
# (Just like the name of this Kata). Strings passed in
# will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    words_list = sentence.split()
    for word in range(len(words_list)):
        new_word = words_list[word]
        if len(new_word) >= 5:
            words_list[word] = new_word[::-1]
    new_sentence = " ".join(words_list)

    return new_sentence


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))