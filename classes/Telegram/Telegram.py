import json

from .TelegramUpdate import TelegramUpdate
from .TelegramRequest import TelegramRequest

class TelegramWrapper():
	
	def dispatchUpdate(update):
		
		handle = TelegramUpdate()
		handle.dispatch(update)
		
		return handle;
		
	async def sendMessage(chat_id, text):
		request = TelegramRequest()
		return await request.sendMessage(chat_id, text)
	
	def log(data): 
		print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
		

		