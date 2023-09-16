import asyncio


async def think(me):
    me.center_x = 550
    me.center_y = 450
    me.angle = 0
    speed = 2
    num_of_turns = 7
    me.forward(speed)

    turn = 360 // num_of_turns
    while True:
        for _ in range(num_of_turns):
            await asyncio.sleep(0.3)
            me.turn_right(turn)
            me.stop()
            me.forward(speed)
        turn = -turn
