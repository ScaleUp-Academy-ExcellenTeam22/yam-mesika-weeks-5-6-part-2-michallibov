
def find_perfect_serving():
    """
    This is a generator that runs in an endless loop and returns using yield if the sum of all it's
    divisions equals to the number itself.
    :return: using yield returns a number which the sum of all of it's divisors equals to the number
    itself.
    """
    # The number we want to check if it's divisor's sum equals to it.
    number_of_serving = 1
    while True:
        sum_of_divisors = sum(serving_divisor for serving_divisor in range(1, number_of_serving-1) if number_of_serving % serving_divisor == 0)
        # The result variable is just to prevent a warning that the statement has no effect.
        result = [(yield number_of_serving) if sum_of_divisors == number_of_serving else 0]
        number_of_serving += 1


if __name__ == '__main__':
    perfect_serving = find_perfect_serving()
    for item in perfect_serving:
        print(item)
