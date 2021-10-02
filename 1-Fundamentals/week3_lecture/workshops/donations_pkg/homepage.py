donation_sum = 0

def show_homepage():
    print("       === DonateMe Homepage ===           ")
    print("------------------------------------------ ")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------ ")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------ ")
    print("|              5.   Exit                  |")
    print("------------------------------------------ ")

def donate(username):
    global donation_sum
    while True:
        donation_amt = input("Enter amount to donate: ")
        try:
            donation_amt = float(donation_amt)
        except ValueError:
            print("Please enter numerical digits.")
            continue
        if donation_amt < 0 or donation_amt == 0:
            print("Please enter a non-negative and non-zero amount.")
        else:
            break
    donation = f"{username} donated ${donation_amt:.2f}"
    donation_sum += donation_amt
    print(f"Thank you for your donation")
    return donation, donation_sum

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    for donation in donations:
        print(donation)
    print(f"Total = ${donation_sum}")