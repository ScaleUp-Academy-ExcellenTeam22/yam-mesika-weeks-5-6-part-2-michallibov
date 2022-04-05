
def find_perfect_serving():
    """
    This is a generator that runs in an endless loop and returns using yield if the sum of all it's
    divisions equals to the number itself.
    :return: using yield returns a number which the sum of all of it's divisions equals to the number
    itself.
    """
    # The number we want to check if it's division's sum equals to it.
    number_of_serving = 1
    while True:
        # The sum of all divisions
        sum_of_divisions = 0
        for serving_division in range(1, number_of_serving-1):
            # Check if this number is a division of number_of_serving and if so, add it to the sum_of_divisions
            sum_of_divisions += serving_division if number_of_serving % serving_division == 0 else 0
        if sum_of_divisions == number_of_serving:
            yield number_of_serving
        number_of_serving += 1


if __name__ == '__main__':
    perfect_serving = find_perfect_serving()
    for item in perfect_serving:
        print(item)
