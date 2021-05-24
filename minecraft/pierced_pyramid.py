from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc.tokyocodingclub.com")
playerId = mc.getPlayerEntityId("TCCMinecraft008")
x, y, z = mc.entity.getPos(playerId)

x = x + 2
z = z + 2
# We will set the number of blocks we want in a variable
size = 8
# We will use a k for the size
k = 0
while k < size:
    i = 0
    # We will use i to repeat our diagonal
    while i < size - k:
        j = 0
        # We will use j to loop over one of our diagonal
        while j < size - k:
            mc.setBlock(x + i - j, y + k, z + i + j + k, 24)
            # We use a timer so we can see the pyramid drawing slowly
            sleep(0.05)
            j = j + 1
        i = i + 1
    k = k + 1
