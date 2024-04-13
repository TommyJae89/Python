numbers = input().split(" ")
counts = int(input())
final_numbers = []
for number in numbers:
    final_numbers.append(int(number))

for count in range(counts):
    final_numbers.remove(min(final_numbers))
print(final_numbers)
