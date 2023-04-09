import random
import string

def generate_password(num_words=2):
    """Generate a random password made up of random words."""

    words = []

    # Load a list of words from a text file
    with open('words.txt', 'r') as f:
        for word in f.readlines():
            words.append(word.strip())

    # Randomly select the specified number of words
    selected_words = random.sample(words, num_words)

    selected_words += random.choice(string.digits)
    selected_words += random.choice(string.punctuation)

    random.shuffle(selected_words)

    # Combine the selected words into a single string
    password = ''.join(selected_words)

    return password