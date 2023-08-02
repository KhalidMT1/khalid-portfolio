# Practice:
# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string,
# and returns the same string with all even indexed characters in each word upper cased,
# and all odd indexed characters in each word lower cased.
# The indexing just explained is zero based, so the zero-ith index is even,
# therefore that character should be upper cased and you need to start over for each word.
# The passed in string will only consist of alphabetical
# characters and spaces(' '). Spaces will only be present if there are multiple words.
# Words will be separated by a single space(' ').

def to_weird_case(words):
    words_list = words.split()
    new_words = ''
    list_length = len(words_list)

    for word in words_list:
        for i in range(len(word)):
            if i % 2 == 0:
                new_words += word[i].upper()
            else:
                new_words += word[i].lower()
        if word != words_list[list_length-1]:
            new_words += ' '

    return new_words


print(to_weird_case('String'))
print(to_weird_case('Weird string case'))