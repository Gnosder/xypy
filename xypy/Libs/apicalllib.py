api_endpoint_list = ['about',
                     'account',
                     'beacon',
                     'beaconsubscription',
                     'beaconevent',
                     'config',
                    #  'developer',
                     'error',
                     'ifttt',
                    #  'image',
                    #  'invest',
                    #  'metric',
                    #  'oauth2',
                    #  'prismPro',
                    #  'role',
                    #  'share',
                    #  'subscription',
                    #  'support',
                    #  'voucher',
                     'zapier']   # List of each API call and Function

# Calls Library
def about():
    get = {"action": "get",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"
                      }
            }
    return {"about_get": get}


def account():
    read ={"action": "read",
           "host" : {"os" : "osx",
                     "osVersion" : "10.11.3",
                     "app" : "postman",
                     "appVersion" : "3.2.16",
                     "hardware" : "MacBookPro11,2"},
            "user":{"id":"uuvwd5ztnx"}}

    signin = {"action": "signin",
              "target":"account",
              "host" : {"os" : "osx",
                        "osVersion" : "10.11.3",
                        "app" : "postman",
                        "appVersion" : "3.2.16",
                        "hardware" : "MacBookPro11,2"},
              "user": {"password" : "qwerty",
                       "email" : "xydevv+99@gmail.com"}}

    update = {"action": "update",
              "host" : {"os" : "osx",
                        "osVersion" : "10.11.3",
                        "app" : "postman",
                        "appVersion" : "3.2.16",
                        "hardware" : "MacBookPro11,2"},
              "user": {"username": "xydevv+99@gmail.com",
                       "email": "xydevv+99@gmail.com",
                       "firstName": "API",
                       "lastName": "Test",
                       "id": "26n89v4rin",
                       "properties":{"photoUrl":"https://lh4.googleuserconte"
                                     "nt.com/Dfqo9J42K7-xRvHW3GVpTU7YCa_zpy3"
                                     "kEDSIlKjpd2RAvVlNfZe5pn8Swaa4TgCWNTuOJ"
                                     "OAfwWY=s50-h50-e365"}}}

    # Skipped because it's not a safe action to call
    # add ={"action": "add",
    #       "host" : {"os" : "osx",
    #                 "osVersion" : "10.11.3",
    #                 "app" : "postman",
    #                 "appVersion" : "3.2.16",
    #                 "hardware" : "MacBookPro11,2"},
    #       "user": {"email": "xydevv+98@gmail.com",
    #                "password": "qwerty",
    #                "firstName": "API",
    #                "lastName": "Test2",
    #                "facebookToken": ""}}
    add = "Skipped"

    reset ={"action": "reset",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
           "user": {"email": "xydevv+98@gmail.com"}}

    verify ={"action": "verify",
             "host" : {"os" : "osx",
                       "osVersion" : "10.11.3",
                       "app" : "postman",
                       "appVersion" : "3.2.16",
                       "hardware" : "MacBookPro11,2"},
             "user": {"email": "xydevv+99@gmail.com",
                      "id":"26n89v4rin"}}

    sendverification ={"action": "sendVerification",
                       "host" : {"os" : "osx",
                                 "osVersion" : "10.11.3",
                                 "app" : "postman",
                                 "appVersion" : "3.2.16",
                                 "hardware" : "MacBookPro11,2"},
                        "user": {"email": "xydevv+99@gmail.com",
                                 "firstName":"API",
                                 "lastName":"Test",
                                 "id":"26n89v4rin"}}

    push = {"action" : "push",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "settings":{"action": "update"}}

    addtoken = {"action" : "addtoken",
                "host" : {"os" : "osx",
                          "osVersion" : "10.11.3",
                          "app" : "postman",
                          "appVersion" : "3.2.16",
                          "hardware" : "MacBookPro11,2"},
                "token" : {"token" : "xxxxx",
                           "platform" : "ios",
                           "deviceId" : "zzzzzz"}}

    return {"account_read": read,
            "account_signin": signin,
            "account_update": update,
            "account_add": add,
            "account_reset": reset,
            "account_verify": verify,
            "account_sendverification": sendverification,
            "account_push": push,
            "account_addtoken": addtoken}




def beacon():
    read = {"action": "read",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "ids": ["xy:gps:a500248c-test-test-t5st-034f4fc9ed10.ruyl.qmt2"]}

    sync = {"action" : "sync",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "beacon" : {"name": "Testy",
                        "id": "xy:ibeacon:08885dd0-111b-11e4-9191-0800200c9a66."
                              "9253.58884",
                        "ownerId": "uuvwd5ztnx",
                        "updateTime": "2019-11-23T18:46:41.269Z",
                        "createTime": "2019-11-23T18:46:41.269Z",
                        "stats": {},
                        "properties": {"isMultiBeacon": 'true',
                                       "isKeepIt":'false'},
                        "status": "owned"}}


    return {"beacon_read": read,
            "beacon_sync": sync}

def beaconsubscription():
    read = {"action": "read",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "beaconId": "xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.43440.4"}

    return {"beaconsubscriptions_read": read}

def beaconevent():
    read ={"action": "read",
           "host" : {"os" : "osx",
                     "osVersion" : "10.11.3",
                     "app" : "postman",
                     "appVersion" : "3.2.16",
                     "hardware" : "MacBookPro11,2"},
           "maxCount" : 5,
           "ids":["xy:gps:9474f7c6-47a4-11e6-beb8-9e71128cae77.43440.4"]}

    add = {"action":"add",
           "host" : {"os" : "osx",
                     "osVersion" : "10.11.3",
                     "app" : "postman",
                     "appVersion" : "3.2.16",
                     "hardware" : "MacBookPro11,2"},
          "beaconEvents": [{"eventType": "EXIT",
                            "deviceId": "666",
                            "id": "xy:ibeacon:08885dd0-111b-11e4-9191-0800200c9"
                                  "a66.9253.58884",
                            "userId": "666",
                            "createTimestamp": '1458871460002',
                            "location": {"latitude": '33.7485587',
                                         "longitude": '-116.355199',
                                         "accuracy": '23.0629997253418',
                                         "name": ""},
         "distance": '31.2088061674259',
         "beaconAddress": "none",
         "batteryLevel": '94',
         "isMuted": 'no',
         "firmwareVersion": "666"}]}

    return {"beaconevent_read": read,
            "beaconevent_add": add}

def config():
    read ={"action": "read",
           "host" : {"os" : "osx",
                     "osVersion" : "10.11.3",
                     "app" : "postman",
                     "appVersion" : "3.2.16",
                     "hardware" : "MacBookPro11,2"},
           "platform": "ios"}

    update ={"action": "update",
             "host" : {"os" : "osx",
                       "osVersion" : "10.11.3",
                       "app" : "postman",
                       "appVersion" : "3.2.16",
                       "hardware" : "MacBookPro11,2"},
             "platform": "ios",
             "config":{}}

    reset ={"action": "reset",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "platform": "ios"}

    return {"config_read": read,
            "config_update": update,
            "config_reset": reset}


def developer():
    createDeveloper = "Skipped"

    addWebhook = "Skipped"

    testWebhook = "Skipped"

    addTarget = "Skipped"

    removeTarget = "Skipped"

    getWebhooks = "Skipped"

    return {"developer_createDeveloper": createDeveloper,
            "developer_addWebhook": addWebhook,
            "developer_testWebhook": testWebhook,
            "developer_addTarget": addTarget,
            "developer_removeTarget": removeTarget,
            "developer_getWebhooks": getWebhooks}



def error():
    read = {"action": "read",
            "host" : {"os" : "osx",
                      "osVersion" : "10.11.3",
                      "app" : "postman",
                      "appVersion" : "3.2.16",
                      "hardware" : "MacBookPro11,2"},
            "ids": ["jkghdfjkg"],
            "settings": {"verbose": 'true',
                         "details": 'true'}}

    return {"error_read": read}


def ifttt():
    triggers = {"action": "trigger",
                "id":"xy:ibeacon:08885dd0-111b-11e4-9191-0800200c9a66.9253"
                     ".58884",
                "type":"single_press",
                "settings":{"verbose":'true'}}

    return {"ifttt_triggers": triggers}


def image():
    upload = {"action": "upload",
              "host" : {"os" : "osx",
                        "osVersion" : "10.11.3",
                        "app" : "postman",
                        "appVersion" : "3.2.16",
                        "hardware" : "MacBookPro11,2"},
              "settings":{"verbose": 'true'},
              "image":{"extension": "png",
    "data": """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"""}}

    importURL = "Skipped"

    importS3 = "Skipped"

    upload2 = "Skipped"

    return {"image_upload": upload,
            "image_importURL": importURL,
            "image_importS3": importS3,
            "image_upload2": upload2}


def invest():
    rewards = "Skipped"

    getInvestments = "Skipped"

    return {"invest_rewards": rewards,
            "invest_getInvestments": getInvestments}


def metric():
    add = "Skipped"

    return {"metric_add": add}


def oauth2():
    token = "Skipped"

    return {"oauth2_token": token}


def prismPro():
    activate = "Skipped"
    # activate = {"action":"activate",
    #             "device":"",
    #             "EAPCode":""}

    deactivate = "Skipped"

    getStatus = "Skipped"

    setCustomFields = "Skipped"

    setThresholds = "Skipped"

    return {"prismPro_activate": activate,
            "prismPro_deactivate": deactivate,
            "prismPro_getStatus": getStatus,
            "prismPro_setCustomFields": setCustomFields,
            "prismPro_setThresholds": setThresholds}

def role():
    importS3 = "Skipped"

    return {"role_importS3": importS3}


def share():
    read = "Skipped"

    add = "Skipped"

    return {"share_read": read,
            "share_add": add}


def subscription():
    add = "Skipped"

    read = "Skipped"

    update = "Skipped"

    cancel = "Skipped"

    return {"subscription_add": add,
            "subscription_read": read,
            "subscription_update": update,
            "subscription_cancel": cancel}


def support():
    importS3 = "Skipped"

    return {"support_importS3": importS3}


def voucher():
    importS3 = "Skipped"

    return {"voucher_importS3": importS3}


def zapier():
    triggers = {"action": "trigger",
                "id":"xy:ibeacon:08885dd0-111b-11e4-9191-0800200c9a66"
                     ".9253.58884",
                "type":"single_press"}

    return {"zapier_triggers": triggers}
