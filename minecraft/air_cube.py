from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getPos()

stoneBlock = 1
airBlock = 0

mc.setBlocks(x, y, z, x + 3, y + 3, z + 3, stoneBlock)
mc.setBlocks(x + 1, y + 1, z + 1, x + 2, y + 3, z + 2, airBlock)