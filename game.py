"""
Module to define the game First Orchard as a class.
"""

import random # to roll the die

class FirstOrchard:
    """
    The objective of the game is to collect all 16 fruits, 4 of 4 types, 
    before the crow moves 6 tiles. The starting positions are saved in
    class attributes.
    Two modes are defined about what to do when the die rolls a basket:
    'smart' picks one of the fruit with the highest count, while 'random' 
    picks any of the remaining fruits.
    Each round is played by calling the roll() method. The whole game is 
    played by calling the play_game() method. The export_summary() method
    returns a dictionary with information about the current state of the
    game. The game can be returned to its initial state with the reset_game()
    method.
    """
    def __init__(self, mode: str = "smart", verbose: bool = True):

        if mode not in ["smart", "random"]:
            raise ValueError("mode must be either 'smart' or 'random'")
        
        if verbose not in [True, False]:
            raise ValueError("verbose must be either True or False")

        self.mode = mode
        self.verbose = verbose
        self.green = 4
        self.red = 4
        self.yellow = 4
        self.blue = 4
        self.crow = 6
        self.game_state = "Game is on!"
        self.round = 0 # to count the number of rounds
    
    def roll(self):

        self.round += 1
        # check if game can be continued: has crow reached the end and are there still fruits left?
        # if not, update the game state accordingly, and assign an explanatory string to die_face
        if self.crow and (self.green or self.red or self.yellow or self.blue):
            die_face = random.choice(["blue", "green", "red", "yellow", "basket", "crow"])
            if self.verbose:
                print(f"You rolled {die_face}")
        elif self.crow == 0: # crow has reached the end
            self.game_state = "Game over. Crow won!"
            die_face = "Cannot roll. Game over. Crow won!"
        elif self.green == 0 and self.red == 0 and self.yellow == 0 and self.blue == 0: # no more fruits
            self.game_state = "Game over. Crow lost!"
            die_face = "Cannot roll. Game over. Crow lost!"

        # for each fruit, first check if there are any remaining:
        # if not, pass the turn, otherwise, decrease the count by 1
        # for crow, do the same by checking the number of tiles left
        if die_face == "blue":
            if self.blue > 0:
                self.blue -= 1
                if self.verbose:
                    print(f"Blue plums left: {self.blue}")
            elif self.verbose:
                print("No more blue plums. Roll again!")
        elif die_face == "green":
            if self.green > 0:
                self.green -= 1
                if self.verbose:
                    print(f"Green apples left: {self.green}")
            elif self.verbose:
                print("No more green apples. Roll again!")
        elif die_face == "red":
            if self.red > 0:
                self.red -= 1
                if self.verbose:
                    print(f"Red apples left: {self.red}")
            elif self.verbose:
                print("No more red apples. Roll again!")
        elif die_face == "yellow":
            if self.yellow > 0:
                self.yellow -= 1
                if self.verbose:
                    print(f"Yellow pears left: {self.yellow}")
            elif self.verbose:
                print("No more yellow pears. Roll again!")
        elif die_face == "crow":
            if self.crow > 0:
                self.crow -= 1
                if self.verbose:
                    print(f"Crow is getting closer: {self.crow} tiles left")
        elif die_face == "basket":
            name_map = {
                "blue plum": self.blue, 
                "green apple": self.green, 
                "red apple": self.red, 
                "yellow pear": self.yellow
            }
            # when the basket is rolled, the player can pick one of the remaining fruits:
            rem_fruits = [fruit for fruit in name_map if name_map[fruit] > 0]
            # in the random mode, no consideration is given the count of the remaining fruits:
            if self.mode == "random":
                if self.verbose:
                    print(f"Remaining fruit(s): {', '.join(rem_fruits)}")
                sel_fruit = random.choice(rem_fruits)
            # in the smart mode, the player picks one of the fruits with the highest count
            elif self.mode == "smart":
                rem_fruits_max = [fruit for fruit in name_map if name_map[fruit] == max(name_map.values())]
                if self.verbose:
                    print(f"Remaining fruit(s) with highest count: {', '.join(rem_fruits_max)}")
                sel_fruit = random.choice(rem_fruits_max)
            # after selection, the count is decreased by 1
            if sel_fruit == "blue plum":
                self.blue -= 1
                if self.verbose:
                    print(f"Selected blue plum, remaining: {self.blue}")
            elif sel_fruit == "green apple":
                self.green -= 1
                if self.verbose:
                    print(f"Selected green apple, remaining: {self.green}")
            elif sel_fruit == "red apple":
                self.red -= 1
                if self.verbose:
                    print(f"Selected red apple, remaining: {self.red}")
            elif sel_fruit == "yellow pear":
                self.yellow -= 1
                if self.verbose:
                    print(f"Selected yellow pear, remaining: {self.yellow}")
        else: # this happens when the game is already over, and die_face is assigned corresponding value
            if self.verbose:
                print(die_face)
    
    def play_game(self):
        while self.game_state == "Game is on!":
            self.roll()
    
    def reset_game(self):
        self.game_state = "Game is on!"
        self.round = 0
        self.green = 4
        self.red = 4
        self.yellow = 4
        self.blue = 4
        self.crow = 6
    
    def export_summary(self):
        summary = {
            "num_rounds" : self.round - 1,
            "result" : self.game_state, 
            "rem_blue" : self.blue,
            "rem_green" : self.green,
            "rem_red" : self.red,
            "rem_yellow" : self.yellow,
            "rem_crow_tiles" : self.crow
            }
        return summary