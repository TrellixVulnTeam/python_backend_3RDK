def fizzbuzz(num):
    for item in range(1, num + 1):
        if not item % 3 and not item % 5:
            print("FizzBuzz")
        elif not item % 3:
            print("Fizz")
        elif not item % 5:
            print("Buzz")
        else:
            print(item)

fizzbuzz(50)
