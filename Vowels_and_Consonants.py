# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# Ex.
# Input: *depends on the user*
# Output:
# Words: 3
# Vowels: 6
# Consonants: 8

def words_vowels_consonants():
    user_words = input("Enter a word/words: ").lower()

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels_count = 0
    consonants_count = 0

    # word count
    word_count = len(user_words.split())
    print(f"Words: {word_count}")

    for vowel in user_words:
        if vowel in vowels:
            vowels_count += 1
    print(f"Vowels: {vowels_count}")

    for consonant in user_words:
        if consonant in consonants:
            consonants_count += 1
    print(f"Consonants: {consonants_count}")


words_vowels_consonants()

