__author__ = 'Andrew'
import json , os
from collections import namedtuple
class Predix:
    def __init__(self):

        settings = self.load_predix_settings()
        import websocket, base64, requests
        from datetime import datetime
        self.ingest_wss = settings.ingest_wss
        self.ingestZone = settings.ingest_zone
        self.uaa_client = settings.uaa_client
        self.uaa_password = settings.uaa_password
        self.uaa_uri = settings.uaa_uri
        self.preauthorization_headers={'Authorization':'Basic %s' %(base64.b64encode('%s:%s'%(settings.uaa_client, settings.uaa_password)))}

        payload = {'client_id':settings.uaa_client,'response_type':'token','grant_type':'client_credentials'}
        response = requests.post('%s/oauth/token'%(settings.uaa_uri),data=payload,headers=self.preauthorization_headers)
        # print response.content
        self.response = response.json()
        self.token = response['access_token']



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
    #ok we have headers
    data = {""}
    return

def predix_co2_empty():
    return

def predix_omt():
    pass