from ast import Num
from cmd import PROMPT
import random

class Card:

    """display the cards randomly way.
    
    Atributes:
    value (int): the number guess
    points (int): the number ponints to track."""


    def __init__(self):
        self.newNum=True
        self.value=0
        

    
    def newNumber(self):
        """Generates a new number"""

        value=0
        self.value = random.randint(1, 13)

    def display(self):
        return self.value
    
            
            
            

    

        
