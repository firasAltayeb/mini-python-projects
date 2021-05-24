from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

position = mc.player.getTilePos()

x = position.x
y = position.y
z = position.z

mc.postToChat("x coordinate is ")
mc.postToChat(x)
mc.postToChat("y coordinate is ")
mc.postToChat(y)
mc.postToChat("z coordinate is ")
mc.postToChat(z)
