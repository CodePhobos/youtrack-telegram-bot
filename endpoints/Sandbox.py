from aiohttp import web

class SandboxEndpoint(web.View):
	
	async def get(self):  
		return web.json_response({})