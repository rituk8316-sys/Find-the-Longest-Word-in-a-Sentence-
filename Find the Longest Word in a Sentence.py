# Find the longest word in a sentence

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


# Input
sentence = "Python programming is very interesting"

# Function call
result = find_longest_word(sentence)

# Output
print("Longest word is:", result)
