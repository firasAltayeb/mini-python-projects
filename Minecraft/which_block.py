from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

which_block_id = mc.getBlockWithData(x, y-1, z)
id_as_string = str(which_block_id)

mc.postToChat("The block below has an id of " + id_as_string)

