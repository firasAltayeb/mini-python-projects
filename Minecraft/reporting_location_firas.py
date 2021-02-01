from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
mc.postToChat("x coordinate is {}".format(x))
mc.postToChat("y coordinate is {}".format(y))
mc.postToChat("z coordinate is {}".format(z))
