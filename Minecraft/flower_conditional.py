from mcpi.minecraft import Minecraft
from time import sleep

grass = 2
flower = 38

mc = Minecraft.create()

while True:
    x, y, z = mc.player.getPos()  # player position (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # block ID
    
    if block_beneath == grass:
        mc.setBlock(x, y, z, flower)
    sleep(0.1)
