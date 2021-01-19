#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    greatest_number = number_list[0]
    for num in number_list[1:]:
        if greatest_number < num:
            greatest_number = num

    return greatest_number


def get_smallest(number_list):
    smallest_number = number_list[0]
    for num in number_list[1:]:
        if smallest_number > num:
            smallest_number = num

    return smallest_number


def get_mean(number_list):
    s = sum(number_list)
    mean = s / len(number_list)

    return mean


def get_median(number_list):
    n = len(number_list)
    mid = int(n / 2)
    number_list.sort()
    if n % 2 == 0:
        median = (number_list[mid - 1] + number_list[mid]) / 2
    else:
        median = number_list[mid]

    return median
