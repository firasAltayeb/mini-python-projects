from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#just outside the house
#x = 78
#y = 72
#z = 53

#inside the house
x = 80
y = 72
z = 59

mc.player.setTilePos(x, y, z)
