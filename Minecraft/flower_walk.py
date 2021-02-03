from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

flower_block = 38

while True:
    position = mc.player.getTilePos()
    x = position.x
    y = position.y
    z = position.z
    mc.setBlock(x, y, z, flower_block)
    sleep(0.1)
