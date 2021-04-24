from mcpi.minecraft import Minecraft

mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft001")

x,y,z = mc.entity.getPos(playerId)

nLayer = 20
for l in range(1,nLayer+1):
	for i in range(l*2-1):
		for j in range(l*2-1):
			mc.setBlock(x+i-l+1, y+nLayer-l, z+j-l+1, 57)