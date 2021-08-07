from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft008")


def undo_walk():
    while True:
        x, y, z = mc.entity.getPos(playerId)
        mc.setBlocks(x - 10, y - 10, z - 10, x + 10, y + 10, z + 10, 0)
        sleep(0.1)


undo_walk()
