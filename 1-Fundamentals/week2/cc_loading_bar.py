for amount_loaded in range(0, 105, 5):
    print(amount_loaded)
    if not amount_loaded == 0 and amount_loaded % 25 == 0:
        print(f"{str((amount_loaded/100).as_integer_ratio()[0])}/{str((amount_loaded/100).as_integer_ratio()[1])} of the way there")
print("Loading Complete")