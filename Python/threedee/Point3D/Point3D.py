from math import cos as _cos
from math import sin as _sin
from math import pi
from CustomMath import Matrix
from threedee import Camera

def sin(x):
    return _sin(x*(pi/180))
    
def cos(x):
    return _cos(x*(pi/180))

class Point3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return f"Point3D({round(self.x, 4)}, {round(self.y, 4)}, {round(self.z, 4)})"
    

    def to_matrix(self) -> Matrix:
        return Matrix([
            [self.x,self.y,self.z]
        ])

    def from_matrix(matrix: Matrix) -> "Point3D":
        if len(matrix.cols) == 3 and len(matrix.rows[0]) == 1:
            x, y, z = matrix.cols
            return Point3D(matrix)
    

    def rotateX(self, angle: float) -> None:
        rot = Matrix([
            [ 1         , 0         , 0         ],
            [ 0         , cos(angle),-sin(angle)],
            [ 0         , sin(angle), cos(angle)]
        ])
        self = self.to_matrix().mult(rot)
        return self

    def rotateY(self, angle: float) -> None:
        rot = Matrix([
            [ cos(angle), 0         , sin(angle)],
            [ 0         , 1         , 0         ],
            [-sin(angle), 0         , cos(angle)]
        ])
        self = self.to_matrix().mult(rot)
        return self

    def rotateZ(self, angle: float) -> None:
        rot = Matrix([
            [ cos(angle),-sin(angle), 0         ],
            [ sin(angle), cos(angle), 0         ],
            [ 0         , 0         , 1         ]
        ])
        self = self.to_matrix().mult(rot)
        return self


    def project_ortho(self, camera: Camera, sx: float=1, sz: float=1) -> tuple[float,float]:
        # x = scale_x * self.x + camera.x
        # y = scale_z * self.z + camera.z

        scale_matrix = Matrix([
            [sx, 0 , 0 ],
            [0 , 0 , sz]
        ])
        camera_matrix = Matrix([
            [camera.x],
            [camera.z]
        ])

        point_matrix = scale_matrix.mult(self.to_matrix())
        point_matrix = point_matrix.add(camera_matrix)
        return tuple(point_matrix.cols[0])
