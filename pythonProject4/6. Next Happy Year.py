number = int(input())

while True:
    number = str(number)
    if len(set(number)) == len(number):
        print(number)
        break

    else:
        number = int(number)
        number += 1
