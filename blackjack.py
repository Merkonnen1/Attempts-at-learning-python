import random

class Deck:
    def __init__(self):
        self.List = []
        self.dealerList = []
        self.cards = {
            'Spades': ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', "Ace"],
            'Hearts': ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', "Ace"],
            'Flower': ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', "Ace"],
            'Diamond': ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', "Ace"]
        }
        self.value = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                      'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': [1, 11]}
        self.total = 0
        self.dealer = 0

    def deal(self):
        x = random.choice(self.List)
        random1 = random.randint(0, len(self.cards[x]) - 1)
        y = self.cards[x][random1]
        print(x + ' ' + y)
        if y == 'Ace':
            self.total += int(input('You got an ace. Do you want a 1 or 11?: '))
            print('Total:', self.total)
        else:
            self.total += self.value[y]
            print('Total:', self.total)

    def dealer_play(self):
        x = random.choice(self.List)
        random1 = random.randint(0, len(self.cards[x]) - 1)
        y = self.cards[x][random1]
        print(x + ' ' + y)
        if y == 'Ace':
            self.dealer += 11 if self.dealer + 11 <= 21 else 1
            print('Dealer Total:', self.dealer)
        else:
            self.dealer += self.value[y]
            print('Dealer Total:', self.dealer)

    def blackjack(self, money):
        while self.total < 21:
            self.deal()
            if self.total >= 17 and self.total < 21:
                p = input('Stick or twist: ')
                if p.lower() == "stick":
                    break

        if self.total > 21:
            return 'BUST', 0

        while self.dealer < 17:
            self.dealer_play()

        if self.dealer > 21 or self.total > self.dealer:
            return 'WIN', money * 2
        elif self.total == self.dealer:
            return 'DRAW', money
        else:
            return 'LOSE', 0

    def initialize_deck(self):
        for keys in self.cards.keys():
            self.List.append(keys)

    def __str__(self):
        return ', '.join(self.List)

d = Deck()
d.initialize_deck()
str()
print('Deck:', d)
result, winnings = d.blackjack(500)
print('Result:', result)
print('Winnings:', winnings)
