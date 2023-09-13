#Par Maxime
# TP1

# variables (permet de compter le nb de mots)
def count_words_and_characters(input_string):
    word_count = len(input_string.split())

    character_count = len(input_string)
    return word_count, character_count


#écrire une phrase
input_text = input("Écriver une phrase: ")
word_count, character_count = count_words_and_characters(input_text)


# afficher le nb de mots et de characteres
print(f"Word count: {word_count}")
print(f"Character count: {character_count}")
