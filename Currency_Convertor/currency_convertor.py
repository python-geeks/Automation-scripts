# Currency Converter

# Import necessary modules
import requests


class Currency_Converter:
    rate = {}

    def __init__(self, url):
        data = requests.get(url).json()
        # Extracting rate from json
        self.rate = data["rates"]

    # Conversion
    def convert(self, from_country, to_country, amount):
        initial = amount
        if from_country != 'EUR':
            amount = amount / self.rates[from_country]

        # Precision to 2 decimal places
        amount = round(amount * self.rate[to_country], 2)
        print(f'{initial} {from_country} = {amount} {to_country}')


# Driver Code
if __name__ == "__main__":
    # Replace API_KEY with your own API key from fixer.io
    url = 'http://data.fixer.io/api/latest?access_key=API_KEY'
    cc = Currency_Converter(url)
    from_country = input("From: ")
    to_country = input("To: ")
    amount = int(input("Amount: "))

    cc.convert(from_country, to_country, amount)
