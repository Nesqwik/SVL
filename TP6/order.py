class Order:
    def __init__(self):
        self.id = ""
        self.customer = ""
        self.amount = ""
        self.date = ""

    def parserOrderFile(self, path):
        with open(path) as tfile:
            self.id = tfile.readline().rstrip()
            self.customer = tfile.readline().rstrip()
            self.amount = tfile.readline().rstrip()
            self.date = tfile.readline().rstrip()

    def parserOrderJson(self, json_order):
        self.id = json_order["id"]
        self.customer = json_order["customer"]
        self.amount = json_order["amount"]
        self.date = json_order["date"]

    def exportJSON(self):
        json = {}
        json["id"] = self.id
        json["customer"] = self.customer
        json["amount"] = self.amount
        json["date"] = self.date
        return json
