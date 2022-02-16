from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("18.181.61.53")

player_id = mc.getPlayerEntityId("TCC_11")
while True:
    x, y, z = mc.entity.getPos(player_id)
    print("x is {0}, y is {1}, z is {2}".format(x,y,z))
    which_block = mc.getBlockWithData(x, y-1, z)
    mc.postToChat("The block below has an id of {}".format(which_block.id))
    sleep(1.0)