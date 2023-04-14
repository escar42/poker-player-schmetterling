class Player:
    VERSION = "Schmetter 0.0.4"

    def betRequest(self, game_state):
        cards = game_state["players"][game_state["in_action"]]["hole_cards"]
        card1 = cards[0]
        card2 = cards[1]
        comcards_suits = []
        for comcard_suits in game_state["community_cards"]:
            comcards_suits.append(comcard_suits["suit"])

        # Check if there is a flush
        flush_suit = None
        for suit in ["spades", "hearts", "clubs", "diamonds"]:
            if sum(card["suit"] == suit for card in cards + game_state["community_cards"]) >= 5:
                flush_suit = suit
                break

        # Check if there is a two pair
        two_pairs = []
        for card in cards + game_state["community_cards"]:
            if sum(other_card["rank"] == card["rank"] for other_card in cards + game_state["community_cards"]) == 2:
                two_pairs.append(card["rank"])

        if flush_suit:
            if card1["suit"] == flush_suit and card2["suit"] == flush_suit:
                return game_state["players"][game_state["in_action"]]["stack"]
            else:
                return 0
        elif len(two_pairs) > 1:
            return game_state["players"][game_state["in_action"]]["stack"]
        elif game_state["current_buy_in"] > 500:
            return 0
        return (game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"])
