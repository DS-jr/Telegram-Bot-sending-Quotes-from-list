import requests
import time

my_quotes = [

]

for q_1 in my_quotes:
    url_1 = "https://api.telegram.org/botBOT_TOKEN/sendMessage?chat_id=CHAT_ID&text='{}'".format(q_1)  # Substitute BOT_TOKEN with your Bot's token. Substitute CHAT_ID with your group chat ID.
    requests.get(url_1)
    time.sleep(10) # Period of time in seconds between quote sending
