from pandas.io.json import json_normalize
import simplejson as json


test_data_1 =""" {"beacons":[{"name":"F1","id":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","ownerId":"sfcr4xqjji","updateTime":"2017-11-03T20:53:01.323Z","createTime":"2017-11-03T15:59:06.724Z","isKeepIt":false,"state":null,"stats":{},"properties":{},"status":"owned","beaconEvents":[{"location":{"accuracy":21,"longitude":-117.1672073,"latitude":32.7172116,"type":"btle"},"distance":-1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"F8:84:4D:EC:81:08","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"EXIT","cache_time":"2017-11-03T20:43:20.436Z","timeSinceCharged":-1,"createTimestamp":1509741800436},{"location":{"accuracy":13,"longitude":-117.1672255,"latitude":32.7172165,"type":"btle"},"distance":1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"F8:84:4D:EC:81:08","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"ENTER","cache_time":"2017-11-03T20:41:16.286Z","timeSinceCharged":-1,"createTimestamp":1509741676286},{"location":{"accuracy":28.822999954223633,"longitude":-117.1674255,"latitude":32.717224,"type":"btle"},"distance":1,"deviceId":"207565581","batteryLevel":100,"host":{"app":"XYFindIt","appVersion":"4.0.2376","os":"3.18.31-11614766(G930AUCS4BQJ2)","osVersion":"7.0(24)","device":"Samsung SAMSUNG-SM-G930A","platform":"android","hardware":"heroqlteatt"},"userId":"sfcr4xqjji","beaconAddress":"E5:10:11:6F:A2:91","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"UPDATE","cache_time":"2017-11-03T20:41:10.281Z","timeSinceCharged":-1,"createTimestamp":1509741670281},{"location":{"accuracy":28.822999954223633,"longitude":-117.1674255,"latitude":32.717224,"type":"btle"},"distance":1,"deviceId":"207565581","batteryLevel":100,"host":{"app":"XYFindIt","appVersion":"4.0.2376","os":"3.18.31-11614766(G930AUCS4BQJ2)","osVersion":"7.0(24)","device":"Samsung SAMSUNG-SM-G930A","platform":"android","hardware":"heroqlteatt"},"userId":"sfcr4xqjji","beaconAddress":"E5:10:11:6F:A2:91","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"ENTER","cache_time":"2017-11-03T20:41:10.163Z","timeSinceCharged":-1,"createTimestamp":1509741670163},{"location":{"accuracy":21.371000289916992,"longitude":-117.1671792,"latitude":32.7172163,"type":"btle"},"distance":-1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"DC:81:16:99:72:D9","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"EXIT","cache_time":"2017-11-03T19:21:30.408Z","timeSinceCharged":-1,"createTimestamp":1509736890408},{"location":{"accuracy":33.374000549316406,"longitude":-117.1676599,"latitude":32.7173001,"type":"btle"},"distance":-1,"deviceId":"207565581","batteryLevel":100,"host":{"app":"XYFindIt","appVersion":"4.0.2376","os":"3.18.31-11614766(G930AUCS4BQJ2)","osVersion":"7.0(24)","device":"Samsung SAMSUNG-SM-G930A","platform":"android","hardware":"heroqlteatt"},"userId":"sfcr4xqjji","beaconAddress":"E5:10:11:6F:A2:91","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"EXIT","cache_time":"2017-11-03T19:17:49.377Z","timeSinceCharged":-1,"createTimestamp":1509736669377},{"location":{"accuracy":104.6729965209961,"longitude":-117.1691877,"latitude":32.7180124,"type":"btle"},"distance":2,"deviceId":"207565581","batteryLevel":100,"host":{"app":"XYFindIt","appVersion":"4.0.2376","os":"3.18.31-11614766(G930AUCS4BQJ2)","osVersion":"7.0(24)","device":"Samsung SAMSUNG-SM-G930A","platform":"android","hardware":"heroqlteatt"},"userId":"sfcr4xqjji","beaconAddress":"E5:10:11:6F:A2:91","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"UPDATE","cache_time":"2017-11-03T19:10:51.267Z","timeSinceCharged":-1,"createTimestamp":1509736251267},{"location":{"accuracy":21.24799919128418,"longitude":-117.1671792,"latitude":32.7172163,"type":"btle"},"distance":1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"DC:81:16:99:72:D9","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"ENTER","cache_time":"2017-11-03T19:10:39.603Z","timeSinceCharged":-1,"createTimestamp":1509736239603},{"location":{"accuracy":21.24799919128418,"longitude":-117.1671792,"latitude":32.7172163,"type":"btle"},"distance":1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"DC:81:16:99:72:D9","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"UPDATE","cache_time":"2017-11-03T19:10:39.281Z","timeSinceCharged":-1,"createTimestamp":1509736239281},{"location":{"accuracy":144,"longitude":-117.1670789,"latitude":32.7174423,"type":"btle"},"distance":-1,"deviceId":"136952610","batteryLevel":-2,"host":{"app":"XYFindIt","appVersion":"4.0.2377","os":"3.10.49-g3d22cfa-00579-g3d0949a(20150803.143047)","osVersion":"5.1(22)","device":"ZTE Z958","platform":"android","hardware":"lol"},"userId":"4zl7yhclds","beaconAddress":"DC:81:16:99:72:D9","beaconId":"xy:ibeacon:a44eacf4-0104-0000-0000-5f784c9977b5.0.20708","eventType":"EXIT","cache_time":"2017-11-03T18:43:52.371Z","timeSinceCharged":-1,"createTimestamp":1509734632371}]}],"api":{"request":"8bad8a18-c0e1-11e7-a31a-8b9a95d0f212","latency":49},"authorization":"xy398d4c40c69b9298a292d42cae08c844eed7c24c2cf5ebe23e54d49c04cf051bd5fa3f917a612cd1424bf0e6a0088e683e5196d396a8e94c22a5c3b3e85e4b1479acb54d9215285d346c76","loggingEnabled":false}"""


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


test_json = json.loads(test_data_1)
flat = flatten_json(test_json)
print(flat)
print(json_normalize(flat))