from urllib.parse import urlparse
from urllib.parse import parse_qs

def get_stock_symbol(url):
    parsed_url = urlparse(url)
    symbol_value = parse_qs(parsed_url.query)['symbol'][0]

    return symbol_value