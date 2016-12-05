import asyncio
import aiohttp
import json

class YoutrackAPI():
	BASE_URL = "http://track.codephobos.com/youtrack";
	ENDPOINT_LOGIN = "/rest/user/login"
	
	async def auth(self, login, password):
		
		url = self.BASE_URL + self.ENDPOINT_LOGIN
		
		data = {
			"login": login,
			"password": password
		}
		
		print("POST", url, data)
		
		with aiohttp.ClientSession() as session:
			response = await session.post(url, data=data)
			return response
		