from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

x, y, z = mc.player.getTilePos()
block_id = 103

mc.setBlock(x + 1, y+1, z, block_id)
mc.setBlock(x + 1, y+2, z, block_id)
mc.setBlock(x + 1, y+3, z, block_id)
mc.setBlock(x + 1, y+4, z, block_id)

