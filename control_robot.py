import aiohttp
import asyncio

# URL = "http://10.32.11.160/"
# URL = "http://192.168.1.34/"
URL = "http://192.168.222.115/"

def robot_happy():
    async def robot():
        async with aiohttp.ClientSession() as session:
            async with session.get(URL+"happy") as response:
                pass      
            async with session.get(URL+"neutral") as response2:
                pass
    loop = asyncio.get_event_loop()
    loop.run_until_complete(robot())

def robot_listen():
    async def robot():
        async with aiohttp.ClientSession() as session:
            async with session.get(URL+"listening") as response:
                pass      
            async with session.get(URL+"neutral") as response2:
                pass
    loop = asyncio.get_event_loop()
    loop.run_until_complete(robot())

def robot_speak():
    async def robot():
        async with aiohttp.ClientSession() as session:
            async with session.get(URL+"speaking") as response:
                pass      
            async with session.get(URL+"neutral") as response2:
                pass
    loop = asyncio.get_event_loop()
    loop.run_until_complete(robot())