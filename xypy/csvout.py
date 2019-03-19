from datetime import date
import csv
import Libs.jsonParse as parse
import os
import pyperclip
import simplejson as json
import sys
import xyapi as api
import Libs.xylib as lib


def csv_make(header=lib.header):
    data, events = lib.clip_data()

    file_name = parse.name(data) + ".csv"
    file_path = os.path.join(path(), file_name)

    with open(file_path, "w", newline="") as output:
        output = csv.writer(output, delimiter=",")
        output.writerow(header)
        for event in range(events):
            row = []
            for h in header:
                h = h.lower()
                row.append(getattr(parse, h)(data, event))
            output.writerow(row)
    excel_open(file_name)


def excel_kill():
    pass
    try:
        os.system('taskkill /IM notepad.exe')
    except:
        pass
    finally:
        return "notepad-kill complete"


def excel_open(name):
    data_path = path()
    os.system('start excel.exe "%s\\%s"' % (data_path, name))

def path():
    data_path = os.path.join(sys.path[0], "data")
    return data_path


def tests():
    header = lib.header
    csv_make(header)



if __name__ == '__main__':
    # tests()
    # input("")
    try:
        tests()
    except:
        print(sys.exc_info()[0])
        print(traceback.format_exec())
        input("Press Enter to exit.")
