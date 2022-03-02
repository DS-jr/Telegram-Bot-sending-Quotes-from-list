import requests
import time

my_quotes = [
    "(Ray Dalio) Go to your pain rather than avoid it.",
    "(Paul Graham)  Working hard means constantly aiming towards the core important center of the problem / task: usually the most difficult / uncomfortable part of it.", 
    "(Stephen Hawking)  However difficult life may seem, there is always smth you can do and succeed at.", 
    "(Lee Kuan Yew, LKY)  Determination creates a huge internal drive & focus. People feel if you are determined or not.", 
    "(Goethe)  “Treat people as if they were what they ought to be and you help them to become what they are capable of being.”, 
    "(Ray Dalio)  Do NOT worry about looking good - worry instead about achieving your goals.", 
    "(Jay Adelson)  A simple test about integrity: if you make a decision, would you be comfortable if everyone knows you made it? Can you make this decision w/ full transparency & feel you’ll NOT have to hide anything?"
]

for q_1 in my_quotes:
    url_1 = "https://api.telegram.org/botBOT_TOKEN/sendMessage?chat_id=CHAT_ID&text='{}'".format(q_1)  # Substitute BOT_TOKEN with your Bot's token. Substitute CHAT_ID with your group chat ID.
    requests.get(url_1)
    time.sleep(10) # Period of time in seconds between quote sending
