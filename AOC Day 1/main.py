num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

file = open('AOC Day 1/input_data', 'r')

sum_of_calibration_values = 0

for value in file:
    value = value.rstrip()

    converted_values = ""

    lowest_word_index = None
    highest_word_index = None

    lowest_word_value = ""
    highest_word_value = ""

    lowest_int_index = None
    highest_int_index = None

    for word in num_dict:
        x = value.find(word)
        y = value.rfind(word)

        if x >= 0:
            if lowest_word_index is None:
                lowest_word_index = x
                lowest_word_value = num_dict[word]

            if x < lowest_word_index:
                lowest_word_index = x
                lowest_word_value = num_dict[word]

        if y >= 0:
            if highest_word_index is None:
                highest_word_index = y
                highest_word_value = num_dict[word]

            if y > highest_word_index:
                highest_word_index = y
                highest_word_value = num_dict[word]

    for i, c in enumerate(value):
        if c.isdigit():
            if lowest_int_index is None:
                lowest_int_index = i
            else:
                highest_int_index = i

    if highest_int_index is None:
        highest_int_index = lowest_int_index

    if lowest_word_index is not None:

        if lowest_int_index < lowest_word_index:
            converted_values += str(value[lowest_int_index])

        else:
            converted_values += lowest_word_value

        if highest_int_index > highest_word_index:
            converted_values += str(value[highest_int_index])

        else:
            converted_values += highest_word_value
    else:
        converted_values += str(value[lowest_int_index])
        converted_values += str(value[highest_int_index])

    sum_of_calibration_values += int(converted_values)

    print(value, converted_values)

print(sum_of_calibration_values)
