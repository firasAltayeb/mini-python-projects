from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerIds = mc.getPlayerEntityIds()
playerId = mc.getPlayerEntityId("TCCMinecraft008")
pidX, pidY, pidY = mc.entity.getPos(playerId)

x = 144
y = 100
z = 50

mc.entity.setTilePos(playerId, x, y, z)

if playerId == playerIds[1]:
    mc.player.setTilePos(pidX, pidY, pidY)

