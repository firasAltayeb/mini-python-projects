file = open("charizard.txt", "r")
outfile = open("charizard.py", "w")

outfile.write("from mcpi.minecraft import Minecraft\n")
outfile.write('mc = Minecraft.create("mc.tokyocodingclub.com")\n')
outfile.write('playerId = mc.getPlayerEntityId("TCCMinecraft008")\n\n')

outfile.write("pos_x, pos_y, pos_z = mc.entity.getPos(playerId)\n")
outfile.write("block_id = 155\n\n")

for lines in file:
    line = lines[:-1].replace(" ", "").split(",")
    outfile.write("mc.setBlock(pos_x+" + line[0] + ", pos_y+"
                  + line[1] + ", pos_z+" + line[2] + ", block_id)\n")

file.close()
outfile.close()
