class Camera:
    def __init__(self, x: float=0, y: float=0, z: float=0, ax: float=0, ay: float=0,az: float=0, *args, **kwargs) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.ax = ax
        self.ay = ay
        self.az = az

    def __repr__(self) -> str:
        return "Camera("+str(round(self.x,4))+", "+str(round(self.y,4))+", "+str(round(self.z,4))+")@("+str(round(self.ax, 4))+"°, "+str(round(self.ay, 4))+"°, "+str(round(self.az, 4))+"°)"
        
