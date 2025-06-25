# Filename:  currency_converter.py
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not found"
    
    rate = exchange_rates[to_currency] / exchange_rates[from_currency]
    converted_amount = amount * rate
    return converted_amount

exchange_rates = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 139.0}

amount = 100
from_currency = "USD"
to_currency = "EUR"

converted = convert_currency(amount, from_currency, to_currency, exchange_rates)
print(f"{amount} {from_currency} is equal to {converted:.2f} {to_currency}")