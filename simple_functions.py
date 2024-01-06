# Simple temperature converter 
def f_to_c(f_temp):
  c_temp = round((f_temp - 32) * 5/9, 1)
  return f_temp, c_temp

curr_fahrenheit, curr_celsius = f_to_c(100)

print("The current temperature of " + str(curr_fahrenheit) + " degrees Fahrenheit is " + str(curr_celsius) + " degrees Celsius.\n")

def c_to_f(c_temp):
  f_temp = round((c_temp * (9/5) + 32), 1)
  return f_temp, c_temp

new_fahrenheit, new_celsius = c_to_f(0)

print("The current temperature of " + str(new_celsius) + " degrees Celsius is " + str(new_fahrenheit) + " degrees Fahrenheit.\n")


# Functions for calculating force, energy, work
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " newtons of force.\n")

def get_energy(mass, c = 3*10**8):
  return mass * c

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " joules of energy.\n")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " joules of work over " + str(train_distance) + " meters.\n")