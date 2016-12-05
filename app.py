import asyncio
from aiohttp import web
from config import *

from endpoints import SandboxEndpoint, TelegramEndpoint

# init application	
app = web.Application()
app.router.add_route('*', '/initial', SandboxEndpoint)
app.router.add_route('*', '/hooks/telegram', TelegramEndpoint)

# start servering
handler = app.make_handler()
loop = asyncio.get_event_loop()
server = loop.create_server(handler, SERVER_HOST, SERVER_PORT)
generator = loop.run_until_complete(server)
print("start servering on", SERVER_HOST, SERVER_PORT)

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("serving off...")
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    generator.close()
    loop.run_until_complete(generator.wait_closed())
    loop.run_until_complete(app.finish())
    
