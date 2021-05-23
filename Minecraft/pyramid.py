from mcpi.minecraft import Minecraft

mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft001")

x, y, z = mc.entity.getPos(playerId)

nLayer = 20
for g in range(1, nLayer + 1):
	for i in range(g * 2 - 1):
		for j in range(g * 2 - 1):
			mc.setBlock(x + i - g + 1, y + nLayer - g, z + j - g + 1, 57)
