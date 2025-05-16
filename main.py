import requests


# defining a user input interface function that will take inputs from the user.

def user_input():
    print(":CURRENCY CONVERTER:\n\n-you need to type the currect currency code to get the results\n(for example: rupee is INR and dollar is USD etc)\n")

    #getting user input.

    from_currency = input('Enter the currency you want to convert from: ')
    to_currency = input('Enter the currency you want to convert to: ')
    amount = float(input('Enter ammount: '))

    print(f"===>{convert_currency(amount, from_currency, to_currency)}")


# getting the currency rates from the api

def get_exchange_rate(from_currency, to_currency):
    api_key = 'd1b28fa9e234625e8d82f5cd'
    url = f"https://v6.exchangerate-api.com/v6/d1b28fa9e234625e8d82f5cd/latest/{from_currency}"

    responce = requests.get(url)
    data = responce.json()

    if responce.status_code != 200 or data['result'] != 'success':
        return None

    return data['conversion_rates'].get(to_currency, None)



# defining a function which will perform the conversion.

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return "Currency cannot be converted. (data not available on that currency)"
    converted_amount = amount * rate
    return converted_amount


user_input()






