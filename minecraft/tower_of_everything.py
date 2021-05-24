import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId('TCCMinecraft008')

x,y,z,= mc.entity.getTilePos(playerId)

all_blocks = list(range(1, 255))
random.shuffle(all_blocks)
for i in range(len(all_blocks)):
    mc.setBlock(x, y+i, z+1, all_blocks[i])

