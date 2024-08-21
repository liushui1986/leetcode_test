import math


def passcode_generator(n):
    import string
    import random

    all_chars = string.ascii_letters + string.digits + '!@#$%^?()\\/<>'
    passcode_list = random.choices(all_chars, k=n)
    return ''.join(passcode_list)


def message_simple_encryption(message):
    import string
    a = string.ascii_lowercase
    b = a[::-1]
    c = b[18:] + b[10:18] + b[6:10] + b[:6]
    d = c[::-1]
    e = d[24:] + d[19:24] + d[12:19] + d[7:12] + d[:7]
    table = str.maketrans(a, e)
    return message.translate(table)


def gcd(x, y):
    """
    find the greatest common divisor
    :type x: int
    :type y: int
    :rtype: int
    """
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x, y):
    """
    find the least common multiple
    :type x: int
    :type y: int
    :rtype: int
    """
    return x * y // gcd(x, y)


def range_num(data):
    """
    :type data: List/Tuple/Dict
    :retype: float/int
    """
    return max(data) - min(data)


def average(data):
    """
    :type data: List/Tuple/Dict
    :retype: float/int
    """
    return sum(data) / len(data)


def variance(data):
    """
    :type data: List/Tuple/Dict
    :retype: float/int
    """
    num_aver = average(data)
    temp = [(num - num_aver) ** 2 for num in data]
    return sum(temp) / (len(temp) - 1)


def standard_deviation(data):
    """
    :type data: List/Tuple/Dict
    :retype: float/int
    """
    return math.sqrt(variance(data))


def median(data):
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return average(temp[size // 2 - 1: size // 2 + 1])


def random_leetcodetest(n1, n2):
    """
    :type n1: int (the number of tests from what we have learned in interview python basics)
    :type n2: int (the number of tests from what we haven't learned in interview python basics)
    :rtype: List[int] (it will return the leetcodetest number)
    """
    import random
    leetcodetest_easy = [1, 20, 26, 27, 35, 69, 70, 125, 136, 155, 167, 169, 217, 219, 225, 232, 242, 268, 278, 283,
                         287, 344, 345, 349, 350, 367, 374, 389, 438, 441, 442, 448, 496, 575, 641, 682, 704, 744, 844,
                         852, 905, 922, 933, 977, 1004, 1047, 1381, 1441]
    leetcodetest_hard = [53, 62, 67, 70, 94, 100, 101, 102, 104, 108, 111, 112, 121, 122, 144, 145, 198, 199, 213, 226,
                         257, 309, 394, 513, 515, 559, 583, 589, 617, 669, 700, 714, 746, 938, 965, 1137, 1143, 1480]
    selected_test = random.sample(leetcodetest_easy, n1)
    selected_test.sort()
    selected_test += random.sample(leetcodetest_hard, n2)
    return sorted(selected_test)
