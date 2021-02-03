from mcpi.minecraft import Minecraft
from time import sleep

grass_block = 2
flower_block = 38

mc = Minecraft.create()

while True:
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    block_beneath = mc.getBlock(x, y - 1, z)

    if block_beneath == grass_block:
        mc.setBlock(x, y, z, flower_block)
    sleep(0.1)
