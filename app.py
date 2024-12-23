import json, config
from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
#set FLASK_APP=app.py
#flask run

client = Client(config.API_KEY, config.API_SECRET)

def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order_result = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order_result


@app.route('/')
def welcome():
    return 'index.html'

@app.route('/webhook', methods=['POST'])
def webhook():

    print('Account balance:')
    print(client.get_asset_balance(asset='USDT'))

    # print(request.data)
    data = json.loads(request.data)

    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }

    ticker = data['ticker']
    #print(f"The ticker is {ticker}")
    side = data['strategy']['order_action'].upper()
    quantity = data['strategy']['order_contracts']
    order_response = order(side, quantity, ticker)

    if order_response:
        return {
            "code": "success",
            "message": "order executed"
        }
    else:
        print("order failed")

        return {
            "code": "error",
            "message": "order failed"
        }