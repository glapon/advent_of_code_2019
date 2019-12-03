input_file = open("input1.txt", "r")
input = input_file.readlines()

def calc_fuel(mass):
    fuel = 0
    while (int(mass) / 3 - 2 > 0):
        fuel += int(mass) / 3 - 2
        mass = int(mass) / 3 - 2
    return fuel

fuel = [calc_fuel(mass) for mass in input]
print sum(fuel)
