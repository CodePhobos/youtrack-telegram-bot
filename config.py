from os.path import isfile
from envparse import env

if isfile('.env'):
    env.read_envfile('.env')
    
SERVER_HOST = env.str('HOST')
SERVER_PORT = env.int('PORT')

PG_USER = env.str('PG_USER')
PG_HOST = env.str('PG_HOST')
PG_PASSWORD =  env.str('PG_PASSWORD') 
PG_DATABASE = env.str('PG_DATABASE') 
PG_PORT = env.int('PG_PORT')

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')