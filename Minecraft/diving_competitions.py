from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getTilePos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
    score = score + 1
    mc.postToChat("Current score: " + str(score))

mc.postToChat("Final Score: " + str(score))
if score > 6:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x - 5, y + 10, z - 5,
                 x + 5, y + 10, z + 5, 38)
