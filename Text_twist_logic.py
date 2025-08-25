import random
import os


def shuffle_letters(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


text = {
    2: {'as', 'me', 'he', 'am'},
    3: {'ash', 'ham', 'she'},
    4: {"same", "seam", "sham"},
    5: {"shame"}
}

word = "SHAME"
shuffled = shuffle_letters(word)

guessed = set()
all_words = set(word for group in text.values() for word in group)

score = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TEXT TWIST GAME ===")
    print(f"Your letters: {shuffled}")
    print(f"Score: {score}\n")

    print("Words left to guess:")
    for length, words in text.items():
        line = []
        for w in words:
            if w in guessed:
                line.append(w)
            else:
                line.append("_" * length)
        print(f"{length}-letter words: {' '.join(line)}")

    if guessed == all_words:
        print("\n Congratulations! You found all the words!")
        print(f"Final Score: {score}")
        break

    guess = input("\nEnter a word (or 'shuffle', 'quit'): ").lower()

    if guess == "quit":
        print("\nGame over. Thanks for playing!")
        print(f"Final Score: {score}")
        break
    elif guess == "shuffle":
        shuffled = shuffle_letters(word)
        continue

    if guess in all_words and guess not in guessed:
        print("Correct!")
        guessed.add(guess)
        score += len(guess) * 10
    elif guess in guessed:
        print("You already guessed that word!")
    else:
        print("Not a valid word.")

    input("\nPress Enter to continue...")
