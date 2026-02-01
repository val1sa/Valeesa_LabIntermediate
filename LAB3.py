def update_text(guess, secret_word):
    
    if guess in secret_word:
        print(f"Great! The letter '{guess}' is in the secret word!\n")
        return True
    else:
        print(f"Sorry, the letter '{guess}' is NOT in the secret word.\n")
        return False

def update_display_word(secret_word, guessed_letters):
   
    display_text = ""
    for letter in secret_word:
    
        if letter in guessed_letters:
            display_text += letter + " "
        else:
            display_text += "_ "
    return display_text.strip()

def main_game(secret_word):
    
    secret_word = secret_word.upper()
    guessed_letters = [] 
    chances = 5         
    
    print("=== WELCOME TO THE HANGMAN GAME ===")
    print(f"The secret word has {len(secret_word)} letters.")
    
    while chances > 0:
    
        current_display = update_display_word(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Chances left: {chances}")
        
        if "_" not in current_display:
            print("\n========================================")
            print(f"CONGRATULATIONS! You guessed the word: {secret_word}")
            print("YOU WIN!")
            print("========================================")
            return 

        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another one.")
            continue
        
        guessed_letters.append(guess)
        
        is_correct = update_text(guess, secret_word)
        
        if not is_correct:
            chances -= 1
            
    print("Oh no, you ran out of chances!")
    print(f"The secret word was: {secret_word}")
    print("GAME OVER.")

main_game("BANANA")