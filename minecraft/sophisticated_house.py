from mcpi import block
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc.tokyocodingclub.com")

# Determine the Player's current position.
playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)

width = 5
height = 3
depth = 6

# Create a hollow shell made of bricks.
mc.setBlocks(x, y, z + 3, x + width, y + height, z + 3 + depth, block.DIAMOND_BLOCK.id)
mc.setBlocks(x + 1, y, z + 4, x + width - 1, y + height - 1, z + 2 + depth, block.AIR.id)

# Set the floor.
mc.setBlocks(x - 1, y - 1, z + 2, x + 1 + width, y - 1, z + 4 + depth, block.GOLD_BLOCK.id)

# Add a Door.
mc.setBlock(x+1, y, z+3, block.DOOR_WOOD.id, 0)
mc.setBlock(x+1, y+1, z+3, block.DOOR_WOOD.id, 8)

# Add Windows.
mc.setBlocks(x+3, y+1, z+3, x+4, y+2, z+3, block.GLASS.id)
mc.setBlocks(x+2, y+1, z+3+depth, x+3, y+2, z+3+depth, block.GLASS.id)
mc.setBlocks(x, y+1, z+5, x, y+2, z+7, block.GLASS.id)
mc.setBlocks(x+width, y+1, z+5, x+width, y+2, z+7, block.GLASS.id)

# Add a Roof.
for i in range(int(width / 2) + 1):
    mc.setBlocks(x + i, y + height + i, z + 3, x + i, y + height + i, z + 3 + depth, 133)
    mc.setBlocks(x + width - i, y + height + i, z + 3, x + width - i, y + height + i, z + 3 + depth, 133)
    # Gable ends.
    if int(width / 2) - i > 0:
        mc.setBlocks(x + 1 + i, y + height + i, z + 3, x + width - i - 1, y + height + i, z + 3, 133)
        mc.setBlocks(x + 1 + i, y + height + i, z + 3 + depth, x + width - i - 1, y + height + i, z + 3 + depth, 133)
