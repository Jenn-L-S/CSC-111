# Jennifer Smith
# Code written 09-27-2019.

# Here I assign the lists for rank and suit characters, as following:
rank = ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'J', 'Q', 'K', 'A']
suit = ['s', 'h', 'd', 'c']

# I also assign these characters to a prettier dictionary.
pretty_suit = {"s": "Spades", "h": "Hearts", "d": "Diamonds", "c": "Clubs"}
pretty_rank = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8",
               "9": "9", "t": "10", "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"}

# Here we define the ppcard(card) function to make our chosen card pretty.
def ppcard(card):
    print(pretty_rank[card[0]], "of", pretty_suit[card[1]])

def main():
    # Initialize deck and card.
    deck = []
    card = []

    # Call a for loop to create a deck with 52 playing cards.
    for x in rank:
        for y in suit:
            combo = x + y
            deck = deck + [combo]

    for z in deck:
        card = input('What is your card? ')
        if card == '00':
            print("Finished!")
            break
        elif card not in deck:
            print("That is not a card. Please note J/Q/K/A must be uppercase.")
        else:
            print("Your card is:", card)
            ppcard(card)

main()
