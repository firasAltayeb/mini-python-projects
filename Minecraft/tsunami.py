from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc2.tokyocodingclub.com")

water = 8
direction = 1

playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)

while True:
    mc.setBlocks(x+direction, y, z, x+direction, y, z+10, water)
    mc.setBlocks(x+direction, y, z, x+direction, y, z-10, water)
    direction += 1
    sleep(0.1)            



