from random import shuffle

class Deck:
      def __init__(self, cards):
            self.cards = cards

      def draw(self):
            return self.cards.pop()

      def add(self, card):
            self.cards.append(card)
            shuffle(self.cards)

      def count(self):
            return len(self.cards)
deck_info = [ ("Eelena", 3),("Kimerald",3),("Hareen",3),("sin-bah",2),("Barius",2),("Anzu",3),("Camisah",2),("Delphonse",4),("sacrifice",4),("lac",3),("cadeau",3),("portail",1),("resurection",1),("chute",8),("port",4),("ggris",6),("gcristal",4)]

def create_deck(deck_info):
      deck = []
      for cardInfo in deck_info:
            for i in range(0,cardInfo[1]):
                  deck.append(cardInfo[0])
      shuffle(deck)
      return deck

deck = Deck(create_deck(deck_info))

hand = []

run = True
gold = 1000
is_starting = True

print("C'est vous qui commencer ? O=Oui, N=Non")
resp = input()
if resp.lower() == "o":
      is_starting = True
else:
      is_starting = False
your_turn = is_starting

for i in range(0,7):
      hand.append(deck.draw())
print(hand)
print("Avez vous un stade en main ? O=Oui, N=Non" )
can_start = input()
mis_count = 0
while can_start.lower() != "o":
      mis_count+=1
      for card in hand:
            deck.add(card)
      hand = [ ]
      for i in range(0, 7):
            hand.append(deck.draw())
      print(hand)
      print("Avez vous un stade en main ? O=Oui, N=Non")
      can_start=input()
print(f"Vous avez eu {mis_count} misères")

while run:
      if your_turn:
            goldWin = ""
            cost = ""
            while not goldWin.isdigit():
                  print("Votre tour commence, combien d'argent gagner-vous ?")
                  goldWin = input()
            while not cost.isdigit():
                  print("Combien dépenser vous ?")
                  cost = input()

            gold = gold + int(goldWin) - int(cost)
            while(your_turn):
                  print(f"A vous de jouer, vous avez {gold} d'argent et {deck.count()} cartes dans votre deck.")
                  print(hand)
                  resp = input()
                  if resp[0] == "p":
                        card = deck.draw()
                        hand.append(card)
                  elif resp[0] == "j":
                        name = resp[2:].lower()
                        cardToPlay = 0
                        find = False
                        for card in hand:
                              if card.lower()==name:
                                    hand.remove(card)
                                    find=True
                                    break
                              cardToPlay+=1
                        if not find:
                              print("carte non trouver.")
                  elif resp[0] == "a":
                        name = resp[2:].lower()
                        deck.add(name)
                  elif resp[0] == "d":
                        deck.draw()
                  elif resp[0] == "e":
                        your_turn = False
                  elif resp[ 0 ] == "r":
                        for card in hand:
                              deck.add(card)
                        hand = [ ]
                  elif resp[ 0 ] == "c":
                        hand = [ ]

                  elif resp.startswith("s "):
                        print("pass")
                        find = False
                        for card in deck.cards:
                              if card.lower() == resp[2:].lower():
                                    deck.cards.remove(card)
                                    hand.append(card)
                                    find = True
                                    break
                        if not find:
                              print("Carte non trouvé")
                  elif resp == "see":
                        print(deck.cards)
                        shuffle(deck.cards)
                  elif resp.startswith("paid"):
                        gold -= int(resp[5:])
                  elif resp.startswith("win"):
                        gold += int(resp[4:])
      else:
            print("Attendez que votre adversaire ait fini de jouer")
            resp = input()
            if resp == "o":
                  your_turn = True
            elif resp.startswith("paid"):
                  gold -= int(resp[ 5: ])
            elif resp.startswith("win"):
                  gold += int(resp[ 4: ])
