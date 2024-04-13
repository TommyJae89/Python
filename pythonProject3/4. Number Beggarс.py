list_of_numbers_as_string = input().split(", ")
beggars = int(input())

sum_of_each_beggars = []
start_index = 0

for beggar in range(beggars):
    current_sum = 0
    for total in range(start_index, len(list_of_numbers_as_string), beggars):
        current_sum += int(list_of_numbers_as_string[total])
    sum_of_each_beggars.append(current_sum)
    start_index += 1

print(sum_of_each_beggars)
