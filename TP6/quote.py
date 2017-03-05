from order import Order

class Quote:
    def __init__(self):
        self.id = ""
        self.customer = ""
        self.amount = ""

    def parserQuoteFile(self, path):
        with open(path) as tfile:
            self.id = tfile.readline().rstrip()
            self.customer = tfile.readline().rstrip()
            self.amount = tfile.readline().rstrip()

    def parserQuoteJson(self, json_quote):
        self.id = json_quote["id"]
        self.customer = json_quote["customer"]
        self.amount = json_quote["amount"]

    def validateQuote(self, date):
        order = Order()
        order.id = self.id
        order.customer = self.customer
        order.amount = self.amount
        order.date = date
        return order

    def exportJSON(self):
        json = {}
        json["id"] = self.id
        json["customer"] = self.customer
        json["amount"] = self.amount
        return json
