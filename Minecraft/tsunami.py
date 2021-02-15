from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc2.tokyocodingclub.com")

water = 8
direction = 1

playerIds = mc.getPlayerEntityIds()
x, y, z = mc.entity.getPos(playerIds[0])

while True:
    mc.setBlock(x+direction, y, z, water)
    direction += 1
    sleep(0.1)            



