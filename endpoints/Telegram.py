from aiohttp import web
from classes import TelegramWrapper, YoutrackAPI
from models import User 

class TelegramEndpoint(web.View):
	TG_COMMAND_AUTH = "/auth"
	TG_COMMAND_START = "/start"
	
	MSG_WELCOME = "Привет! Это бот-помощник для YouTrack."
	MSG_ASK_FOR_LOGIN = "👌 Для начала напиши свой логин!"
	MSG_ASK_FOR_PASSWORD = "👍 Теперь напиши свой пароль:"
	
	async def post(self):
		data = await self.request.json()
		
		update = TelegramWrapper.dispatchUpdate(data)
		user = User.get_or_register(update.from_id)
		
		# Check credentials
		if(user.state == User.STATE_HAS_LOGIN):
			user.youtrack_password = update.text
			api = YoutrackAPI()
			response = await api.auth(login = user.youtrack_login, password = user.youtrack_password);
			await TelegramWrapper.sendMessage(update.chat_id, await response.text())
			user.set_state(User.STATE_NO_CREDENTIALS)
			
		# Ask for password 
		if(user.state == User.STATE_ASKED_FOR_LOGIN):
			user.youtrack_login = update.text
			user.set_state(User.STATE_HAS_LOGIN)
			await TelegramWrapper.sendMessage(update.chat_id, self.MSG_ASK_FOR_PASSWORD)
		
		# Ask for login
		if(user.state == User.STATE_NO_CREDENTIALS):
			user.set_state(User.STATE_ASKED_FOR_LOGIN)
			await TelegramWrapper.sendMessage(update.chat_id, self.MSG_WELCOME)
			await TelegramWrapper.sendMessage(update.chat_id, self.MSG_ASK_FOR_LOGIN)
		
		if(update.has_command):
			if(update.command == self.TG_COMMAND_START):
				1;
			else:
				print(update.command)
		
		else:
			print(update.text)
			
		return web.json_response({})