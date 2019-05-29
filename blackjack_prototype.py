import random
class cards_deck():
    cards = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    cards_value = {'Ace':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'Jack':10,'Queen':10,'King':10}
    Deck = {'Diamonds','Clubs','Spades','Heart'}
    def Show_deck(self):
        print(self.cards)
    def generate_card(self):
        out1 = []
        for i in range(0,2):
            out1.append(random.choice(self.cards))
        return out1
class player_game(self,chips,bet,cards*):

def player_input():
    total = 0
    input_1 = cards_deck()
    player_card = input_1.generate_card()
    print(player_card)
    for x in player_card:
        total = total + input_1.cards_value[x]
    print('the cards are {} and total card value is {}'.format(player_card,total))
player_input()