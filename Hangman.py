import random

def menu():
    print("\"play\" to play the game, \"exit\" to quit:")
    if input() == "play":
        return 1
    return 0
        

tries = 8
history = set()
words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
while menu():
    s = random.choice(words)
    guess = '-' * (len(s))
    while tries:
        print("")
        print(guess)
        print("Input a letter:")
        letter = input()
        if 0 < len(letter) <= 1:
            if letter.islower():
                if letter in s and letter not in history:
                    for i in range(len(s)):
                        if s[i] == letter:
                            guess = guess[:i] + letter + guess[i+1:]
                            history.add(letter)
                            
                elif letter in history:
                    print("You already typed this letter")
                
    
                else:
                    print("No such letter in the word")
                    tries-=1
                    history.add(letter)
                    
            else:
                print("It is not an ASCII lowercase letter")
                history.add(letter)
        else:
            print("You should print a single letter")
            
        
        if '-' not in guess:
            print("You guessed the word!")
            print("You survived!\n")
            break
        
    if '-' in guess:
        print("You are hanged!\n")
    
        
    
    
                
