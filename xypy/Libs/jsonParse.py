import datetime
try:
    import xylib as lib
except ModuleNotFoundError:
    import Libs.xylib as lib


def accuracy(data, event, *args):
    """Finds and returns the GPS accuracy of given event."""
    accuracy = data["beacons"][0]["beaconEvents"][event]["location"]["accuracy"]
    accuracy = format(accuracy, '.0f')
    return str(accuracy)


def appversion(data, event, *args):
    """Find and return the version of the
    XY Find It app used to report event."""
    try:
        version = data["beacons"][0]["beaconEvents"][event]["host"]["appVersion"]
    except:
        return "N/A"
    return str(version)


def battery(data, event, *args):
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


def delta(data, event, *args):
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


def deviceid(data, event, *args):
    """Find and return the id of the device that reported the given event."""
    try:
        did = str(data["beacons"][0]["beaconEvents"][event]["deviceId"])
    except KeyError:
        return "null"
    for key in lib.test_mobiledevices:
        if did == str(key):
            did = lib.test_mobiledevices[key]
    return str(did)


def events_num(data):
    length = len(data["beacons"][0]["beaconEvents"])
    return length


def eventtype(data, event, *args):
    """Find and returns the update type (Update, Enter, Exit)
    of a given event."""
    et = data["beacons"][0]["beaconEvents"][event]["eventType"]
    return str(et)


def geocode(data, event, *args):
    """Requests human readable location from Google. Limited calls per day
    (1500 or so)."""
    lat = data["beacons"][0]["beaconEvents"][event]["location"]["latitude"]
    longi = data["beacons"][0]["beaconEvents"][event]["location"]["longitude"]
    pos = gmap.reverse_geocode((lat, longi))
    pos = pos[0]["formatted_address"]
    return str(pos)


def latitude(data, event, *args):
    _latitude = data["beacons"][0]["beaconEvents"][event]["location"]["latitude"]
    return _latitude


def location(data, event, *args):
    """Finds and combines the longitude and latitude of a given event into an
    easily selectable format and condenses it to an accuracy of 6 decimal
    points."""
    _latitude = latitude(data, event, *args)
    _latitude = format(_latitude, '.6f')
    _longitude = longitude(data, event, *args)
    _longitude = format(_longitude, '.6f')
    concat = (str(_latitude) + ", " + str(_longitude))
    return str(concat)


def locationtype(data, event, *args):
    """Finds and returns the type (BLE or GPS) of a given event."""
    ty = data["beacons"][0]["beaconEvents"][event]["location"]["type"]
    return str(ty)


def longitude(data, event, *args):
    _longitude = data["beacons"][0]["beaconEvents"][event]["location"]["longitude"]
    return _longitude


def mac(data, event, *args):
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


def name(data, *args):
    """Finds and returns the name of the beacon being read."""
    try:
        name = (data["beacons"][0]["name"])
    except KeyError:
        return "Unclaimed"
    return str(name)


def owner(data, *args):
    """Finds and returns the owener of the beacon being read."""
    owner = (data["beacons"][0]["ownerId"])
    for key in lib.test_userids:
        if owner == key:
            owner = lib.test_userids[key]
    return str(owner)


def subscription(data, event, *args):
    """TODO """
    sub_raw = data["beacons"][1]["properties"]["subscription"]
    return sub_raw


def subexpire(data, event, *args):
    sub_raw = subscription(data,event)
    exp_raw = sub_raw["expires"]
    exp = datetime.datetime.fromtimestamp(int(exp_raw / 1000))
    return str(exp)


def sublevel(data, event, *args):
    pass


def time(data, event, *args):
    """Convets and returns the createdTimestamp of a given
    event into human readable text."""
    time = data["beacons"][0]["beaconEvents"][event]["createTimestamp"]
    stamp = datetime.datetime.fromtimestamp(int(time / 1000))
    return str(stamp)


def userid(data, event, *args):
    """Find and returns the id of the user that reported the given event."""
    try:
        uid = data["beacons"][0]["beaconEvents"][event]["userId"]
    except:
        uid = "null"
    if uid is not "null" and str(uid) == str(owner(event, data)):
        uid = "Owner"
    return uid


def username(data, event, *args):
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


def uuid(data, *args):
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
