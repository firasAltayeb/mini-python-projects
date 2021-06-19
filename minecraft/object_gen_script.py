file = open("giant_egg_input.txt", "r")
outfile = open("giant_egg_script.py", "w")

outfile.write("from mcpi.minecraft import Minecraft\n")
outfile.write("mc = Minecraft.create()\n")

outfile.write("pos_x = 100\n")
outfile.write("pos_y = 30\n")
outfile.write("pos_z = 100\n")
outfile.write("block_id = 42\n")

for lines in file:
    line = lines[:-1].replace(" ", "").split(",")
    outfile.write("mc.setBlock(pos_x+" + line[0] + ", pos_y+"
                  + line[1] + ", pos_z+" + line[2] + ", block_id)\n")

file.close()
outfile.close()
