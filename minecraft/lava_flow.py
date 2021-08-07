from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId("TCCMinecraft008")
x, y, z = mc.entity.getPos(playerId)


lava = 10
water = 8
air = 0

mc.setBlock(x+3, y+3, z, lava)
sleep(20)
mc.setBlock(x+3, y+5, z, water)
sleep(4)
mc.setBlock(x+3, y+5, z, air)
