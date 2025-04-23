def main():
    guests_list = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for guest in guests_list:
        print(write_letter(guest, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {receiver},
    
       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
    """


main()
