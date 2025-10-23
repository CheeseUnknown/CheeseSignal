import asyncio

import __init__
from CheeseSignal import Signal

signal = Signal()

async def handle_1():
    print('Handler 1 executed')
signal.connect(handle_1)

@signal.connect()
async def handle_2():
    print('Handler 2 executed')

if __name__ == '__main__':
    asyncio.run(signal.async_send())
