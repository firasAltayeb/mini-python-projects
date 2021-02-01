from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

block = 79
mc.setBlock(x, y, z, block)

for i in range(10):
    mc.setBlock(x, y, z, block)
    x += 1
