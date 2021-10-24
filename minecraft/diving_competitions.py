import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

score = 0
playerId = mc.getPlayerEntityId("TCCMinecraft001")
pos_x, pos_y, pos_z = mc.entity.getPos(playerId)
blockAbove = mc.getBlock(pos_x, pos_y + 2, pos_z)

while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    score = score + 1
    pos_x, pos_y, pos_z = mc.entity.getPos(playerId)
    blockAbove = mc.getBlock(pos_x, pos_y + 2, pos_z)

    mc.postToChat("Current score: " + str(score))

mc.postToChat("Final Score: " + str(score))
if score > 6:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x - 5, y + 10, z - 5,
                 x + 5, y + 10, z + 5, 38)
