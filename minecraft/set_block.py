from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId("TCCMinecraft008")
x, y, z = mc.entity.getPos(playerId)

block_id = 103
number_of_cycles = 2 ** 4 * 3

for i in range(0, number_of_cycles):
    mc.setBlock(x + i, y, z, block_id)

