from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

block_id = 103

for i in range(0, 10):
    mc.setBlock(x + i, y, z, block_id)
