from card import Card

class Director:
    def __init__(self):
        self.card = Card()
        self.userGuess = ""
        self.score = 300
        self.isPlaying = True

    def askToGuess(self):
        self.userGuess = input("Higher or lower? [h/l]: ")


    def startGame(self):
        while self.isPlaying:
            Card.newNumber(self)
            self.askToGuess()
            Card.nextNumber(self)
            self.calculateScore()
            self.getInputs()

    def calculateScore(self):
        if self.userGuess == "h":
            if self.card.nextValue > self.card.value: 
                self.score += 100
        elif self.userGuess == "l":
            if self.card.nextValue < self.card.value:
                self.score -= 75



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






