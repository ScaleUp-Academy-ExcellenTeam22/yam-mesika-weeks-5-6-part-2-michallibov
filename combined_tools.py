
def interleave(*iterables):
    """
    This function creates a list from all the iterable objects we received that
    chains all the objects by their indexes. This function first chains all the
    first indexes of all the iterables, then the it chains by the second and so on.
    :param iterables: iterable objects that we will chain to one list
    :return: a chained by indexes list of the iterables we got
    """
    return [item for sub_iterable in zip(*iterables) for item in sub_iterable]


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
