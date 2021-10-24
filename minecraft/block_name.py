from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()

x, y, z = mc.player.getPos()

mc.setBlock(x+3, y, z, block.FIRE.id)
