import asyncio
import aiohttp
import json
from config import TELEGRAM_BOT_TOKEN

class TelegramRequest():
	BASE_URL = "https://api.telegram.org/bot";
	
	async def sendMessage(self, chat_id, text):
		
		url = self.BASE_URL + TELEGRAM_BOT_TOKEN + "/sendMessage"
		data = {
			"chat_id": chat_id,
			"text": text
		}
		print("POST", url, data)
		
		with aiohttp.ClientSession() as session:
			response = await session.post(url, data=data)
			return await response.json()
		