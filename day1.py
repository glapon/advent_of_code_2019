input_file = open("input1.txt", "r")
input = input_file.readlines()
fuel = [int(mass) / 3 - 2 for mass in input]
print sum(fuel)
