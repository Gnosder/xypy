try:
    import Libs.xylib as lib
except ModuleNotFoundError:
    import xylib as lib
import simplejson as json
import urllib
import urllib.request


def get_beaconevents(_uuid, _events):
    # Move apibody to apilib.beaconevent.read
    api_body = {"action": "read",
               "host": {"os": "osx",
                        "osVersion": "10.11.3",
                        "app": "postman",
                        "appVersion": "3.2.16",
                        "hardware": "MacBookPro11,2"
                        },
               "maxCount": _events,
               "ids": ["xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.%s"
                       % (_uuid)
                       ]
               }
    url = urlGet()
    data, head = clen(api_body)
    req = urllib.request.Request(url, data=data, headers=head)
    resp = urllib.request.urlopen(req)

    # turn bytes into json object
    resp_bytes = resp.read()
    resp_json = resp_bytes.decode('utf8').replace("'", '"')
    resp_json = json.loads(resp_json)

    # Return json object
    return resp_json


def get_status(endpoint_url, action_body):
    data, head = clen(action_body)
    req = urllib.request.Request(endpoint_url, data=data, headers=head)
    reason = ''
    try:
        resp = urllib.request.urlopen(req, timeout=3)
    except urllib.error.HTTPError as e:
        status = str(e.code)
        reason = str(e.reason)
    except urllib.error.URLError as e:
        status = 'URLError'
    else:
        status = '200'
    return status, reason


def urlGet(stage = lib.api_stage, version = lib.api_version, call = "beaconevent"):
    url = "https://%s.xyfindit.com/%s/%s" % (stage, version, call)
    return url


def clen(action_body):
    head = {'Authorization': 'xy398d4c40c69b9298a292d42cae08c844eed7c24c2cf5'
                                'ebe23e54d49c04cf051bd5fa3f917a612cd1424bf0e6a0'
                                '088e683e5196d396a8e94c22a5c3b3e85e4a1d78abb748'
                                '9a17285f316b76',
               'Content-type':  'application/json',
               'x-api-key':     'nJUi4EOxR93mCwrSt4H6S6mpSeg2jSByzQGww8z5'}
    data = json.dumps(action_body).encode('utf8')
    head['Content-Length'] = len(data)
    return data, head


# Tests
# print(call(17296.4, 150))  # Mum
