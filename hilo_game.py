from card import Card
from score import Score

class Director:
    def __init__(self):
        self.card = Card()
        self.userGuess = ""
        self.score = Score()
        self.isPlaying = True

    def askToGuess(self):
        self.userGuess = input("Higher or lower? [h/l]: ")


    def startGame(self):
        while self.isPlaying:
            Card.display()
            self.askToGuess()
            self.score()
            self.getInputs()


    def getInputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        playAgain = input("Play again? [y/n]: ")
        if playAgain == "y":
            self.isPlaying 
        elif playAgain =="n":
            print ("Thank you. Good bye!")
            self.isPlaying = False
        else:
            print("wrong command, bye!")
            self.isPlaying = False






