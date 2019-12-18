import random  

def draw_hangman(i):
    Graphics =['''_____\n|/  |\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  / \\\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|  /\n|''',
    '''_____\n|/\n|   O\n|  /|\\\n|\n|''',
    '''_____\n|/\n|   O\n|  /|\n|\n|''',
    '''_____\n|/\n|   O\n|   |\n|\n|''',
    '''_____\n|/\n|   O\n|\n|\n|''',
    '''_____\n|/\n|\n|\n|\n|''',
    '']
    print(Graphics[i])

def pick_random_word():

    with open("words.txt", 'r') as f:
        words = f.readlines()

    index = random.randint(0, len(words) - 1)

    word = words[index].strip()
    return word


def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")

    return " ".join(output)

if __name__ == '__main__':
    WORD = pick_random_word()

    letters_to_guess = set(WORD)

    correct_letters_guessed = set()
    incorrect_letters_guessed = set()

    num_guesses = 8

    print("Welcome to Hangman!")
    while (len(letters_to_guess) > 0) and num_guesses > 0:
        guess = ask_user_for_next_letter()

        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue

        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses -= 1

        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(num_guesses))
        draw_hangman(num_guesses)

    if num_guesses > 0:
        print("Congratulations! You correctly guessed the word {}".format(WORD))
    else:
        print("Sorry, you lost! Your word was {}".format(WORD))
