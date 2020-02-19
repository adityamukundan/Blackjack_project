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
    def generate_single_card(self):
        card = random.choice(self.cards)
        return card


def player_input(st = 'normal'):
    total = 0
    input_1 = cards_deck()
    player_card = input_1.generate_card()
    print(player_card)
    for x in player_card:
        total = total + input_1.cards_value[x]
    print('the cards are {} and total card value is {}'.format(player_card,total))
    return total


def dealer():
    total = 0
    input_1 = cards_deck()
    player_card = input_1.generate_card()
    print(player_card)
    for x in player_card:
        total = total + input_1.cards_value[x]
    print('the  dealer cards are {} and total card value is {}'.format(player_card,total))

def betting():
    pass



def play_game():
    i = 2
    total_player = []
    draw = cards_deck()
    while i > 1:
      decision = input('What do you want to do ? \n 1.Hit \n 2.Stand \n')
      if decision == 'yes':
          total_player.append(draw.generate_card())
          print(total_player)
          for x in total_player:
              value_card_player = value_card_player + draw.cards_value[x]
          print('the total score for the cards is {}'.format(value_card_player))
          dealer()
      else:
          break

play_game()