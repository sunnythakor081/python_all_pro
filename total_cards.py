total_cards = 52


kings = 4


spades = 13


king_of_spades = 1


kings_or_spades = kings + spades - king_of_spades


neither_kings_nor_spades = total_cards - kings_or_spades


probability = neither_kings_nor_spades / total_cards

print("The probability of drawing a card that is neither a king nor a spade is %.2f",probability)

