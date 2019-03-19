# Global Imports


# Global Variables
tx = -44


def calc_dist(rssi):
    ratio = (rssi * 1.0) / tx
    if ratio < 1.0:
        return ratio ** 10
    else:
        return (0.89976 * (ratio ** 7.7095)) * 0.111


def get_rand():
    from random import randint
    _rand_num = randint(tx - 20, tx + 20)
    return _rand_num


def looper_man():
    while True:
        smooth_test()
        cont = input('')
        if cont.lower() in ["end", "stop", "exit", "false"]:
            break


def looper_auto():
    i = 1
    test = []
    while i <= 100:
        rssi, test = smooth_test(test)
        printer(i, rssi)
        i += 1


def printer(num, rssi):
    if num is 0:
        print("RSSI value test")
        print("===============")
    else:
        print("{}  |  {}".format(num, rssi))


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
    looper_auto()
