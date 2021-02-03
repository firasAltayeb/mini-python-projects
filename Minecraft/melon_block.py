from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# we can make a lantern in case it's dark 169
block_id = 103

for i in range(10):
    mc.setBlock(x, y, z, block_id)
    x += 1
