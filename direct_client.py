import urllib2
import json
from pymongo import MongoClient

class Rest_Request(object):
    """docstring for Rest_Request"""

    def __init__(self,server):
        super(Rest_Request, self).__init__()
        self.server = server
        self.db = 0

    def DB_connect(self):
        if client:
            return True
        else:
            return False

    def Sensors_recense(self):
        path = self.server+"/sensors"
        req = urllib2.Request(path)
        opener = urllib2.build_opener()
        f = opener.open(req)
        sensors = f.read()
        return sensors

    def Read_Line(self,text):
        line = text.split('\n')
        return line

    def Request_data(self,id):
        path = self.server+"/sensors/"+str(id)+"/all_measures"
        req = urllib2.Request(path)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = json.loads(f.read())
        return data
        
client = Rest_Request("http://129.194.184.224:5001")     
#client = Rest_Request("http://129.194.184.124:5000")
sensors = client.Sensors_recense()

line = client.Read_Line(sensors)
#connect = client.DB_connect()
client_db = MongoClient()
db = client_db.smarthepia
for i in range(0,len(line)-1):
   num = line[i].split("=")
   data = client.Request_data(num[0])
   result = db.Sensors_data.insert_one(data)
   # Insertion des donnees dans la base de donnees
cursor = db.Sensors_data.find()
for document in cursor:
    print(document)
