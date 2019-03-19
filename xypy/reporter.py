from datetime import date
import csv as CSV
import Libs.jsonParse as parse
import os
import simplejson as json
import sys
import Libs.xyapi as api
import Libs.xylib as lib

def report(gps_dict = lib.test_uuids, events_requested = lib.events_requested,
           header = lib.header):
    """
    gps_dict = {"Name": UUID}
    events_requested type = int
    header do not pass
    """
    log(gps_dict, events_requested, header)
    csv_date = str(date.today())

    # File Path
    root_path = os.path.join(sys.path[0], "data")
    file_name = "%s.csv" % (csv_date)
    file_path = os.path.join(root_path, file_name)

    # Star CSV write
    with open(file_path, "w", newline="") as report:
        # C:\Users\patrick.plaisted\Google Drive\Code\xypy\Data
        report = CSV.writer(report, delimiter=",")
        # Create CSV Header
        report.writerow(header)
        # Get beacon API data
        for gps in gps_dict:
            gps_api_json = api.get_beaconevents(gps_dict[gps], events_requested)
            print("API(%s, %s) SUCCESS" % (gps, events_requested))
        # Parse JSON and write rows
            _events_num = parse.events_num(gps_api_json)
            for event in range(_events_num):
                row = []
                for h in header:
                    h = h.lower()
                    row.append(getattr(parse, h)(gps_api_json, event))
                report.writerow(row)
            print("%s WRITTEN" % (gps))

        os.system('start excel.exe "%s\\%s.csv"' % (root_path, csv_date))


def log(gps_dict, events_requested, header):
    # TODO replace print with logging
    print("Start console log")
    print("Header items are {}".format(header))
    print("{} events requested".format(events_requested))
    print("Gathering data on the following GPS units:")
    for gps in gps_dict:
        print(gps)
    print("End Log")


def debug():
    pass


def tests():
    report()


if __name__ == '__main__':
    try:
        tests()
    except:
        print(sys.exc_info()[0])
        print(traceback.format_exec())
        input("Press Enter to exit.")
