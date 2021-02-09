import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")

length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
# x2 = x + 1
# y2 = y + 0
# z2 = z + 1

# Create a tower at specified location (x,y,z) with specified length, width, and height
def generateTower(x,y,z,length,width,height):
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
        length *= .9
        width *= .9
        height *= .9
        z += height


def drawRow(x,y,z,length,width,height):
    for i in range(6):
        generateTower(x,y,z,length,width,height)
        x += 1

for i in range(6):
    drawRow(x,y,z,length,width,height)
    y+=1



# pyrosim.Send_Cube(name="Box", pos=[x2,y2,z2] , size=[length,width,height])
pyrosim.End()