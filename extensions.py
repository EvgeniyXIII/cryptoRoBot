import requests
import json
from config import keys

class APIException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amout: str):
        if quote == base:
            raise APIException(f"Невозможно конвертировать одинаковые валюты {base}.")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Невозможно обработать валюту {quote}.")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Невозможно обработать валюту {base}.")
        try:
            amout = float(amout)
        except KeyError:
            raise APIException(f"Не удалось обработать количество {amout}.")
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = float(json.loads(r.content)[keys[base]])
        return round(total_base * amout, 2)
