import requests
import datetime

class Talks:
    # Initializer / Instance Attributes
    def __init__(self):
        self.data = {}
        self.byId = {}
        self.url = "https://fahrplan.events.ccc.de/congress/2023/fahrplan/schedule.json"

        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
            self.getTalks()
        else:
            print("Could not retrive Fahrplan")
            exit(1)
        

    def getTalks(self):
        for day in self.data["schedule"]["conference"]["days"]:
            for room in day["rooms"]:
                if room == "Saal 1" or room == "Saal Grace" or room == "Saal Zuse":
                    for event in day["rooms"][room]:
                        if(event["id"] != 12338):
                            self.byId[event["id"]] = event
                        
    def getNumOfTalks(self):
        return len(self.byId)
    
    def printTalks(self):
        for key in self.byId:
            dt = datetime.datetime.strptime(self.byId[key]["date"], "%Y-%m-%dT%H:%M:%S%z")
            day = dt.strftime("%d")
            if day == "27":
              textday = "DAY1"
            if day == "28":
              textday = "DAY2"
            if day == "29":
              textday = "DAY3" 
            if day == "30":
              textday = "DAY4"
            print("Tag:",textday, "Saal:", self.byId[key]["room"], "ID:", key," : ",self.byId[key]["title"])
       



    # def search_data(self, what, value):
    #     out = {}
    #     for key in self.data:
    #         if what == "room":
    #             if self.data[key]["block"]["room"] == str(value):
    #                 out.update({key: self.data[key]})
    #         elif what == "day":
    #             if self.data[key]["day"] == str(value):
    #                 out.update({key: self.data[key]})
    #         elif isinstance(what, list):
    #             if (self.data[key]["block"]["room"] == str(value[0])) and (self.data[key]["day"] == str(value[1])):
    #                 out.update({key: self.data[key]})
    #     return out
