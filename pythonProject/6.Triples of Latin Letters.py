number = int(input())

small_letter_ascii= ord("a")

for first_char in range(small_letter_ascii, small_letter_ascii + number):
    for second_char in range(small_letter_ascii, small_letter_ascii + number):
        for third_char in range(small_letter_ascii, small_letter_ascii + number):
            print(f"{chr(first_char)}, {chr(second_char)}, {chr(third_char)}")