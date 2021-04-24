from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId("TCCMinecraft008")
pidX, pidY, pidY = mc.entity.getPos(playerId)

x = 144
y = 100
z = 50

mc.entity.setTilePos(playerId, x, y, z)

mc.player.setTilePos(pidX, pidY, pidY)

