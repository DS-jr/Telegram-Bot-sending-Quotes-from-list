# Telegram-Bot-sending-Quotes-from-list

Telegram Bot sending a quote from a fixed (predetermined) list to a group chat every 10 seconds<br>

<h2>Steps</h2>
<ul>
  <li>Intall <a href="https://telegram.org/">Telegram</a> (if you don't have it yet) & open it</li>
  <li>Register your new Bot with Telegram's official tool - <a href="https://telegram.me/BotFather">BotFather</a></li>
  <li>Follow <a href="https://telegram.me/BotFather">BotFather's</a> instructions, get a Token (keep it safe) to access Telegram API</li> 
  <li>Create a Telegram group chat & add your Bot as a group member</li>
  <li>Send <code>/my_id BOT_NAME</code> command as a message in your group chat to get group chat ID</li>
  <li>Open <code>https://api.telegram.org/botBOT_TOKEN/getUpdates</code> in a browser (in the link: substitute <code>BOT_TOKEN</code> with your Bot's Token)</li>
  <li>Copy your group chat ID from the JSON that was returned in the browser</li>
  <li>In <a href="https://github.com/DS-jr/Telegram-Bot-sending-Quotes-from-list/blob/main/bot4.py">bot4.py</a> file (in line 15): substitute <code>BOT_TOKEN</code> with your Bot's Token, substitute <code>CHAT_ID</code> with your group chat ID</li>
  <li>In Terminal: create a new directory & enter it</li>
  <li>Run these commands in Terminal:</li>
  <code>python3 -m venv env</code><br>
  <code>source env/bin/activate</code><br>
  <code>pip install requests</code><br>
  <li>Run your <a href="https://github.com/DS-jr/Telegram-Bot-sending-Quotes-from-list/blob/main/bot4.py">bot4.py</a> file (it can be done locally on your computer):</li>
  <code>python3 bot4.py</code><br>
  <li>Go to your group chat in Telegram. A new quote from your list should appear every 10 seconds</li>
</ul>
