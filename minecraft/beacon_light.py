from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft008")

position = mc.entity.getPos(playerId)
x = position.x
y = position.y
z = position.z

diamondBlock = 57
beaconBlock = 138
# base layer
mc.setBlocks(x, y, z, x+6, y, z+6, diamondBlock)
# middle layer one
mc.setBlocks(x+1, y+1, z+1, x+5, y, z+5, diamondBlock)
# middle layer two
mc.setBlocks(x+2, y+2, z+2, x+4, y+1, z+4, diamondBlock)
# # to make beacon top
mc.setBlock(x+3, y+3, z+3, beaconBlock)


