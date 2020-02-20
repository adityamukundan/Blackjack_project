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
       player_game = cards_deck()
       dealer_game = cards_deck()
       round = 0
       i = 2
       player_card = []
       dealer_card = []
       dealer_card.append(dealer_game.generate_card())
       dealer_game.card_value(dealer_card)
       player_card.append(player_game.generate_card())
       player_game.card_value(player_card)
       bet = int(input('Please place your bet:\n'))
       while i > 1:
           choice = input('what do you want to do ? \nh for Hit and s for stand \npress any other key to quit\n')
           if choice == 'h':
               player_card.append(player_game.generate_card_single())
               player_game.card_value(player_card)
               dealer_game.card_value(dealer_card)
           elif choice == 's':
               player_game.card_value(player_card)
           else:
               print('thanks for playing')
               break
           player_card_value = player_game.card_value(player_card)
           dealer_card_value = dealer_game.card_value(dealer_card)
           if round == 1:
               if player_card_value > dealer_card_value:
                   print('you have won the game')
                   break
               elif player_card_value == dealer_card_value == 21:
                   print('this game is a tie')
                   break
               else:
                    print("the dealer wins ,you lose ")
                    break
           if player_card_value == 21:
               print('you have won the game!')
               break
           if player_card_value > 21:
               print('bust!')
               break
           if dealer_card_value < 21:
               dealer_card.append(dealer_game.generate_card_single())
           round += 1
   except ValueError as msg:
       print('please enter a number and try again')
   except Exception as msg1:
       print(msg1)

play_game()

#class with dealer and game logic to be added with functions .Separate objects to be created for the player and for the dealer at which point the winner is to be decided and the bet money will be calculated with 3:2 ratio