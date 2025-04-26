# defining a user input interface function that will take inputs from the user.

def user_input():
    print(":CURRENCY CONVERTER:\nAvailable currencies: INR, USD, EUR")

    #getting user input.

    from_currency = input('Enter the currency you want to convert from: ')
    to_currency = input('Enter the currency you want to convert to: ')
    amount = float(input('Enter ammount: '))

    print(f"===>{convert_currency(amount, from_currency, to_currency)}")


#defining a function which will check and return the available currency which can be converted.

def get_exchange_rate(from_currency, to_currency):
    rates = {
        'USD':{'INR':83.3,'EUR':0.92},
        'INR':{'USD':0.012,'EUR':0.011},
        'EUR':{'USD':1.09,'INR':90.5}
    }
    return rates.get(from_currency, {}).get(to_currency, None)


# defining a function which will perform the conversion.

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        return "Currency cannot be converted. (data not available on that currency)"
    converted_amount = amount * rate
    return converted_amount


user_input()






