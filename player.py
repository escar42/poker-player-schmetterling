
class Player:
    VERSION = "Schmetter 0.0.1"

    def betRequest(self, game_state):
        return game_state["current_buy_in"] - game_state["players"]["in_action"]["bet"]

    def showdown(self, game_state):
        pass

