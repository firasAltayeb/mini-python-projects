from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

water = 8
distance = 1

playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)

while distance < 10:
    mc.setBlocks(x + distance, y, z, x + distance, y, z + 10, water)
    mc.setBlocks(x + distance, y, z, x + distance, y, z - 10, water)
    distance += 1
    sleep(1.0)



