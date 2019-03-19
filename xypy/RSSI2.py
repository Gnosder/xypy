# Global Imports
import os, sys

# Global Variables
TX = -60
line = 80


def get_tx(tx = -60):
    global TX
    TX = tx
    return TX


def range_band(dist):
    if dist < -1.0:
        return "!"
    elif dist < 0.0173:
        return "A"
    elif dist < 1.0108:
        return "B"
    elif dist < 3.0639:
        return "C"
    elif dist < 8.3779:
        return "D"
    elif dist < 20.6086:
        return "E"
    else:
        return "!"


def calc_dist(rssi, c1 = 0.89976, c2 = 7.7095, c3 = 0.111, tx = TX):
    ratio = float(rssi) / tx
    if ratio < 1.0:
        return calc_std_dist(ratio)
    else:
        return (c1 * (ratio ** c2)) + c3


def calc_std_dist(ratio):
    return ratio ** 10


def calc_tst(rssi, tx = TX):
    r = rssi / 100
    return r ** 3


def build_scale():
    """Returns list of numbers from 0 to -100 for RSSI base"""
    rssi_list = range(-100,0)
    rssi_list = rssi_list[::-1]
    return rssi_list


def rand_list(in_list = None):
    from random import randint
    if in_list is None:
        in_list = build_scale()
    for x in in_list:
        in_list[x] = randint(tx-20, tx+20)
    return in_list


def top():
    top1 = '{:^{space}}'.format("RSSI Value Test", space = line) + "\n"
    top2 = '{:=^{space}}'.format('=', space = line) + "\n"
    return top1, top2


def head_row(row):
    out = ""
    for i in row:
        _line = col(i)
        out += ("{:^{line}}".format(i, line = _line) + "|")
    return out


def col(head):
    if isinstance(head, str):
        return 8
    else:
        return 10


def body(scale, row):
    out = ""
    b = []
    for n in scale:
        r = ''
        for i in row:
            if i is "RSSI":
                p = n
            else:
                p = calc_dist(n, tx = i)
            if isinstance(p, float):
                rb = range_band(p)
                p = str(rb) + " " + str(p)
                r += ("{:^10.8}".format(p) + "|")
            else:
                r += ("{:^8}".format(p) + "|")
        b.append(r)
    return b


def print_out(head):
    top1, top2 = top()
    print(top1)
    print(top2)
    print(head_row(head))
    scale = build_scale()
    b = body(scale, head)
    for x in range(len(b)):
        print(b[x])


def write_out(head):

    file_name = "RSSI Test.txt"
    data_path = os.path.join(sys.path[0], "data")
    file_path = os.path.join(data_path, file_name)
    with open(file_path, "w") as output:
        top1, top2 = top()
        output.write(top1)
        output.write("\n")
        output.write(top2)
        output.write("\n")

        output.write(head_row(head))
        output.write("\n")

        scale = build_scale()
        b = body(scale, head)
        for x in range(len(b)):
            output.write(b[x])
            output.write("\n")


def main(head = None):
    if head is None:
        head = ["RSSI", -40, -50, -59, -60, -65, -70, -80]
    test = ["RSSI", TX]
    # write_out(test)
    # print_out(test)
    # print_out()
    write_out(head)


if __name__ == '__main__':
    main()
