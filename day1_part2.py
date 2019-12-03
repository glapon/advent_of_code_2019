input_file = open("input1.txt", "r")
input = input_file.readlines()

def fuel_formala(mass):
    return int(mass) / 3 - 2

def calc_fuel(mass):
    fuel = 0
    while (fuel_formala(mass)> 0):
        fuel += fuel_formala(mass)
        mass = fuel_formala(mass)
    return fuel

fuel = [calc_fuel(mass) for mass in input]
print sum(fuel)
