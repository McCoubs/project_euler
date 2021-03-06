from functools import reduce


def get_factors(n):
    """
    Function returns all the factors of n very quickly as a set.

    REQ: n >=0 and whole

    :param n: {int} is number to return all factors of
    :return: {set} of factors of n
    """

    # check for 0, return None
    if n == 0:
        return None
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
