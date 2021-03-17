from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc.tokyocodingclub.com")

flower_block = 38
playerId = mc.getPlayerEntityId("TCCMinecraft001")

while True:
    position = mc.entity.getPos(playerId)
    x = position.x
    y = position.y
    z = position.z
    mc.setBlock(x, y, z, flower_block)
    sleep(0.1)
