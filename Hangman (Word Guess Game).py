import random

# List of words
words = ["python", "hangman", "developer", "computer", "science", "programming"]

# Choose random word
word = random.choice(words)
guessed_letters = []
tries = 6

# Display function
def display_word():
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while tries > 0:
    print("\nWord:", display_word())
    print("Tries left:", tries)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        print("❌ Wrong guess!")
        tries -= 1

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You Win!")
        print("The word was:", word)
        break

# Check lose
if tries == 0:
    print("\n💀 You Lost!")
    print("The word was:", word)
