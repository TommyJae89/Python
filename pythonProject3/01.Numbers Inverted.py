numbers = input().split()

numbers_inverted = []

for number in numbers:
    num = int(number) * -1
    numbers_inverted.append(num)

print(numbers_inverted)