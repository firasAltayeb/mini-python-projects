from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)


def destroy(size):
    while True:
        sleep(0.5)
        mc.setBlocks(x-size, y, z-size, x+size, y+size, z+size, 0)


destroy(10)
