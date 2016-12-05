from peewee import fn, Model, CharField, IntegerField, ForeignKeyField, DateTimeField, DoubleField, BigIntegerField, TextField
from models import *

class User(AbstractModel):
	STATE_NO_CREDENTIALS = "Unregistered"
	STATE_ASKED_FOR_LOGIN = "Asked for login"
	STATE_HAS_LOGIN = "Login passed"
	STATE_REGISTERED = "Registered"
	
	telegram_id = BigIntegerField(unique=True)
	name = CharField(null=True)
	youtrack_login = CharField(null=True)
	youtrack_password = CharField(null=True)
	state = CharField(default="Unregistered")
    
	def set_state(self, state):
	    self.state = state
	    self.save()
	    
	def get_or_register(telegram_id): 
		try:
			user = User.get(User.telegram_id == telegram_id)
		except User.DoesNotExist:
			return User.create(telegram_id=telegram_id);
		else: 
			return user