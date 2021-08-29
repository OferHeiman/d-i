import random



# suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# value_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


class Card:
    def __init__(self,suit,value):
        # self.suit = random.choice(suit_list)
        # self.value = random.choice(value_list)
        self.suit = suit
        self.value = value


class Deck(Card):
    def __init__(self,cards_list:list):
        self.cards_list = cards_list
    

    def shuffle(self):
        if len(self.cards_list) == 52:
             random.shuffle(self.cards_list)
        else:
            print("Deck doesn't have all 52 cards")


    def deal(self):
        random_card = random.choices(self.cards_list)
        print(f'Your card is {random_card.value} of {random_card.suit}')
        self.cards_list.remove(random_card)