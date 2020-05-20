import random
            
words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
s = random.choice(words)
print(s)
guess = []
print(type(guess))
guess = '-' * (len(s))
while True:
    print("Input a letter:")
    letter = input()
    if letter in s:
        for i in range(len(s)):
            if s[i] == letter:
                guess = guess[:i] + letter + guess[i+1:]
                print(guess)
    print("You are hanged!")
