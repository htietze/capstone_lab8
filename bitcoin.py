import requests

def main():
    bitcoins = get_bitcoin_amount()
    bitcoin_rate = get_current_BTC_rate()
    # if it successfully returned a bitcoin rate, then it'll convert and print, otherwise alerts the user to an issue.
    if bitcoin_rate:
        converted = convert_BTC_to_USD(bitcoins, bitcoin_rate)
        print(f'{bitcoins} bitcoin is equal to ${converted}, at a rate of {bitcoin_rate} dollars per bitcoin')
    else:
        print('Please try again later or check your network connection')

def get_bitcoin_amount():
    # loops for validation, so if they enter something that breaks the float requirement, it'll keep going
    # and only return once they do it right.
    while True:
        try:
            btc = float(input('Enter bitcoin amount for conversion: '))
            return btc
        except ValueError:
            print('Invalid amount entered, please try again.')

def get_current_BTC_rate():
    # trys to get the BTC rate from online, then return the USD rate from that json
    # If that fails due to the json response being different resulting in a key error, or there being no network connection
    # which causes requests to raise a connection error exception, then it'll return false and let the user know it couldn't get the rate.
    try:
        data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        USD_rate = data['bpi']['USD']['rate_float']
        return USD_rate
    except (KeyError, requests.exceptions.ConnectionError):
        print('Bitcoin exchange rate could not be retrieved')
        return False

def convert_BTC_to_USD(bitcoins, bitcoin_rate):
    return bitcoins * bitcoin_rate

if __name__ == '__main__':
    main()