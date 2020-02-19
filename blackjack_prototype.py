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

    def generate_card_single(self):
        card_single = []
        for i in range(0, 1):
            card_single.append(random.choice(self.cards))
        return card_single


def player_input():
    total = 0
    input_1 = cards_deck()
    player_card = []
    player_card.append(input_1.generate_card())
    print(player_card)
    for x in player_card:
        for y in x:
            total = total + input_1.cards_value[y]
    print('the cards are {} and total card value is {}'.format(player_card,total))
    print('edited')

def play_game():
    input_1 = cards_deck()
    i=2
    total = 0
    new_total = 0
    player_card = []
    player_card.append(input_1.generate_card())
    for x in player_card:
        for y in x:
            total = total + input_1.cards_value[y]
    print('the cards are {} and total card value is {}'.format(player_card, total))
    bet = input('Please place your bet:\n')
    bet = int(bet)
    while i > 1:
        choice = input('do you want to continue ?\n')
        if choice == 'hit':
            input_1 = cards_deck()
            player_card.append(input_1.generate_card_single())
            for o in player_card:
                for z in o:
                    new_total = new_total +  input_1.cards_value[z]
            print('the cards are {} and total card value is {}'.format(player_card, new_total))
            total = new_total
        elif choice == 'stand':
            print('the cards are {} and total card value is {}'.format(player_card, total))
        else:
            print('thanks for playing')
            break
play_game()