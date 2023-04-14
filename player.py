class Player:
    VERSION = "Zerschmetterling 1.2"

    def betRequest(self, game_state):
        cards = game_state["players"][game_state["in_action"]]["hole_cards"]
        card1 = cards[0]
        card2 = cards[1]
        
        comcards_suits = []
        comcards_ranks = []

        for comcard in game_state["community_cards"]:
            comcards_suits.append(comcard["suit"])
            comcards_ranks.append(comcard["rank"])

        # Check if there is a pair
        pair_rank = None
        for card in cards + game_state["community_cards"]:
            if sum(other_card["rank"] == card["rank"] for other_card in cards + game_state["community_cards"]) == 2:
                pair_rank = card["rank"]
                break

        # Straight
        def checkRank(rank):
            if rank in ["J", "Q", "K", "A"]:
                rank = 10
            else:
                rank = int(rank)
            return rank

        straight_list = []
        straight_list.append(checkRank(card1["rank"]))
        straight_list.append(checkRank(card2["rank"]))

        if len(straight_list) > 2:
            for comcard_rank in comcards_ranks:
                straight_list.append(checkRank(comcard_rank))

            straight_list.sort()
            for i in range(len(straight_list)-1):
                if straight_list[i] == straight_list[i+1] - 1:
                    pass
                else:
                    break
            if len(straight_list) == i + 1:
                return 2 * game_state["current_buy_in"]

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

        # Check if there is a triple
        triple_rank = None
        for card in cards + game_state["community_cards"]:
            if sum(other_card["rank"] == card["rank"] for other_card in cards + game_state["community_cards"]) == 3:
                triple_rank = card["rank"]
                break

        if pair_rank and checkRank(pair_rank) <= 8:
            return 0
        elif pair_rank:
            if pair_rank in [card1["rank"], card2["rank"]]:
                return (game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"]) + 100
            else:
                return 0
        elif flush_suit:
            if card1["suit"] == flush_suit and card2["suit"] == flush_suit:
                return 3 * game_state["current_buy_in"]
            else:
                return 0
        elif len(two_pairs) > 1:
            return int(2.5 * game_state["current_buy_in"])
        elif triple_rank:
            if triple_rank in [card1["rank"], card2["rank"]]:
                return 2 * game_state["current_buy_in"]
            elif game_state["current_buy_in"] <= 50:
                return 2 * game_state["current_buy_in"]
            else:
                return 0
        elif len(comcards_suits) <= 2:
            if game_state["current_buy_in"] > 300:
                return 0
        elif len(comcards_suits) == 3:
            if game_state["current_buy_in"] > 100:
                return 0
        elif len(comcards_suits) == 4:
            if game_state["current_buy_in"] > 50:        
                return 0
        elif len(comcards_suits) == 5:
            if game_state["current_buy_in"] > 0:        
                return 0  
        return (game_state["current_buy_in"] - game_state["players"][game_state["in_action"]]["bet"])

    def showdown(self, game_state):
            pass
