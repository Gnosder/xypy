"""
Get Data from clipboard
Either from copied JSON or copied GUID
Get data from user imput
"""
import pyperclip
import simplejson as json


def gd_mai(guid = 0, *args, **kwargs):


def clip_data():
    """
    Must be given a valid JSON object to parse
    """
    import Libs.jsonParse as parse
    import pyperclip
    import simplejson as json
    while True:
        data = pyperclip.paste()
        try:
            data = json.loads(data)
            if validate(data):
                break
            else:
                print("Finder unclaimed, no beaconevents to show.")
                input("Press Enter to continue...")
        except:
            try:
                import Libs.xyapi as api
            except ModuleNotFoundError:
                import xyapi as api
            input_id = input("Invalid data, press Enter to try again"
                             " or enter ID and count.   ")
            if input_id is not "":
                input_split = input_id.split()
                data = api.get_beaconevents(input_split[0], input_split[1])
                if validate(data):
                    break
                else:
                    print("Finder unclaimed, no beaconevents to show.")
    events = parse.events_num(data)
    return data, events


def validate(data):
    """
    Take json object as input, check to see if json object is valid,
    return Ture or False
    """
    status = data["beacons"][0]["status"]
    if status in ["unclaimed"]:
        return False
    elif status in ["owned", "claimed"]:
        return True
    else:
        print("Error reading status")
        print("Status is %s" % (status))
        return False
