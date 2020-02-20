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
        return new_total



def play_game():
   try:
       player_game = cards_deck()
       dealer_game = cards_deck()
       i = 2
       j = 2
       while j > 1:
           player_card = []
           dealer_card = []
           dealer_card.append(dealer_game.generate_card())
           dealer_game.card_value(dealer_card)
           player_card.append(player_game.generate_card())
           player_game.card_value(player_card)
           bet = int(input('Please place your bet:\n'))
           while i > 1:
               print("The Player's cards are :{} \nThe Dealers cards are:{} ".format(player_card, dealer_card))
               choice = input('what do you want to do ? \nh for Hit and s for stand \npress any other key to quit\n')
               if choice == 'h':
                   player_card.append(player_game.generate_card_single())
                   player_game.card_value(player_card)
                   dealer_game.card_value(dealer_card)
                   print("The Player's cards are :{} \nThe Dealers cards are:{} ".format(player_card, dealer_card))
               elif choice == 's':
                   player_game.card_value(player_card)
                   print("The Player's cards are :{} \nThe Dealers cards are:{} ".format(player_card, dealer_card))
               else:
                   print('please press a valid input')
                   continue
               dealer_card_value = dealer_game.card_value(dealer_card)
               if dealer_card_value < 21:
                   dealer_card.append(dealer_game.generate_card_single())
               print("The Player's cards are :{} \nThe Dealers cards are:{} ".format(player_card, dealer_card))
               player_card_value = player_game.card_value(player_card)
               dealer_card_value = dealer_game.card_value(dealer_card)
               if player_card_value == 21:
                   money_won_bet = bet * (150 / 100)
                   print('Blackjack! you have won %d' % money_won_bet)
                   break
               elif dealer_card_value == 21:
                   print('Dealer wins you lose all bet ')
                   break
               elif player_card_value > 21:
                   print('bust!')
                   break
               elif dealer_card_value > 21:
                   money_dealer_bust = bet * (150 / 100)
                   print("you won the game because dealer went bust and your money is %d " % money_dealer_bust)
                   break
               if player_card_value > dealer_card_value:
                   money_won = bet * (150 / 100)
                   print('you have won the game and your money is %d' % money_won)
                   break
               elif player_card_value == dealer_card_value == 21:
                   print('this game is a tie')
                   break
               else:
                   money_won = bet * (150 / 100)
                   print('you have won the game and your money is %d' % money_won)
                   break
           choice = input('Would you like to Play again [y/n]?:\n')
           if choice == 'n' or  'N':
               print('thanks for playing')
               break
           else:
               continue
   except ValueError as msg:
       print('please enter a number and try again')
   except Exception as msg1:
       print(msg1)

play_game()
