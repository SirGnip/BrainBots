import random
import asyncio


async def think(me):
    pos_jitter = 5
    angle_jitter = 30
    while True:
        me.center_x += random.randint(-pos_jitter, pos_jitter)
        me.center_y += random.randint(-pos_jitter, pos_jitter)
        me.angle += random.randint(-angle_jitter, angle_jitter)
        await asyncio.sleep(random.uniform(0.1, 0.2))
