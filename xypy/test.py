# Global Imports
import Libs.jsonParse as parse
import os

# Global Variables
TX = -59


def scale():
    rssi_list = range(-100,1)
    rssi_list = rssi_list[::-1]
    for x in rssi_list:
        dist = calc_dist(x)
        # dist1 = calc_dist(x, -70)
        printer(x, range_band(dist), dist)


def range_band(dist):
    if dist < -1.0:
        return "None"
    elif dist < 0.0173:
        return "Touch"
    elif dist < 1.0108:
        return "V. Near"
    elif dist < 3.0639:
        return "Near"
    elif dist < 8.3779:
        return "Medium"
    elif dist < 20.6086:
        return "Far"
    else:
        return "ERROR"


# def calc_dist(rssi, tx = TX):
#     ratio = (rssi * 1.0) / tx
#     if ratio < 1.0:
#         return ratio ** 10
#     else:
#         return (0.89976 * (ratio ** 7.7095)) + 0.111


def calc_dist(rssi, c1 = 0.89976, c2 = 7.7095, c3 = 0.111, tx = TX):
    ratio = float(rssi) / tx
    if ratio < 1.0:
        return calc_std_dist(rssi, tx)
    else:
        return (c1 * (ratio ** c2)) + c3


def calc_std_dist(rssi, tx):
    ratio = (rssi * 1.0) / tx
    return ratio ** 10


def get_rand():
    from random import randint
    _rand_num = randint(tx - 20, tx + 20)
    return _rand_num


def looper_auto():
    i = 1
    test = []
    while i <= 100:
        rssi, test = smooth_test(test)
        printer(i, rssi)
        i += 1


def printer(num, *args):
    if num is 0:
        print('{:^32}'.format("RSSI Value Test"))
        print('{:^32}'.format('TX value is %s' % (TX)))
        print('{:=^32}'.format('='))
    else:
        print('{:>4}'.format(str(num)) + ' | ', end='')
        for arg in range(len(args)):
            print('{:^10.10}'.format(str(args[arg])) + ' | ', end='')
        print("\n")


def save_to():
    file_name = parse.name(data) + ".txt"
    file_path = os.path.join(path(), file_name)
    with open(file_path, "w") as output:
        output.write('{:^32}'.format("RSSI Value Test"))
        output.write('{:^32}'.format('TX value is %s' % (tx)))
        output.write('{:=^32}'.format('='))

        rssi_list = range(-100,1)
        rssi_list = rssi_list[::-1]
        for x in rssi_list:
            dist = calc_dist(x)
            output.write('{:>4}'.format(str(num)) + ' | ', end='')


def smooth_test(rssi_list = None):
    if rssi_list is None:
        rssi_list = []

    # Create list of RSSI values
    while len(rssi_list) < 20:
        # Get new number
        rand_num = get_rand()
        # Append new nmber
        rssi_list.append(rand_num)

    # Sort List
    sorted_rssi_list = sorted(rssi_list)

    # Average the middle 12 values
    _temp_rssi_list = sorted_rssi_list[4:16]
    smooth_rssi = 0
    for i in _temp_rssi_list:
        smooth_rssi += i
    smooth_rssi = smooth_rssi / 12

    # Run Distance Calc on average
    beacon_dist = calc_dist(smooth_rssi)

    # Remove last rssi value and add a new one
    rssi_list.pop(-1)

    return beacon_dist, rssi_list


if __name__ == '__main__':
    # looper_auto()
    scale()
