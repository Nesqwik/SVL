class Customer:

    def __init__(self):
        self.id = ""
        self.name = ""
        self.address = ""
        self.city = ""
        self.number = ""

    def parserCustomerFile(self, path, id) :
        self.id = id
        with open(path) as tfile:
            self.name = tfile.readline()
            self.address = tfile.readline()
            self.city = tfile.readline()
            self.number = tfile.readline()

    def parserCustomerJson(self, json_customer):
        self.id = json_customer["id"]
        self.name = json_customer["name"]
        self.address = json_customer["address"]
        self.city = json_customer["city"]
        self.number = json_customer["number"]

    def exportJSON(self):
        json = {}
        json["id"] = self.id
        json["name"] = self.name
        json["address"] = self.address
        json["city"] = self.city
        json["number"] = self.number
        return json
