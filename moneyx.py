import requests

API_KEY = "aee2d574b38f46d39a3134939bedc8c8"
BASE_URL = "https://open.er-api.com/v6/latest/EUR"

def convert_currency(amount, from_currency, to_currency):
    response = requests.get(BASE_URL, params={"apikey": API_KEY})
    data = response.json()

    if 'rates' in data and to_currency in data['rates'] and from_currency in data['rates']:
        rate = data['rates'][to_currency] / data['rates'][from_currency]
        return amount * rate
    else:
        raise ValueError("Не вдалося отримати курс валют.")



print("Enter your amount, start currency and final currency:")
print("Examle> 34.7, EUR, USD")

user_input = input("input> ")
user_input = user_input.split(", ")

print(user_input)

start_currency = user_input[1].upper()
final_currency = user_input[2].upper()
amount = float(user_input[0])

converted_amount = convert_currency(amount, start_currency, final_currency)

print(f"{amount} {start_currency} is {converted_amount} {final_currency}")