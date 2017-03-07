__author__ = 'Andrew'
import json , os, requests, datetime
from collections import namedtuple
from models import Keg
class Predix:
    def __init__(self):

        settings = self.load_predix_settings()
        import websocket, base64, requests
        from datetime import datetime
        self.ingest_wss = settings.ingest_wss
        self.ingest_zone = settings.ingest_zone
        self.uaa_client = settings.uaa_client
        self.uaa_password = settings.uaa_password
        self.uaa_uri = settings.uaa_uri
        self.preauthorization_headers={'Authorization':'Basic %s' %(base64.b64encode('%s:%s'%(settings.uaa_client, settings.uaa_password)))}

        payload = {'client_id':settings.uaa_client,'response_type':'token','grant_type':'client_credentials'}
        response = requests.post('%s/oauth/token'%(settings.uaa_uri),data=payload,headers=self.preauthorization_headers)
        # print response.content
        self.response = response.json()
        self.token = self.response['access_token']



        self.authorization_headers= {'Authorization': 'Bearer %s' % self.token, 'Predix-Zone-id': "%s" % self.ingest_zone, 'Content-Type':'application/json'}

    #basically load the settings as a bigass NamedTuple
    #just some shit to get settings
    def load_predix_settings(self):
        try:
            settings_json = json.loads(open("predix_settings.json", 'r').read())
        except:
            self.stdout.write("Cannot open predix settings file", ending='')

        PredixSettings = namedtuple("PredixSettings", [k for k in settings_json.keys()])
        return PredixSettings(**settings_json) #DOUBLE SPLAT!!

def predix_keg_empty():
    predix = Predix()
    # from datetime import datetime
    # import tzlocal  # $ pip install tzlocal

    # unix_timestamp = float("1284101485")
    # local_timezone = tzlocal.get_localzone() # get pytz timezone
    # local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    #ok we have headers
    #curl 'https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints' -X post -H 'predix-zone-id: bc1f83f1-c489-4426-9341-f6bee917cb44' -H 'authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJhZmUxNTQwNTJlMjA0NGZmODY2ZTkxOWQwMTVjMWY2OSIsInN1YiI6ImtlZyIsInNjb3BlIjpbInRpbWVzZXJpZXMuem9uZXMuNjRhMmE3NjItYTMwNS00YTk1LTlkNWQtMDUyZThiYjM3Mjc2LnF1ZXJ5IiwidWFhLnJlc291cmNlIiwib3BlbmlkIiwidWFhLm5vbmUiLCJ0aW1lc2VyaWVzLnpvbmVzLjY0YTJhNzYyLWEzMDUtNGE5NS05ZDVkLTA1MmU4YmIzNzI3Ni5pbmdlc3QiLCJ0aW1lc2VyaWVzLnpvbmVzLjY0YTJhNzYyLWEzMDUtNGE5NS05ZDVkLTA1MmU4YmIzNzI3Ni51c2VyIiwidGltZXNlcmllcy56b25lcy5iYzFmODNmMS1jNDg5LTQ0MjYtOTM0MS1mNmJlZTkxN2NiNDQuaW5nZXN0IiwidGltZXNlcmllcy56b25lcy5iYzFmODNmMS1jNDg5LTQ0MjYtOTM0MS1mNmJlZTkxN2NiNDQudXNlciIsInRpbWVzZXJpZXMuem9uZXMuYmMxZjgzZjEtYzQ4OS00NDI2LTkzNDEtZjZiZWU5MTdjYjQ0LnF1ZXJ5Il0sImNsaWVudF9pZCI6ImtlZyIsImNpZCI6ImtlZyIsImF6cCI6ImtlZyIsImdyYW50X3R5cGUiOiJjbGllbnRfY3JlZGVudGlhbHMiLCJyZXZfc2lnIjoiMWY0MDI5MjQiLCJpYXQiOjE0ODg4NDY2NTcsImV4cCI6MTQ4ODg4OTg1NywiaXNzIjoiaHR0cHM6Ly9hZDhmM2IzYy1mNDViLTQ4YmYtOWMzNi00Njc4YWMyZWRlMzcucHJlZGl4LXVhYS5ydW4uYXdzLXVzdzAyLXByLmljZS5wcmVkaXguaW8vb2F1dGgvdG9rZW4iLCJ6aWQiOiJhZDhmM2IzYy1mNDViLTQ4YmYtOWMzNi00Njc4YWMyZWRlMzciLCJhdWQiOlsidWFhIiwidGltZXNlcmllcy56b25lcy42NGEyYTc2Mi1hMzA1LTRhOTUtOWQ1ZC0wNTJlOGJiMzcyNzYiLCJvcGVuaWQiLCJrZWciLCJ0aW1lc2VyaWVzLnpvbmVzLmJjMWY4M2YxLWM0ODktNDQyNi05MzQxLWY2YmVlOTE3Y2I0NCJdfQ.w7LzOkp7huTXUkx-EJ7zgSw329ytkpmSs24FsQSZKqjazTv2hZVO0EUotuPfSOCfIH0O8W0tIBy_UWPm58bzfgaO1s7PMhCzdlhYm4XcWsF_r-LMzrkO1az4jR2TCk-wxHnUHG_ew-4NJD5aF01La9YPPifgqQrAlZsAUznxsESh3mUG4Rt7GhWu5qgD5rJF0ukFYv_CGyQoWEU0GjKKeDSuJPm-FufCuf2oJgQaNyn64-dr0Sq3HcTmRij4xlUgMzSqJuCSCYn5NJeGg66Na4jMZBF6KHQ5S6j53uRNZNqDkz0-XvTqc0sRhW3fbeEw9FFp7nzyXUAJzl214Vqeug' --data-binary '{"start":"1y-ago","tags":[{"name":"pour","order":"desc","groups":[{"name":"attribute","attributes":["keg"]}]}]}'
    data = {"start":"1y-ago","tags":[{"name":"pour","order":"desc","groups":[{"name":"attribute","attributes":["keg"]}]}]}
    # data = {""}
    r = requests.post("https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints", headers=predix.authorization_headers, json=data)
    if r.status_code == 200:
        total_volume=0
        for collection in json.loads(r.text)['tags'][0]['results']:
            if int(collection['groups'][0]['group']['keg']) != Keg.objects.last().id:
                continue
            else:

                for dp in collection['values']:
                    total_volume = total_volume+dp[1]

                print "Total Volume Consumed From Current Keg: %s oz" %(total_volume)
    current_keg = Keg.objects.last()
    keg_install_time = datetime.datetime.utcfromtimestamp(float(current_keg.date))
    current_time= datetime.datetime.now()
    # print "hours since install %s" %((current_time-keg_install_time).total_seconds()/60/60)
    ounces_per_hour = float((current_time-keg_install_time).total_seconds()/60.0/60.0)/total_volume
    total_keg_ounces = float(current_keg.volume *128.0)
    ounces_remaining = float(total_keg_ounces-total_volume)
    return int(ounces_remaining/ounces_per_hour)/24


def predix_co2_empty():
    return

def predix_omt():
    pass