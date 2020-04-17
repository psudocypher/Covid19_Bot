from bot import telegram_chatbot
from reply import make_reply

bot = telegram_chatbot("config.cfg")
update_id = None
botReply = make_reply()

while True:
	print("....")
	updates = bot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = item["message"]["text"]
			except:
				message = None
			from_ = item["message"]["from"]["id"]
			Reply = botReply.Reply(message)
			bot.send_message(Reply, from_)