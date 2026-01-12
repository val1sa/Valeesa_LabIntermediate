# the secret word

secret_word = "six seven"

print("GUESS THE WORD")
guess = input("Give a letter")

if len(guess) == 1:

    if guess.lower() in secret_word:
        print("True! The letter is there.")

        answer = input("Now, guess the word: ")
        if answer.lower() == secret_word:
            print("You WIN, 67 67")
        else:
            print("You LOSE WOOOOO")

    else:
            print("False! Not in the word.")
else:
    print("Please enter only 1 letter!")