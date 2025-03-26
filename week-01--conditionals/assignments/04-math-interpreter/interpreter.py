def main():
  expression = input("Expression: ").strip()
  result = evaluate(expression)
  if result is not None:
    print(f"{result:.1f}")
  else:
    print("Bad input")


def evaluate(expression: str) -> float:
  x, y, z = expression.split(" ")
  first_operand = float(x)
  second_operand = float(z)
  operator = y

  match operator:
    case "+":
      return first_operand + second_operand
    case "-":
      return first_operand - second_operand
    case "*":
      return first_operand * second_operand
    case "/":
      return first_operand / second_operand
    case _:
      return None


main()
