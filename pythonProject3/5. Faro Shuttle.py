cards = input().split()
half = int(len(cards) // 2)
number_of_faro_shuffles = int(input())
current_deck = []

left_side = (cards[0:half])
right_side = (cards[half::])
for index in range(len(left_side)):
    current_deck.append(left_side[index])
    current_deck.append(right_side[index])

    cards = current_deck

print(cards)
