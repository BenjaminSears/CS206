import pybullet as p
import pybullet_data

class WORLD:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeID = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")