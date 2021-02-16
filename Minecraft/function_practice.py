from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create("mc2.tokyocodingclub.com")

lava = 10
water = 8
air = 0

playerId = mc.getPlayerEntityId("TCCMinecraft001")
x, y, z = mc.entity.getPos(playerId)

def lava_fountain():
    mc.setBlock(x+3, y+3, z, lava)
    sleep(20)
    mc.setBlock(x+3, y+5, z, water)
    sleep(4)
    mc.setBlock(x+3, y+5, z, air)


def gameOver():
    while True:
        sleep(1)
        chats= mc.events.pollChatPosts()

        for chat in chats:
            if(chat.message=='kill player'):
                mc.entity.setTilePos(playerIds[0],x,-100,z)
            elif(chat.message=='lava fountain'):
                lava_fountain()

gameOver()

