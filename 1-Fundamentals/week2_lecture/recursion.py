# Recursion
# def countdown(n):
#     for i in range(n, 0, -1):
#         print(i)

# def r_countdown(n):
#     print(n)
#     if n > 0:
#         r_countdown(n-1)

# # countdown(5)
# r_countdown(5)


def rFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return rFib(n-1) + rFib(n-2)

rFib(4)