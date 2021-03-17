from mcpi.minecraft import Minecraft

mc = Minecraft.create("mc.tokyocodingclub.com")

tnt = 46

playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

