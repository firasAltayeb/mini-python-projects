from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create("mc2.tokyocodingclub.com")

diamond = 57
beacon = 138

lava = 10
water = 8
air = 0

playerId = mc.getPlayerEntityId("TCCMinecraft008")
x, y, z = mc.entity.getPos(playerId)
playerIds = mc.getPlayerEntityIds()


def lava_fountain():
    mc.setBlock(x+3, y+3, z, lava)
    sleep(20)
    mc.setBlock(x+3, y+5, z, water)
    sleep(4)
    mc.setBlock(x+3, y+5, z, air)


def create_beacon():
    mc.setBlocks(x, y, z, x+4, y, z+4, diamond)
    mc.setBlocks(x+1, y+1, z+1, x+3, y+1, z+3, diamond)
    mc.setBlock(x+2, y+3, z+2, beacon)


def game_over():
    while True:
        sleep(1)
        chats = mc.events.pollChatPosts()

        for chat in chats:
            if chat.message == 'kill player':
                mc.entity.setTilePos(playerIds[1], x, -100, z)
            elif chat.message == 'lava fountain':
                lava_fountain()
            elif chat.message == 'diamond beacon':
                create_beacon()


game_over()

