import threading
import requests
import time

def get_bitcoin_price():
    while True:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        print(f"Aktualna cena Bitcoina: {price} USD")
        time.sleep(1)

def print_date_time():
    while True:
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)

thread1 = threading.Thread(target=get_bitcoin_price)
thread2 = threading.Thread(target=print_date_time)

thread1.start()
thread2.start()