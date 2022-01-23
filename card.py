import random

class Card:

    """display the cards radnomly.
    
    Atributes:
    value (int): the number guess
    points (int): the number points to track."""


    def __init__(self):
        self.newNum=True
        self.value=0
        

    
    def newNumber(self):
        """Generates a new number"""
        self.value = random.randint(1, 13)

    def display(self):
        return self.value
    
            
            
            

    

        
