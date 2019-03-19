events_requested = 100

#gmap = maps.Client(key='AIzaSyBqHB0Imgn3jtXZ6uSawg8-6ZlLuv3FBF8')
api_stage = "api"

api_version = "2.2"

header = ["Name", "UUID", "Time", "Location",
          "locationType", "eventType", "deviceid", "username",
          "Battery", "appversion", "mac"]

test_userids = {"rzub364dvi": "alex.mcelroy@xyfindables.com",
                "wa9lzyqlku": "patrick.plaisted@gmail.com",
                "ni4w7jv7h1": "patrick.plaisted@xyfindables.com",
                "6xmm8i8t9g": "patrick.plaisted@xyfindables.com_deleted_0",
                "cjsglbsf7w": "patrick.plaisted+1@xyfindables.com_deleted_0",
                "7q28hv6qtj": "patrick.plaisted@webble.com",
                "6643u63vtk": "patrick.plaisted@webble.com_deleted_0",
                "1c6s5qwsik": "patrick.plaisted@webble.com_deleted_1",
                "a8apynez4e": "patrick.plaisted@webble.com_deleted_2",
                "sn1qsv4ti6": "patrick.plaisted@webble.com_deleted_3",
                "g17sse79k5": "patrick.plaisted+1@webble.com_deleted_0",
                "cypyzkv5b1": "patrick.plaisted+s@webble.com_deleted_1",
                "b6pq3hemdt": "patrick.plaisted@xyfindit.com_deleted_0",
                "crk62c6kfx": "patrick.plaisted@xyfindit.com",
                "hgu8ntw2ck": "patrick.plaisted@xyfindit.com_deleted_0",
                "4zl7yhclds": "xyalextest@gmail.com",
                "r86ulg8a52": "john.pallag@gmail.com",
                "t2lkQiSi2j": "john.pallag@webble.com",
                "4v12s1zqgd": "john.murcko@xyfindit.com",
                "932xywYmfc": "gabriela.dlt@live.com",
                "896cqblzif": "maryann.cummings@xyfindit.com",
                "441wwfyw92": "c.whitsell@hotmail.com",
                "9q3ufhvw1l": "robert.edmonston@xyfindables.com",
                "sfeax7tsqu": "bob@inzan.com",
                "7SlDuJTBSo": "replai75@gmail.com",
                "60Mf7Z08h6": "arie.trouw@gmail.com",
                "7M5AGxqEFY": "anne.trouw@gmail.com",
                "gps":        "GPS"}

test_mobiledevices = {258500704: "Gal S5",
                      73619995:  "Gal S3",
                      13040258:  "Note 2",
                      10618873:  "Pixel XL?",
                      121585840: "Pixel XL?",
                      227874928: "Pixel XL?",
                      209651209: "Mota XT",
                      136952610: "ZTE ZMAX",
                      182799212: "Nexus 4",
                      34502653:  "LGE LG-K",
                      130762878: "Moto G5+",
                      143960909: "Moto XT1585",
                      123:       "GPS"}

test_batterycodes = {-1: "Checked(-1)",
                     -2: "Not Checked(-2)",
                     -3: "Scheduled(-3)"}

test_uuids = {'Mum':    17296.4,
              'Red 17': 61465.4,
              'Blue 1': 40528.4,
              'Blue 2': 41184.4,
              'Blue 3': 40944.4,
              'Blue 4': 41120.4,
              'Blue 5': 40608.4,
              'Blue 6': 40928.4,
              'Blue 7': 40816.4,
              'Blue 8': 41136.4,
              '40048':  40048.4,
              '39760':  39760.4,
              '39696':  39696.4,
              '40000':  40000.4,
              '41168':  41168.4,
              '43344':  43344.4,
              '43136':  43136.4,
              '42704':  42704.4,
              '43072':  43072.4,
              '320':    320.4,
              '336':    336.4,
              'narp?':  43936.4,
              'Kangaroo': 43520.4,
              'Iran Deal': 43440.4,
              'Gwar':   43872.4}


test_data_1 = '''{
    "beacons": [
        {
            "name": "Kapla",
            "id": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
            "ownerId": "cypyzkv5b1",
            "updateTime": "2017-07-28T23:27:27.033Z",
            "createTime": "2017-06-28T22:31:57.596Z",
            "isKeepIt": false,
            "state": null,
            "stats": {},
            "properties": {},
            "status": "owned",
            "beaconEvents": [
                {
                    "location": {
                        "accuracy": 24,
                        "longitude": -117.1680549,
                        "latitude": 32.7178883,
                        "type": "btle"
                    },
                    "distance": -1,
                    "deviceId": "258500704",
                    "batteryLevel": -2,
                    "host": {
                        "app": "XYFindIt",
                        "appVersion": "3.50.2355",
                        "os": "3.4.0-8025411(G900VVRS2DQB2)",
                        "osVersion": "6.0.1(23)",
                        "device": "Galaxy S5",
                        "platform": "android",
                        "hardware": "kltevzw"
                    },
                    "userId": "rzub364dvi",
                    "beaconAddress": "00:04:48:90:00:04",
                    "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
                    "eventType": "EXIT",
                    "cache_time": "2017-07-28T20:30:43.208Z",
                    "timeSinceCharged": -1,
                    "createTimestamp": 1501273843208
                },
                {
                    "location": {
                        "accuracy": 81,
                        "longitude": -117.168397,
                        "latitude": 32.7181674,
                        "type": "btle"
                    },
                    "distance": 1,
                    "deviceId": "258500704",
                    "batteryLevel": -2,
                    "host": {
                        "app": "XYFindIt",
                        "appVersion": "3.50.2355",
                        "os": "3.4.0-8025411(G900VVRS2DQB2)",
                        "osVersion": "6.0.1(23)",
                        "device": "Galaxy S5",
                        "platform": "android",
                        "hardware": "kltevzw"
                    },
                    "userId": "rzub364dvi",
                    "beaconAddress": true,
                    "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
                    "eventType": "ENTER",
                    "cache_time": "2017-07-28T20:24:35.490Z",
                    "timeSinceCharged": -1,
                    "createTimestamp": 1501273475490
                },
                {
                    "location": {
                        "accuracy": 115.40899658203125,
                        "longitude": -117.1672806,
                        "latitude": 32.7172063,
                        "type": "btle"
                    },
                    "distance": 1,
                    "deviceId": "121585840",
                    "batteryLevel": -3,
                    "host": {
                        "app": "XYFindIt",
                        "appVersion": "3.50.2355",
                        "os": "3.18.31-g80c8372084ef(4051500)",
                        "osVersion": "7.1.2(25)",
                        "device": "Google Pixel XL",
                        "platform": "android",
                        "hardware": "marlin"
                    },
                    "userId": "cypyzkv5b1",
                    "beaconAddress": true,
                    "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
                    "eventType": "ENTER",
                    "cache_time": "2017-07-28T20:24:33.311Z",
                    "timeSinceCharged": -1,
                    "createTimestamp": 1501273473311
                },
                {
                    "location": {
                        "accuracy": 66,
                        "longitude": -117.1683971,
                        "latitude": 32.7181672,
                        "type": "btle"
                    },
                    "distance": 1,
                    "deviceId": "258500704",
                    "batteryLevel": -2,
                    "host": {
                        "app": "XYFindIt",
                        "appVersion": "3.50.2355",
                        "os": "3.4.0-8025411(G900VVRS2DQB2)",
                        "osVersion": "6.0.1(23)",
                        "device": "Galaxy S5",
                        "platform": "android",
                        "hardware": "kltevzw"
                    },
                    "userId": "rzub364dvi",
                    "beaconAddress": true,
                    "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
                    "eventType": "ENTER",
                    "cache_time": "2017-07-28T20:24:32.705Z",
                    "timeSinceCharged": -1,
                    "createTimestamp": 1501273472705
                },
                {
                    "location": {
                        "accuracy": 22.224000930786133,
                        "longitude": -117.1671562,
                        "latitude": 32.7172012,
                        "type": "btle"
                    },
                    "distance": 1,
                    "deviceId": "209651209",
                    "batteryLevel": -2,
                    "host": {
                        "app": "XYFindIt",
                        "appVersion": "3.50.2355",
                        "os": "3.18.31-perf-gf651357-00001-gf7a6332(4)",
                        "osVersion": "7.0(24)",
                        "device": "Motorola XT1635-01",
                        "platform": "android",
                        "hardware": "addison"
                    },
                    "userId": "rzub364dvi",
                    "beaconAddress": true,
                    "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.22144.4",
                    "eventType": "ENTER",
                    "cache_time": "2017-07-28T20:24:32.587Z",
                    "timeSinceCharged": -1,
                    "createTimestamp": 1501273472587
                }
            ]
        }
    ],
    "api": {
        "request": "68ab6b9b-73ec-11e7-899d-133ea01beab5",
        "latency": 62
    },
    "authorization": "xy398d4c40c69b9298a292d42cae08c844eed7c24c2cf5ebe23e54d49"
                     "c04cf051bd5fa3f917a612cd1424bf0e6a0088e683e5196d396a8e94c"
                     "22a5c3b3e85e4b1471a9b94f961b2e5b376076"
}'''


def clip_data():
    """
    Must be given a valid JSON object to parse
    """
    try:
        import Libs.jsonParse as parse
    except ModuleNotFoundError:
        import jsonParse as parse
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
