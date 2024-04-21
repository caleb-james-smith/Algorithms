# play_guessing_game.py

# TODO:
# - improve error catching
# - check for valid inputs from user (int in range)

from random import randrange

# guessing game
class GuessingGame:
    def __init__(self):
        return

    # compare guess to answer
    def evaluate(self, guess, answer):
        if guess < answer:
            return 1
        elif guess > answer:
            return -1
        elif guess == answer:
            return 0
        else:
            print(f"ERROR: Did not find valid comparison for guess {guess} and answer {answer}.")
            return -999
    
    # play guessing game
    def play(self):
        answer = randrange(1,101)
        print("-----------------------------------------------")
        print("It is time to play the guessing game!")
        print("Your goal is to guess the number that I select.")
        print("I have selected a number in range 1 to 100.")
        print("Let the game begin!")
        print("-----------------------------------------------")
        
        game_is_over = False
        while not game_is_over:
            guess = input("Please enter your guess: ")
            guess = int(guess)
            eval = self.evaluate(guess, answer)
            if eval == 1:
                print("Higher...")
            elif eval == -1:
                print("Lower...")
            elif eval == 0:
                print("Correct!")
                game_is_over = True
            else:
                print("ERROR: Evaluation failed.")
        return

def main():
    game = GuessingGame()
    game.play()

if __name__ == '__main__':
    main()
