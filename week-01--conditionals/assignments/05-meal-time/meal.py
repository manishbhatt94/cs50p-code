def main():
  time_str = input("What time is it? ").strip().lower()
  time_hrs = convert(time_str)
  if 7 <= time_hrs <= 8:
    print("breakfast time")
  elif 12 <= time_hrs <= 13:
    print("lunch time")
  elif 18 <= time_hrs <= 19:
    print("dinner time")


def convert(time: str) -> float:
  hours, mins = normalise_to_24hr(time)
  return hours + mins / 60


def get_time_format(time):
  """
  Returns ["24hr", time] if 24 hour format
  Else returns either:
    ["am", time] or ["pm", time]
  """
  # splitting by space to check for 12 hrs suffix
  tokens = time.split(" ")
  assert 1 <= len(tokens) <= 2

  time = tokens[0]
  time_format = "24hr"

  if len(tokens) == 1:
    return [time_format, time]
  
  match tokens[1]:
    case "am" | "a.m.":
      time_format = "am"
    case "pm" | "p.m.":
      time_format = "pm"
    case _:
      raise ValueError("Bad input")
  
  return [time_format, time]

  
def normalise_to_24hr(time):
  time_format, time_str = get_time_format(time)
  time_parts = time_str.split(":")
  input_hours = int(time_parts[0])
  input_mins = int(time_parts[1])

  if time_format == "24hr":
    return input_hours, input_mins
  
  assert time_format == "am" or time_format == "pm"

  hours_normalised = input_hours % 12

  if time_format == "pm":
    hours_normalised += 12

  return hours_normalised, input_mins


if __name__ == "__main__":
  main()
