from django.core.management.base import BaseCommand, CommandError
import os
# from polls.models import Question as Poll
__author__ = 'andrewsmiley'
from collections import namedtuple
import json, time
from datetime import datetime
from keg_api.models import Pour

from keg_api.grovepi import *

# "uaa_uri": "https://58c031e5-475a-436f-9205-3893c393a6a1.predix-uaa.run.aws-usw02-pr.ice.predix.io",
# "uaa_client": "gecloud",
# "uaa_password":"gecloud",
# "ingest_wss": "wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages",
# "ingest_zone":"51281459-3c09-4980-b9e8-32e376bca821",
# "query_uri":"https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    #basically load the settings as a bigass NamedTuple
    #just some shit to get settings
    def load_predix_settings(self):
        try:
            settings_json = json.loads(open("predix_settings.json", 'r').read())
        except:
            self.stdout.write("it worked! %s"%(os.getcwd()), ending='')
        PredixSettings = namedtuple("PredixSettings", [k for k in settings_json.keys()])
        return PredixSettings(**settings_json) #DOUBLE SPLAT!!


    def load_sensor_settings(self):
        try:
            settings_json = json.loads(open("sensor_settings.json", 'r').read())
        except:
            self.stdout.write("it worked! %s"%(os.getcwd()), ending='')
        SensorSettings= namedtuple("SensorSettings", [k for k in settings_json.keys()])
        return SensorSettings(**settings_json) #DOUBLE SPLAT!!

    def add_arguments(self, parser):
        pass
        # parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        settings = self.load_predix_settings()
        import websocket, base64, requests
        # from datetime import datetime
        # ingestURL = 'wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
        # ingestZone = '5423f397-d4eb-499e-ac6b-373b891de2b2'

        # headers={'Authorization':'Basic %s' %(base64.b64encode('%s:%s'%(settings.uaa_client, settings.uaa_password)))}
        #
        # payload = {'client_id':settings.uaa_client,'response_type':'token','grant_type':'client_credentials'}
        # response = requests.post('%s/oauth/token'%(settings.uaa_uri),data=payload,headers=headers)
        # print response.content
        # response = response.json()
        # token = response['access_token']

        # print ('starting websocket stuff')

        # myHeader = {'Authorization': 'Bearer %s' % token, 'Predix-Zone-id': "%s" % settings.ingest_zone, 'Content-Type':'application/json'}
        import urllib
        while True:

            timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
            data_points = self.create_data_entries()
            # https://iot-hydrator-timeseries-service.run.aws-usw02-pr.ice.predix.io/
            for dp in data_points:
                url = "%sservices/iothydrator/add_datapoint/%s/%s/%s/%s/%s/"%\
                      ("https://iot-hydrator-timeseries-service.run.aws-usw02-pr.ice.predix.io/", int(dp['datapoints'][0][0]), int(dp['datapoints'][0][1]), int(dp['datapoints'][0][1]), dp['name'], urllib.quote(json.dumps(dp['attributes']), safe=''))
                # url = urllib.quote(url, safe='')
                # os.system("echo $HTTP_PROXY")
                r=requests.get(url)
                print r.status_code

                # /services/iothydrator/add_datapoint/{timestamp}/{measure}/{quality}/{name}/{attributes}
                # r = requests.get("https://iot-hydrator-timeseries-service.run.aws-usw02-pr.ice.predix.io/")
            # new_data = {"messageId": "mid%s"%str(timestamp), 'body':data_points}
            # print json.dumps(new_data)
            print "taking a little snooze"
            time.sleep(60*15) #15 minute snooze
            # ws = websocket.WebSocket()
            # ws.connect(settings.ingest_wss, header=myHeader)

            # data_points = self.create_data_entries()
            #
            # print ("sending data %s\n at time %s\n to %s" %(new_data, timestamp, settings.ingest_zone))
            # ws.send(json.dumps(new_data))
            # print ws.recv()
            # time.sleep(60*15) #15 minute snooze
        #
            # ws.close()

        # self.stdout.write("it worked! %s"%(os.getcwd()), ending='')


    def create_data_entries(self):
        body = []
        #could this be a lambda???
        [body.append(x) for x in self.fetch_temp_data()]
        [body.append(x) for x in self.fetch_pour_history()]
        body.append(self.fetch_sound_data())
        return body


    def fetch_temp_data(self):
        settings = self.load_sensor_settings()
        sensor= 0

        for entry in settings.dht_sensors:
            datapoints = []
            datapoint = {"name":"dht", "attributes":{"sensor":sensor}}
            timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
            try:
                timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
                #lol it's automatic non-pi testing
                [ temp,hum ] = dht(entry.port,entry.type)
                t = [timestamp,int(float(temp * 9/5+32)), 3]
                h = [timestamp, int(hum), 3]
                datapoint['datapoints']=[t,h]
            except:
                #1 is uncertain quality
                datapoint['datapoints']=[[timestamp,0,1],[timestamp, 0,1]]
            datapoints.append(datapoint)

        # print "Fetched temperator data %s" %datapoints
        return datapoints
    #really all i want here is the volume of the pour
    def fetch_pour_history(self):
        datapoints = []

        for pour in Pour.objects.all():
            # timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
            datapoint = {"name":"pour", "datapoints":[], "attributes":{"user":pour.user.sso, "status":pour.status.description}}
            datapoint['datapoints'].append([int(float(pour.date)), pour.volume, 3])
            datapoints.append(datapoint)
            pour.predix_status=True
            pour.save()
        return datapoints

    def fetch_sound_data(self):
        settings = self.load_sensor_settings()
        sound_sensor = settings.ss_port #get the data via analog port
        datapoint = {"name":"dB", "attributes":{}, "datapoints":[]}
        timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
        #this guy is coming as dB
        try:
            pinMode(sound_sensor,"INPUT")
            db = int(analogRead(sound_sensor))
            datapoint['datapoints'].append([timestamp, db, 3])
        except:
            datapoint['datapoints'].append([timestamp, 0, 1])

        return datapoint




"""
{
  "messageId": "1453338376222",
  "body": [
    {
      "name": "Compressor-2015:CompressionRatio",
      "datapoints": [
        [
          1453338376222,
          10,
          3
        ],
        [
          1453338377222,
          10,
          1
        ]
      ],
      "attributes": {
        "host": "server1",
        "customer": "Acme"
      }
    }
  ]
}
"""

