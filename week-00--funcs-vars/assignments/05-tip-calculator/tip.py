def main():
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percentage would you like to tip? "))
  tip = dollars * percent
  print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
  dollar_str_sans_symbol = d[1:]
  return float(dollar_str_sans_symbol)


def percent_to_float(p: str) -> float:
  percent_str_sans_symbol = p[:-1]
  return float(percent_str_sans_symbol) / 100


main()
