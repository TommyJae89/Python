list_of_gifts = input().split()

command = input()
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command == "OutOfStock":
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] ==current_gift:
                list_of_gifts[index] = "Noone"
    elif current_command == "Required":
        index = int(current_command[2])
        if index <= index <= len(list_of_gifts):
            list_of_gifts = current_gift
    elif current_command == "JustInCase":
        list_of_gifts.pop()
        list_of_gifts.append(current_gift)

    command = input()