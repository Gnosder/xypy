from datetime import date
import Libs.jsonParse as parse
import os
import pyperclip
import simplejson as json
import sys
import Libs.xyapi as api
import Libs.xylib as lib


def text(header=lib.header):
    data, events = lib.clip_data()
    line, settings = config(lib.header)
    # notepad_kill()
    file_name = parse.name(data) + ".txt"
    file_path = os.path.join(path(), file_name)

    with open(file_path, "w") as output:
        output.write(row("+", line))
        # Header
        for x in ("Name", "UUID", "MAC", "OWNER"):
            y = getattr(parse, x.lower())
            temp_row = "| %s -- %s" % (x, y(data, events))
            fill_line = line - len(temp_row)
            temp_row = temp_row + (" " * fill_line) + "|\n"
            output.write(temp_row)
        output.write(row("+", line))
        output.write("|")
        for x in header:
            output.write(center(x, x, settings) + "|")
        output.write("\n")
        output.write(row("=", line))
        # Body
        for x in range(events):
            output.write("|")
            for y in header:
                _temp = getattr(parse, y.lower())
                _temp = center(_temp(data, x), y, settings)
                output.write(_temp + "|")
            output.write("\n")
        output.write(row("+", line))
    notepad_open(file_name)


def text_class(header = lib.header):
    data, events = lib.clip_data()
    line, settings = config(lib.header)
    # notepad_kill()
    file_name = parse.name(data) + ".txt"
    file_path = os.path.join(path(), file_name)

    with open(file_path, "w") as output:
        output.write(row("+", line))
        # Header
        for x in ("Name", "UUID", "MAC", "OWNER"):
            y = getattr(parse, x.lower())
            temp_row = "| %s -- %s" % (x, y(data, events))
            fill_line = line - len(temp_row)
            temp_row = temp_row + (" " * fill_line) + "|\n"
            output.write(temp_row)
        output.write(row("+", line))
        output.write("|")
        for x in header:
            output.write(center(x, x, settings) + "|")
        output.write("\n")
        output.write(row("=", line))
        # Body
        for x in range(events):
            output.write("|")
            for y in header:
                _temp = getattr(parse, y.lower())
                _temp = center(_temp(data, x), y, settings)
                output.write(_temp + "|")
            output.write("\n")
        output.write(row("+", line))
    notepad_open(file_name)


def center(input_str, header, settings, *args):
    if header in settings:
        line = settings[header]
        output = "{:^{line}}".format(input_str, line=line)
    else:
        print("error")

    if len(output) > line:
        output = output[:line]
    return output


def config(header, *args):
    settings = {}
    line = 0
    for x in header:
        settings[x] = len(x) + 5
    if "Time" in header:
        settings["Time"] = 26
    if "Location" in header:
        settings["Location"] = 27
    if "Delta" in header:
        settings["Delta"] = 16
    if "GeoCode" in header:
        settings["GeoCode"] = 55
    if "username" in header:
        settings["username"] = 45
    if "Battery" in header:
        settings["Battery"] = 18
    if "macad" in header:
        settings["macad"] = 20
    for key in settings:
        line = line + settings[key] + 1
    return line, settings


def notepad_kill():
    try:
        os.system('taskkill /IM notepad.exe')
    except:
        pass
    finally:
        return "notepad-kill complete"


def notepad_open(name):
    data_path = path()
    os.system('start notepad.exe "%s\\%s"' % (data_path, name))

def path():
    data_path = os.path.join(sys.path[0], "data")
    return data_path


def row(char, line, *args):
    row = char * (line + 1) + "\n"
    return row


def tests():
    header = lib.header
    header.remove("Battery")
    header.remove("mac")
    header.insert(3, "Delta")
    text(header)


if __name__ == '__main__':
    # tests()
    # input("")
    try:
        tests()
    except:
        print(sys.exc_info()[0])
        print(traceback.format_exec())
        input("Press Enter to exit.")
