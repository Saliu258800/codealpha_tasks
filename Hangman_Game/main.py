import random

words = ["Microsoft", "Meta", "OpenAI", "SpaceX", "Amazon"]

def get_word():
    word = random.choice(words)
    return word 
    
def main():
    
    num = 1
    secret = get_word()
    attempt = len(secret)
    
    progress = ["_"] * len(secret)
     
    while attempt > 0:
        
        print(f"You have {attempt} attempts to guess the right word")
        print(progress)
        user_input = input(f"> {num}: Enter the right letter: ").lower()
        if not user_input or user_input.isdecimal():
            continue
        if len(user_input) > 1:
            print("You have to enter only one letter!")
            continue 
            
        if user_input in secret.lower():
            for i, letter in enumerate(secret.lower()):
                if user_input == letter:
                    progress[i] = secret[i]  
                    
            if "_" not in progress:
                print("Word:", "".join(progress))
                print("You've won! Congratulations!!")
                break
        else:
            attempt -= 1
            num += 1
            
        if attempt <= 0:
            print("Sorry, You've lost...")
            print("The secret word is", secret)
    
if __name__ == "__main__":
    main()