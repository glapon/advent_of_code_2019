input_file = open("input2.txt", "r")
input_strings = input_file.readlines()[0].split(",")

for x in range(100):
    for y in range(100):
        input = [int(value) for value in input_strings]
        input[1] = x
        input[2] = y
        index = 0
        while index < len(input):
            if input[index] == 99:
                break
            elif input[index] == 1:
                input[input[index + 3]] = input[input[index + 1]] + input[input[index + 2]]
            elif input[index] == 2:
                input[input[index + 3]] = input[input[index + 1]] * input[input[index + 2]]
            index += 4
        if input[0] == 19690720:
            print 100 * x + y
            break
