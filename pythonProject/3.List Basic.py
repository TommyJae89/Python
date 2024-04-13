n = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive_numbers.append(numbers)
    else:
        negative_numbers.append(numbers)

print(positive_numbers)
print(negative_numbers)

count_positives = len(positive_numbers)
sum_negatives = sum(negative_numbers)

print(f"count of positives: {count_positives}. Sum of negatives: {sum_negatives}.")