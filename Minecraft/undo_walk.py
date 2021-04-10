from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft001")
unwantedBlock = 8


def undo():
    while True:
        x, y, z = mc.entity.getPos(playerId)
        block_to_right = mc.getBlock(x + 1, y, z)
        block_to_left = mc.getBlock(x - 1, y, z)
        block_above = mc.getBlock(x, y + 1, z)
        block_beneath = mc.getBlock(x, y - 1, z)
        block_in_front = mc.getBlock(x, y, z + 1)
        block_behind = mc.getBlock(x, y, z - 1)

        if block_to_right == unwantedBlock:
            mc.setBlock(x + 1, y, z, 0)
        if block_to_left == unwantedBlock:
            mc.setBlock(x - 1, y, z, 0)
        if block_above == unwantedBlock:
            mc.setBlock(x, y + 1, z, 0)
        if block_beneath == unwantedBlock:
            mc.setBlock(x, y - 1, z, 0)
        if block_in_front == unwantedBlock:
            mc.setBlock(x, y, z + 1, 0)
        if block_behind == unwantedBlock:
            mc.setBlock(x, y, z - 1, 0)

        sleep(0.1)


undo()
