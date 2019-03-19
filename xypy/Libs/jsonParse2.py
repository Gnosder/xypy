"""
Make a data object that holds all the json data
TODO - Transfer jsonParse.py into class
data -- json object
events -- int iterable
"""
import datetime
try:
    import xylib as lib
except ModuleNotFoundError:
    import Libs.xylib as lib


class beacon():
    def __init__(self, raw_data, events):
        self.data = raw_data
        self.events = get_events_num(raw_data)
        self.accuracy = get_accuracy(raw_data, self.events)
        self.appversion = get_appversion(raw_data, self.events)
        self.batter =
        self.delta =
        self.deviceid =
        self.eventtype =
        self.latitude =
        self.location
        self.locationtype
        self.longitude
        self.mac
        self.name = get_name(raw_data)
        self.owner
        self.subscription
        self.eventtime
        self.userid
        self.username
        self.uuid

def get_accuracy(data, events, *args):
    """Finds and returns the GPS accuracy of given event."""
    output = []
    for e in range(events):
        accuracy = data["beacons"][0]["beaconEvents"][e]["location"]["accuracy"]
        accuracy = format(accuracy, '.0f')
        output.append(accuracy)
    return output


def get_appversion(data, event, *args):
    """Find and return the version of the
    XY Find It app used to report event."""
    try:
        version = data["beacons"][0]["beaconEvents"][event]["host"]["appVersion"]
    except:
        return "N/A"
    return str(version)


def get_battery(data, event, *args):
    """Finds and returns the battery levels of a given event. Reports 'null'
     if no value given."""
    try:
        battery = data["beacons"][0]["beaconEvents"][event]["batteryLevel"]
        for key in lib.test_batterycodes:
            if battery == key:
                battery = lib.test_batterycodes[key]
        return str(battery)
    except KeyError:
        return "null"


def get_delta(data, event, *args):
    """TODO -- Write desc"""
    if event == 0:
        return "Start"
    stamp1 = data["beacons"][0]["beaconEvents"][event]["createTimestamp"]
    stamp2 = data["beacons"][0]["beaconEvents"][event - 1]["createTimestamp"]
    millis = stamp2 - stamp1
    millis = int(millis)
    seconds=(millis/1000)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)
    hours=(millis/(1000*60*60))%24
    hours = int(hours)

    if hours == 0:
        if minutes == 0:
            delta = "       %02d" % (seconds)
        else:
            delta = "   %02d:%02d" % (minutes, seconds)
    else:
        delta = "%02d:%02d:%02d" % (hours, minutes, seconds)

    return str(delta)


def get_deviceid(data, event, *args):
    """Find and return the id of the device that reported the given event."""
    try:
        did = str(data["beacons"][0]["beaconEvents"][event]["deviceId"])
    except KeyError:
        return "null"
    for key in lib.test_mobiledevices:
        if did == str(key):
            did = lib.test_mobiledevices[key]
    return str(did)


def get_events_num(data):
    length = len(data["beacons"][0]["beaconEvents"])
    return length


def get_eventtype(data, event, *args):
    """Find and returns the update type (Update, Enter, Exit)
    of a given event."""
    et = data["beacons"][0]["beaconEvents"][event]["eventType"]
    return str(et)


def get_geocode(data, event, *args):
    """Requests human readable location from Google. Limited calls per day
    (1500 or so)."""
    lat = data["beacons"][0]["beaconEvents"][event]["location"]["latitude"]
    longi = data["beacons"][0]["beaconEvents"][event]["location"]["longitude"]
    pos = gmap.reverse_geocode((lat, longi))
    pos = pos[0]["formatted_address"]
    return str(pos)


def get_latitude(data, event, *args):
    _latitude = data["beacons"][0]["beaconEvents"][event]["location"]["latitude"]
    return _latitude


def get_location(data, event, *args):
    """Finds and combines the longitude and latitude of a given event into an
    easily selectable format and condenses it to an accuracy of 6 decimal
    points."""
    _latitude = latitude(data, event, *args)
    _latitude = format(_latitude, '.6f')
    _longitude = longitude(data, event, *args)
    _longitude = format(_longitude, '.6f')
    concat = (str(_latitude) + ", " + str(_longitude))
    return str(concat)


def get_locationtype(data, event, *args):
    """Finds and returns the type (BLE or GPS) of a given event."""
    ty = data["beacons"][0]["beaconEvents"][event]["location"]["type"]
    return str(ty)


def get_longitude(data, event, *args):
    _longitude = data["beacons"][0]["beaconEvents"][event]["location"]["longitude"]
    return _longitude


def get_mac(data, event, *args):
    """Finds and returns the MAC address of the beacon being read."""
    invalid_list = ["00", "true", True, "True"]
    macad = str(data["beacons"][0]["beaconEvents"][0]["beaconAddress"])
    if str(macad) in invalid_list:
        try:
            for x in range(event):
                macad = (data["beacons"][0]["beaconEvents"][x]["beaconAddress"])
                if str(macad) not in invalid_list:
                    break
        except IndexError:
            return "IndexError"
        except TypeError:
            return "TypeError"
    return str(macad)


def get_name(data, *args):
    """Finds and returns the name of the beacon being read."""
    try:
        name = (data["beacons"][0]["name"])
    except KeyError:
        return "Unclaimed"
    return str(name)


def get_owner(data, *args):
    """Finds and returns the owener of the beacon being read."""
    owner = (data["beacons"][0]["ownerId"])
    for key in lib.test_userids:
        if owner == key:
            owner = lib.test_userids[key]
    return str(owner)


def get_subscription(data, event, *args):
    """TODO """
    sub_raw = data["beacons"][1]["properties"]["subscription"]
    return sub_raw


def get_subexpire(data, event, *args):
    sub_raw = subscription(data,event)
    exp_raw = sub_raw["expires"]
    exp = datetime.datetime.fromtimestamp(int(exp_raw / 1000))
    return str(exp)


def get_sublevel(data, event, *args):
    pass


def get_time(data, event, *args):
    """Convets and returns the createdTimestamp of a given
    event into human readable text."""
    time = data["beacons"][0]["beaconEvents"][event]["createTimestamp"]
    stamp = datetime.datetime.fromtimestamp(int(time / 1000))
    return str(stamp)


def get_userid(data, event, *args):
    """Find and returns the id of the user that reported the given event."""
    try:
        uid = data["beacons"][0]["beaconEvents"][event]["userId"]
    except:
        uid = "null"
    if uid is not "null" and str(uid) == str(owner(event, data)):
        uid = "Owner"
    return uid


def get_username(data, event, *args):
    """Finds the id of the user that reported the given event and then compares
    it against a list of known user emails and return either the email
    (if it finds one) or the id."""
    try:
        uid = data["beacons"][0]["beaconEvents"][event]["userId"]
    except:
        uid = "null"
    for key in lib.test_userids:
        if uid == key:
            uid = lib.test_userids[key]
        elif uid == owner(data, event):
            uid = "Owner"
    return str(uid)


def get_uuid(data, *args):
    """
    Finds and retursn the ID of the beacon being read.
    GPS ID -- xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.XXXXX.4
    XY4 ID -- xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.XXXXX.XX
    XY3 ID -- xy:ibeacon:08885dd0-111b-11e4-9191-0800200c9a66.XXXX.XXXXX
    XY2 ID -- xy:ibeacon:07775dd0-111b-11e4-9191-0800200c9a66.XXXX.XXXXX
    """

    uuid = str((data["beacons"][0]["id"]))
    if uuid[-1] == '4':
        uuid = uuid[44:-2]
    else:
        uuid = uuid[44:]
    return uuid


# =======
# Tests
# =======
def test():
    try:
        import Libs.xylib as lib
    except ModuleNotFoundError:
        import xylib as lib
    import simplejson as json
    # data = json.loads(lib.test_data_1)
    data, events = lib.clip_data()
    test1 = beacon(data, 5)
    print(vars(test1))
    print(test1.accuracy)


if __name__ == '__main__':
    test()
