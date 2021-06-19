from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

position = mc.entity.getTilePos("TCCMinecraft001")
x = position.x
y = position.y
z = position.z

diamondBlock = 57
beaconBlock = 138
# to make base layer of beacon
mc.setBlocks(x, y, z, x+4, y, z+4, diamondBlock)
# to make middle layer of beacon
mc.setBlocks(x+1, y+1, z+1, x+3, y+1, z+3, diamondBlock)
# to make beacon top
mc.setBlock(x+2, y+3, z+2, beaconBlock)


