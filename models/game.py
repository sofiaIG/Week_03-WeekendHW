import random
class Game:
    def __init__(self):
        self.game = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

    def add_players_decision(self, choice):
        return choice


    def random_selection(self):
        list_of_selections =["rock", "paper", "scissors"]
        random_choice = random.choice(list_of_selections)
        return random_choice


    def output_of_game(self, players_move, opponents_move):
        for selection in self.game:
            if selection == opponents_move and self.game[selection] == players_move:
                return "loses"
            elif opponents_move == players_move:
                return None
            else:
                return "wins"

        
        