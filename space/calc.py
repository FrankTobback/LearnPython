# MODULE
# function to calculate the mass of the planets
def planet_mass(gravity, radius):
    mass = (gravity*radius**2) / (6.67*10**-11)
    return mass

# function to calculate volume of the planet
def planet_vol(radius):
    vol = (4*3.142*radius**2) / 3
    return vol
