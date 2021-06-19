file = open("input.txt", "r")

outfile = open("output.py","w")

outfile.write("from mcpi.minecraft import Minecraft\n")
outfile.write("mc = Minecraft.create()\n")

outfile.write("x = 100\n")
outfile.write("y = 30\n")
outfile.write("z = 100\n")
outfile.write("a = 42\n")

for line in file:
    l = line[:-1].split(",")
    outfile.write("mc.setBlock(x+"+l[0]+",y+"+l[1]+",z+"+l[2]+", a)\n")

file.close()
outfile.close()
