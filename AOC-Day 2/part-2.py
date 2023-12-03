file = open('input_data', 'r')

power = 0

for line in file:
    line = line.rstrip()
    index = line.find(":")
    line = line[index + 1:]

    game_records = line.split(";")

    list_of_game_records = [inner.split(",") for inner in game_records]

    set_of_cubes = {'blue': 0, 'red': 0, 'green': 0}

    for record in list_of_game_records:
        for color in record:
            color_info = "".join(color).split(" ")
            color_name = color_info[-1]
            count = int(color_info[1])

            if set_of_cubes[color_name] < count:
                set_of_cubes[color_name] = count

    power += (set_of_cubes['red'] * set_of_cubes['blue'] * set_of_cubes['green'])

print(power)




