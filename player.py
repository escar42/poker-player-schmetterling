class Player:
    VERSION = "Schmetter 0.0.7"

    def betRequest(self, game_state):
        cards = game_state["players"][game_state["in_action"]]["hole_cards"]
        card1 = cards[0]
        card2 = cards[1]
        
        comcards_suits = []
        comcards_ranks = []

        for comcard in game_state["community_cards"]:
            comcards_suits.append(comcard["suit"])
            comcards_ranks.append(comcard["rank"])

            
        #straight
        def checkRank(rank):
            if rank == "jogger":
                rank = 11
            if rank == "queen":
                rank = 12
            if rank == "king":
                rank = 13
            if rank == "ace":
                rank = 14
            return rank
            
        strightlist = []
        strightlist.append(checkRank(card1["rank"]))
        strightlist.append(checkRank(card2["rank"]))
        for comcard_rank in comcards_ranks:
            strightlist.append(checkRank(comcard_rank))
           
        strightlist.sort()
        for i in range(5):
            if strightlist[i+1] == strightlist[i] + 1:
                pass
            else:
                break
        if i == 4:
            return game_state["players"][game_state["in_action"]]["stack"]



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

        if flush_suit:
            if card1["suit"] == flush_suit and card2["suit"] == flush_suit:
                return game_state["players"][game_state["in_action"]]["stack"]
            else:
                return 0
        elif len(two_pairs) > 1:
            return game_state["players"][game_state["in_action"]]["stack"]
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
