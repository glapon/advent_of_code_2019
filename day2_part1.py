input_file = open("input2.txt", "r")
input_strings = input_file.readlines()[0].split(",")
input = [int(value) for value in input_strings]

input[1] = 12
input[2] = 2

index = 0
while index < len(input):
    if input[index] == 99:
        break
    elif input[index] == 1:
        input[input[index + 3]] = input[input[index + 1]] + input[input[index + 2]]
    elif input[index] == 2:
        input[input[index + 3]] = input[input[index + 1]] * input[input[index + 2]]
    index += 4

print input[0]
