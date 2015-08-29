from urllib.request import urlopen
import os
import json

KEY_ENV = "STEAM_API_KEY"
API_BASE = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/"

class Dota2API():
    def __init__(self, key=None, uid=None):
        if os.getenv(KEY_ENV):
            self.key = os.getenv(KEY_ENV)
        else:
            self.key = key

    def printkey(self):
        print(self.key)

    def mk_request(self, **kwargs):
        reqstr = "{url}?key={apikey}".format(url=API_BASE, apikey=self.key)

        if kwargs is not None:
            for key, value in kwargs.items():
                reqstr += "&{k}={v}".format(k=key, v=value)

        print(reqstr)
        try:
            res = urlopen(reqstr).read().decode("utf-8")
        except HTTPError as he:
            res = he.errno
        #return json.loads(res)
        return res

