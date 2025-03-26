def energy_equivalent_to_mass(mass: int):
  LIGHT_SPEED = int(3e8)
  energy = mass * pow(LIGHT_SPEED, 2)
  return energy


def main():
  mass = int(input("m: "))
  energy = energy_equivalent_to_mass(mass)
  print(f"E: {energy}")


main()
