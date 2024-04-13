team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

card_input = input().split()
statement = False
for cards in card_input:
    cards_info = cards.split("-")
    if cards_info[0] == "A":
        number = cards_info[1]
        if int(number) not in team_a:
            continue
        team_a.remove(int(number))
        if len(team_a) < 7:
            statement = True
            break
    elif cards_info[0] == "B":
        number = cards_info[1]
        if int(number) not in team_b:
            continue
        team_b.remove(int(number))
        if len(team_b) < 7:
            statement = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if statement:
    print("Game was terminated")
