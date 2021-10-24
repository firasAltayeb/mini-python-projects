from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft008")

block_to_spawn = 38

while True:
    x, y, z = mc.entity.getPos(playerId)
    mc.setBlock(x, y, z, block_to_spawn)
    sleep(0.3)
