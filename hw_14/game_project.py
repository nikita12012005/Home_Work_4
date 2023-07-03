import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card)

    def get_hand_value(self):
        value = 0
        has_ace = False

        for card in self.hand:
            if card.rank == "Ace":
                value += 11
                has_ace = True
            elif card.rank in ["King", "Queen", "Jack"]:
                value += 10
            else:
                value += int(card.rank)

        if has_ace and value > 21:
            value -= 10

        return value

class BlackjackGame:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.dealer = Player("Dealer")
        self.deck = Deck()

    def start(self):
        print("Welcome to Blackjack!")
        print("Dealing initial cards...")

        self.deck.shuffle()

        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

        self.player.show_hand()
        self.dealer.show_hand()

        while True:
            choice = input("Do you want to hit or stand? (h/s) ")
            if choice.lower() == "h":
                self.player.add_card(self.deck.deal_card())
                self.player.show_hand()

                if self.player.get_hand_value() > 21:
                    print("Busted! You lose.")
                    break
            elif choice.lower() == "s":
                while self.dealer.get_hand_value() < 17:
                    self.dealer.add_card(self.deck.deal_card())

                self.dealer.show_hand()

                player_score = self.player.get_hand_value()
                dealer_score = self.dealer.get_hand_value()

                if dealer_score > 21:
                    print("Dealer busts! You win.")
                elif player_score > dealer_score:
                    print("You win!")
                elif player_score < dealer_score:
                    print("You lose.")
                else:
                    print("It's a tie.")

                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

        print("Thanks for playing!")

# Main program
player_name = input("Enter your name: ")
game = BlackjackGame(player_name)
game.start()

