import config
import logging
from binance.client import Client
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from binance.error import ClientError

client = Client(config.API_KEY, config.API_SECRET)
futures_client = UMFutures(config.API_KEY, config.API_SECRET)

#tickers = client.get_all_tickers()
#for symbol in tickers:
#    print(symbol)

# Bitcoin
#symbolTicker = client.get_all_tickers()
#for symbol in symbolTicker:
#    print(symbolTicker)

# Bitcoin perpetual contract
futures_symbolTicker = futures_client.ticker_price("btcusdt")
print(futures_symbolTicker)


