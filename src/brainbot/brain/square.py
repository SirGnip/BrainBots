import asyncio


async def think(me):
    step = 25
    delay = 0.35
    while True:
        me.center_x += step
        me.angle = 0
        await asyncio.sleep(delay)
        me.center_y += step
        me.angle = 90
        await asyncio.sleep(delay)
        me.center_x -= step
        me.angle = 180
        await asyncio.sleep(delay)
        me.center_y -= step
        me.angle = 270
        await asyncio.sleep(delay)

