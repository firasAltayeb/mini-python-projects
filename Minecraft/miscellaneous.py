from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

which_block = mc.getBlock(x, y-1, z)

mc.postToChat("The block below has an id of {}".format(which_block))

