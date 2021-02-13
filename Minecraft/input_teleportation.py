from mcpi.minecraft import Minecraft

mc = Minecraft.create()

points = int(input("Enter your points: "))

if points > 6:
    mc.player.setTilePos(249, 79, -430)
elif points > 4:
    mc.player.setTilePos(-60, 96, 32)
elif points > 2:
    mc.player.setTilePos(739, 85, 112)
elif points <= 2:
    mc.player.setTilePos(0, 92, -205)
else:
    mc.postToChat("I don't know what to do with that information.")
