import random
class cards_deck():
    cards = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    Deck = {'Diamonds','Clubs','Spades','Heart'}
    def __init__(self):
        pass

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

    def card_value(self,card):
        new_total = 0
        cards_value = {'Ace': 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Jack': 10, 'Queen': 10,
                       'King': 10}
        for o in card:
            for z in o:
                new_total = new_total + cards_value[z]
        print('the cards are {} and total card value is {}'.format(card, new_total))
        return new_total

def play_game():
   try:
       input_1 = cards_deck()
       i = 2
       player_card = []
       player_card.append(input_1.generate_card())
       input_1.card_value(player_card)
       bet = int(input('Please place your bet:\n'))
       while i > 1:
           choice = input('do you want to continue ?\n')
           if choice == 'hit':
               input_1 = cards_deck()
               player_card.append(input_1.generate_card_single())
               input_1.card_value(player_card)
           elif choice == 'stand':
               input_1.card_value(player_card)
           else:
               print('thanks for playing')
               break
   except ValueError as msg:
       print('please enter a number and try again')

play_game()

#class with dealer and game logic to be added with functions .Separate objects to be created for the player and for the dealer at which point the winner is to be decided and the bet money will be calculated with 3:2 ratio