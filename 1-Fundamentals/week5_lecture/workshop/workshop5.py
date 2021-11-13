import random

class Guessing_Game():
    tries: int
    low: int
    high: int

    def __init__(self, tries, low, high):
        self.tries = tries
        self.low = low
        self.high = high
        self.answer = self.get_number()

    def get_number(self):
        if random.randint(self.low, self.high) % 0:
            return random.randint(self.low, self.high)
        else:
            print()
        return -1

    def guess(self):
        tries_temp = self.tries
        print("Target",self.answer)
        while tries_temp > 0:
            print(f"{tries_temp} tries remaining")
            user_guess = int(input("Guess a number: "))
            if user_guess == self.answer:
                print("You guessed correctly!")
                return
            elif user_guess < self.answer:
                print("Guess higher!")
            else:
                print("Guess lower!")
            tries_temp -= 1


    def linear_guess(self):
        tries_temp = self.tries
        for i in range(self.low, self.high + 1):
            if tries_temp == 0:
                print("The program has failed to guess the correct number.")
                return
            print(f"{tries_temp} tries remaining")
            print(f"The program is guess... {i}")
            print("This is answer: ", self.answer)
            if i == self.answer:
                print("You guessed correctly!")
                return
            tries_temp -= 1

    # this_list = [1,2,3,4,5,6,7,8,9,10]

    def binary_search_guess(self):
        tries_temp = self.tries
        this_list = list(range(self.low, self.high + 1))
        print(this_list)
        print(self.answer)
        left_index = 0
        right_index = len(this_list) - 1
        while left_index <= right_index and tries_temp > 0:
            middle_index = (left_index + right_index ) // 2
            potentialMatch = this_list[middle_index]
            print("This is middle_index ", middle_index)
            print("Number of tries ", tries_temp)
            print("This is potential match ", potentialMatch)
            if potentialMatch == self.answer:
                print(f"Found it! {potentialMatch}")
                return middle_index
            elif potentialMatch > self.answer:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
            tries_temp -= 1
        return -1

    # def binary_search_guess(self):

        # return -1

        # for i in range(self.low, self.high + 1):
        #     if tries_temp == 0:
        #         print("The program has failed to guess the correct number.")
        #         return
        #     print(f"{tries_temp} tries remaining")
        #     print(f"The program is guess... {i}")
        #     print("This is answer: ", self.answer)
        #     if i == self.answer:
        #         print("You guessed correctly!")
        #         return
        #     tries_temp -= 1

gameone = Guessing_Game(5, 1, 10)
gameone.binary_search_guess()
# gameone.guess()
# gameone.linear_guess()
# gametwo = Guessing_Game(5, 2, 20)
# gametwo.guess()
# gametwo.linear_guess()