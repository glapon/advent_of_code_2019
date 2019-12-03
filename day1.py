input_file = open("input1.txt", "r")
input = input_file.readlines()

def fuel_formala(mass):
    return int(mass) / 3 - 2

fuel = [fuel_formala(mass) for mass in input]
print sum(fuel)
