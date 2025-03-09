class Camera:
    def __init__(self, x: float=0, y: float=0, z: float=0, *args, **kwargs) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Camera({round(self.x,4)}, {round(self.y,4)}, {round(self.z,4)})"
        
