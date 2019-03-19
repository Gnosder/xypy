import Libs.apicalllib as apicall
import Libs.xyapi as api
import Libs.xylib as lib
import sys
import os
from datetime import date


def tests():
    # api_test_outlog(stage = "betaapi")
    api_test_outlog(stage = "api")

def api_test_outlog(stage = lib.api_stage, version = lib.api_version,
                    api_list = apicall.api_endpoint_list):
    file_name = "api_test_log.txt"
    file_path = os.path.join(path(), file_name)
    with open(file_path, "a") as log:
        # Prime new log entry
        log_start = ["XY QA API STATUS TEST",
                     "LOG DATE: %s" % (date.today()),
                     "API STAGE: %s" % (stage.upper()),
                     "API VERSION: %s" % (version),
                     "======================"]
        for line in log_start:
            print(line)
            log.write(line + '\n')
        for endpoint in api_list:
            endpoint_url = api.urlGet(call = endpoint)
            action_dict = {}
            call = getattr(apicall, endpoint)
            action_dict = call()
            for action in action_dict:
                if action_dict[action] is "Skipped":
                    output = "{} status is: Skipped".format(action.upper())
                else:
                    action_status, action_reason = api.get_status(endpoint_url,
                                                               action_dict[action])
                    output = "{} status is: {}  {}".format(action.upper(),
                                                           action_status.upper(),
                                                           action_reason.upper())
                log.write(output + '\n')
                print(output)
        log_end = ["======================",
                   "All API calls complete"
                   "\n"
                   "\n"
                   "\n"]
        for line in log_end:
            print(line)
            log.write(line + '\n')





def path():
    data_path = os.path.join(sys.path[0], "data")
    return data_path


if __name__ == '__main__':
    # tests()
    # input("")
    try:
        tests()
    except:
        print(sys.exc_info()[0])
        print(traceback.format_exec())
        input("Press Enter to exit.")
