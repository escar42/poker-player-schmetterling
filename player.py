
class Player:
    VERSION = "Schmetter 0.0.1"

    def betRequest(self, game_state):
        cards = game_state["players"][game_state["in_action"]]["hole_cards"]
        card1 = cards[0]
        card2 = cards[1]
        comcards_suits = []
        for comcard_suits in game_state["community_cards"]:
            comcards_suits.append(comcard_suits["suit"])
        
        if card1["suit"] == card2["suit"] or if card1["suit"] in comcards_suits or if card2[suit] in comcards_suits:
            return game_state["players"][game_state["in_action"]]["stack"]
        elif game_state["current_buy_in"] > 500:
            return 0
        return (game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"])

    def showdown(self, game_state):
        pass

