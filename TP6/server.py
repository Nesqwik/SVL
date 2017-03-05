"""
SVL 2016-2017 M. Nebut
TP Selenium
Application de suivi de devis, codée avec les pieds.
A refactorer.
created : 2017-02-16 10:06:32 CET
"""

import os

import bottle
import sys
import json
from order import Order
from quote import Quote
from customer import Customer

########################################################################
# Application services
########################################################################

@bottle.route('/')
def index():
    return bottle.template(TPLA_INDEX)


@bottle.route('/quotes')
def quotes():
    quotes = list_quotes()
    return bottle.template(TPLA_QUOTES, quotes=quotes)


@bottle.route('/quote/<reference>')
def quote(reference):
    (customer, quote) = read_quote(reference)
    return bottle.template(TPLA_QUOTE, customer=customer.name, amount=quote.amount, reference=quote.id)


@bottle.route('/valid/<reference>', method='POST')
def valid(reference):
    date = bottle.request.forms.get('date')
    valid_quote(reference, date)
    bottle.redirect('/quotes')


@bottle.route('/orders')
def orders():
    orders = list_orders()
    return bottle.template(TPLA_ORDERS, orders=orders)


@bottle.route('/order/<reference>')
def order(reference):
    (customer, order) = read_order(reference)
    return bottle.template(TPLA_ORDER, reference=reference, amount=order.amount, customer=customer.name, date=order.date)


########################################################################
# Application functions
########################################################################

def list_quotes():
    return sorted(QUOTES.keys())


def read_quote(reference):
    quote = QUOTES[reference]
    customer = read_customer(quote.customer)
    return (customer, quote)


def write_data():
    data = {}
    data["customers"] = []
    for customer in CUSTOMERS.values():
        data["customers"].append(customer.exportJSON())
    data["orders"] = []
    for order in ORDERS.values():
        data["orders"].append(order.exportJSON())
    data["quotes"] = []
    for quote in QUOTES.values():
        data["quotes"].append(quote.exportJSON())
    with open(DATA_PATH, 'w') as tfile:
        json.dump(data,tfile)


def valid_quote(reference, date):
    quote = QUOTES[reference]
    del QUOTES[reference]
    ORDERS[reference] = quote.validateQuote(date)
    write_data()

def list_orders():
    return sorted(ORDERS.keys())


def read_order(reference):
    order = ORDERS[reference]
    customer = read_customer(order.customer)
    return (customer, order)

def read_customer(id_customer):
    return CUSTOMERS[id_customer]


########################################################################
# Templates
########################################################################

TPLA_INDEX = '''
<p>Suivi des devis</p>

<ul>
<li><a href="/quotes">Devis en attente de commandes</a></li>
<li><a href="/orders">Commandes validées</a></li>
</ul>
'''


TPLA_QUOTES = '''
<p>Devis</p>
<table>
  % for quote in quotes:
  <tr>
    <td><a href="/quote/{{ quote }}">{{ quote }}</a></td>
  </tr>
  % end
</table>

<a href="/">Accueil</a>
'''

TPLA_QUOTE = '''
<p>Devis {{  reference }}</p>

<p> {{ customer }}</p>

<p>Montant: {{ amount }}</p>

<form action="/valid/{{ reference }}" method="post">
  Date validation : <input name="date" type="text" />
  <input value="Valider" type="submit" />
</form>

<p>
<a href="/quotes">Liste devis</a>
</p>
'''


TPLA_ORDERS = '''
<p>Commandes</p>
<table>
  % for order in orders:
  <tr>
    <td><a href="/order/{{ order }}">{{ order }}</a></td>
  </tr>
  % end
</table>

<a href="/">Accueil</a>
'''

TPLA_ORDER = '''
<p>Commande {{ reference }}</p>

<p> {{ customer }} </p>

<p>Montant: {{ amount }} </p>

<p>Validé le {{ date }} </p>

<p>
<a href="/orders">Liste commandes</a>
</p>
'''

########################################################################
# Start service
########################################################################


if __name__ == '__main__':
    if len(sys.argv) > 1:
        DATA_PATH = sys.argv[1]
    else:
        DATA_PATH = "data.json"
    with open(DATA_PATH) as tfile:
        data = json.load(tfile)
    CUSTOMERS = {}
    QUOTES = {}
    ORDERS = {}
    for json_customer in data["customers"]:
        customer = Customer()
        customer.parserCustomerJson(json_customer)
        CUSTOMERS[customer.id] = customer
    for json_order in data["orders"]:
        order = Order()
        order.parserOrderJson(json_order)
        ORDERS[order.id] = order
    for json_quote in data["quotes"]:
        quote = Quote()
        quote.parserQuoteJson(json_quote)
        QUOTES[quote.id] = quote
    bottle.run(host='localhost', port=8080, debug=True)

# eof
