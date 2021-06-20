from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

grass_block = 2
flower_block = 38
playerId = mc.getPlayerEntityId("TCCMinecraft001")

while True:
    position = mc.entity.getPos(playerId)
    x = position.x
    y = position.y
    z = position.z
    block_beneath = mc.getBlock(x, y - 1, z)

    if block_beneath == grass_block:
        mc.setBlock(x, y, z, flower_block)
    sleep(0.1)
