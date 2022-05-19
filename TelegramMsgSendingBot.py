import requests

url = 'https://api.telegram.org/bot5236570373:AAGVnduKfwos1o6wh5tGaffECwh1L4S8_HU/sendMessage?chat_id=-616995541&text="This is a test message"'

for number in range(10):
    url = 'https://api.telegram.org/bot5236570373:AAGVnduKfwos1o6wh5tGaffECwh1L4S8_HU/sendMessage?chat_id=-616995541&text="{}"'.format(number)
    res = requests.get(url)
    data = res.json()
    print(data)