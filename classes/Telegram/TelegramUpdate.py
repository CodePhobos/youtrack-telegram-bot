		
class TelegramUpdate():
	chat_id = 0
	from_id = 0
	from_username = ""
	
	has_command = False
	command = ""
	commands = []
	
	is_text = True
	text = ""
	
	def dispatch(self, json):
		message = json.get('message')
		
		self.chat_id = message.get('chat').get('id')
		self.from_id = message.get('from').get('id')
		self.from_username = message.get('from').get('username')
		self.text = message.get('text')
		
		entities = message.get('entities')
		if(entities):
			for entity in entities:
				if(entity['type'] == "bot_command"):
					command = self.text[entity['offset']:entity['length']]
					self.command = command
					self.commands.append(command)
					self.has_command = True