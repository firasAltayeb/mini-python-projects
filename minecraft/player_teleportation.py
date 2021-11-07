from mcpi.minecraft import Minecraft

mc = Minecraft.create("mc.tokyocodingclub.com")

playerId = mc.getPlayerEntityId("TCCMinecraft008")

mc.postToChat("Enter coordinates:")
while True:
    chats = mc.events.pollChatPosts()
    firasId = mc.getPlayerEntityId("TCCMinecraft008")
    firasX, firasY, firasZ = mc.entity.getPos(playerId)
    for chat in chats:
        try:
            if all(char.isdigit() or char == ',' or char == '-'
                   for char in chat.message):
                coordinates = chat.message.split(",")
                x = int(coordinates[0])
                y = int(coordinates[2])
                z = int(coordinates[2])
                mc.entity.setTilePos(playerId, x, y, z)
            elif 'tp to fira' in chat.message:
                mc.entity.setTilePos(playerId, firasX, firasY, firasZ)
        except:
            print("bad input")