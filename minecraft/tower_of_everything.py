import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId('TCCMinecraft008')

x, y, z, = mc.entity.getTilePos(playerId)

all_blocks = list(range(0, 255))
for i in range(len(all_blocks)):
    if i != 8 and i != 9 and i != 10 and i != 11:
        print("i is {}".format(i))
        mc.setBlock(x, y + i, z + 1, all_blocks[i])
