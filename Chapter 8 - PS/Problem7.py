# Write a python function to remove a given word from a list and strip it at the same time.


def remove_word_from_list(word_list, word_to_remove):
    number = []
    for word in word_list:
        if not (word == word_to_remove):
            number.append(word.strip(word_to_remove))
    return number


word_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(remove_word_from_list(word_list, "abc"))
