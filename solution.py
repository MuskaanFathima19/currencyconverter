import requests
import json

def get_exchange_rates():
    """Fetches exchange rates from an API and returns them as a dictionary."""
    url = "https://api.exchangerate-api.com/v6/latest"  # Replace with your desired API URL
    response = requests.get(url)
    data = json.loads(response.text)
    return data['rates']

def convert_currency(amount, from_currency, to_currency, exchange_rates):
    """Converts the given amount from one currency to another."""
    try:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    except KeyError:
        print("Invalid currency code.")
        return None

def main():
    exchange_rates = get_exchange_rates()

    while True:
        print("Currency Converter")
        print("------------------")
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency code (e.g., USD, EUR, INR): ").upper()
        to_currency = input("Enter the target currency code (e.g., USD, EUR, INR): ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Conversion failed.")

        choice = input("Do you want to convert another amount? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()