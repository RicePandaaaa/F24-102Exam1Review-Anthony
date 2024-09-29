# Take in secret word (min length is 6)
password = input("Enter the secret word: ")

while len(password) < 6:
    password = input("Enter the secret word: ")

# Guessing loop
guess = input("Guess a letter: ")
guesses = 1

while guess in password:
    guess = input("Guess another letter: ")
    guesses += 1

# Output
print(f"The secret word is: \"{password}\". You took {guesses} guesses!")

