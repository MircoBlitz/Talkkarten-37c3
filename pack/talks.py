import json, requests

class Talks:
    # Initializer / Instance Attributes
    def __init__(self):
        self.data = {}
        self.byId = {}
        self.fahrplan = "https://fahrplan.events.ccc.de/congress/2023/fahrplan/schedule.json"

        response = requests.get(url)
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
                        self.byId[event["id"]] = event
                        
    def getNumOfTalks(self):
        return len(self.byId)
       



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
