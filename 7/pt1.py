import re
from enum import IntEnum

input = open("./7/input.txt", "r")

class Card:
    value: int
    card: str

    def __init__(self, card: str):
        self.card = card
        match (card):
            case "1": self.value = 1
            case "2": self.value = 2
            case "3": self.value = 3
            case "4": self.value = 4
            case "5": self.value = 5
            case "6": self.value = 6
            case "7": self.value = 7
            case "8": self.value = 8
            case "9": self.value = 9
            case "T": self.value = 10
            case "J": self.value = 11
            case "Q": self.value = 12
            case "K": self.value = 13
            case "A": self.value = 14
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, __value: object) -> bool:
        return self.value == __value.value
    
    def __repr__(self) -> str:
        return self.card

class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    @classmethod
    def get(cls, cards: list[Card]):
        print(cards)
        mapped_cards: dict[str: list[Card]] = dict()
        for card in cards:
            if card.card not in mapped_cards:
                mapped_cards[card.card] = []
            mapped_cards[card.card].append(card)
        print(mapped_cards)
        hand: list[int] = sorted([len(k) for k in mapped_cards.values()])
        match(len(hand)):
            case 1: return cls(7) # FIVE_OF_A_KIND
            case 2:
                match(hand[0]):
                    case 1: return cls(6) # FOUR_OF_A_KIND
                    case 2: return cls(5) # FULL_HOUSE
            case 3:
                match(hand[1]):
                    case 1: return cls(4) # THREE_OF_A_KIND
                    case 2: return cls(3) # TWO_PAIR
            case 4: return cls(2) # ONE_PAIR
            case 5: return cls(1) # HIGH_CARD

class Hand:
    cards: tuple[Card, Card, Card, Card, Card]
    hand_type: HandType
    bet: int

    def __init__(self, cards: str, bet: int) -> None:
        self.cards = (Card(cards[0]), Card(cards[1]), Card(cards[2]), Card(cards[3]), Card(cards[4]))
        self.bet = bet
        self.hand_type = HandType.get(list(self.cards))

    def __eq__(self, __value: object) -> bool:
        return self.cards == __value.cards

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            return self.cards < other.cards
        return self.hand_type < other.hand_type 
        
def parse(input) -> list[Hand]:
    hands: list[Hand] = []
    for line in input:
        cards, bet = line.split()
        hands.append(Hand(cards, int(bet)))
    return hands

hands = parse(input)

sorted_hands = sorted(hands)
val = 0
for i, hand in enumerate(sorted_hands):
    val += (i + 1) * hand.bet

print(val)