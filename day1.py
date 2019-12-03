input_file = open("input1.txt", "r")
input = input_file.readlines()
masses = [int(m) / 3 - 2 for m in input]
print sum(masses)
