import asyncio
import aiohttp
import time

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result

async def request(url):
    #url = 'http://www.baidu.com'
    print('Waiting for', url)
    result = await get(url)
    print('Get response from', url )
    return result 

url = 'http://www.baidu.com'
tasks = [asyncio.ensure_future(request(url)) for _ in range(2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)


for task_item in tasks:

    print ( 'my tastk ' ,  type( task_item.result() ) )