# import random
#
# print("H A N G M A N")
#
# words = ["python", "java", "kotlin", "javascript"]
# answer = random.choice(words)
#
# tries = 8
# guessed = set()
# guess = ""
# answer_wordset = set(answer)
#
# while tries > 0 and not answer_wordset.issubset(guessed):
#     print()
#
#     print("".join([i if i in guessed else "-" for i in answer]))
#     guess = str(input("Input a letter: "))
#
#     if len(guess) != 1:
#         print("You should input a single letter")
#     elif guess in guessed:
#         print("You've already guessed this letter")
#     elif not guess.islower():
#         print("Please enter a lowercase English letter")
#     elif guess not in answer_wordset and guess not in guessed:
#         print("That letter doesn't appear in the word")
#         tries -= 1
#
#     guessed.add(guess)
#
# print("You lost!" if not answer_wordset.issubset(guessed) else "You guessed the word " + answer + "!\nYou survived!")

import random

print("H A N G M A N")

while True:
    option = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if option == "play":
        words = ['python', 'java', 'kotlin', 'javascript']
        chosen = random.choice(words)
        letters = set(chosen)
        answer = list("-" * len(chosen))
        attempts = []
        lives = 8

        while lives > 0:
            print("\n" + ''.join(answer))
            guess = input("Input a letter:")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not guess.islower():
                print("Please enter a lowercase English letter")
            elif guess in attempts:
                print("You've already guessed this letter")
            elif guess in letters:
                attempts.append(guess)
                pos = chosen.find(guess)
                while pos != -1:
                    answer[pos] = guess
                    pos = chosen.find(guess, pos + 1)
                    if ''.join(answer) == chosen:
                        break
            else:
                attempts.append(guess)
                print("That letter doesn't appear in the word")
                lives -= 1
        print(f"You guessed the word {chosen}!\nYou survived!") if lives > 0 else print("You lost!")
    elif option == "exit":
        break
