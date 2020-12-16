#import library
import mathstropy

#greet the player
print("thanks for playing this guessing game!\n")

#generate a random word
random_word = mathstropy.randomword()

#mask the random word
mask_word = mathstropy.wordmask(random_word)
print(mask_word)

#ask player to guess
guess = input("please guess the word above from the given values:")

#impliment the while loop for guessing
while(guess.lower() != random_word.lower()):
    print("your guess is incorrect. Sorry!")
    guess = input("please guess again:")


#print congratulations
print("congratulations you guessed correctly!")

#replay

play_again = input("do you want to play again? (yes or no)")

if play_again == "yes":
    random_word = mathstropy.randomword()
    mask_word = mathstropy.wordmask(random_word)
    print(mask_word)
    guess_2 = input("please guess the word above from the given values:")
    while(guess_2.lower() != random_word.lower()):
        print("your guess is incorrect. Sorry!")
        guess_2 = input("please guess again:")
    print("congratulations, you guessed correctly! thanks for playing!")
else:
    print("okay, thanks for playing!")

