import random
words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
s = random.choice(words)
print("Guess the word:", s[:3]+ '-' * (len(s) - 3 ))
if s == input():
    print("You survived!")
else:
    print("You are hanged!")
