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
    def __init__(self, x: float=0, y: float=0, z: float=0) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return "Point3D("+str(round(self.x, 4))+", "+str(round(self.y, 4))+", "+str(round(self.z, 4))+")"
    

    def to_matrix(self, direction: str="vert") -> Matrix:
        if direction == "horiz":
            return Matrix([
                [self.x,self.y,self.z]
            ])
        if direction == "vert":
            return Matrix([
                [self.x],
                [self.y],
                [self.z]
            ])
                
    @staticmethod
    def from_matrix(matrix: Matrix) -> "Point3D":
        if len(matrix.cols) == 3 and len(matrix.rows) == 1:
            x, y, z = matrix.cols[0]
            return Point3D(x, y, z)
        if len(matrix.cols) == 1 and len(matrix.rows) == 3:
            x = matrix.rows[0][0]
            y = matrix.rows[1][0]
            z = matrix.rows[2][0]
            return Point3D(x, y, z)
    

    def rotateX(self, angle: float) -> "Point3D":
        rot = Matrix([
            [ 1         , 0         , 0         ],
            [ 0         , cos(angle),-sin(angle)],
            [ 0         , sin(angle), cos(angle)]
        ])
        # self = self.to_matrix().mult(rot)
        return Point3D.from_matrix(rot.mult(self.to_matrix()))

    def rotateY(self, angle: float) -> "Point3D":
        rot = Matrix([
            [ cos(angle), 0         , sin(angle)],
            [ 0         , 1         , 0         ],
            [-sin(angle), 0         , cos(angle)]
        ])
        # self = self.to_matrix().mult(rot)
        return Point3D.from_matrix(rot.mult(self.to_matrix()))

    def rotateZ(self, angle: float) -> "Point3D":
        rot = Matrix([
            [ cos(angle),-sin(angle), 0         ],
            [ sin(angle), cos(angle), 0         ],
            [ 0         , 0         , 1         ]
        ])
        # self = self.to_matrix().mult(rot)
        return Point3D.from_matrix(rot.mult(self.to_matrix()))


    def rotate(self, ax: float, ay: float, az: float) -> "Point3D":
        return self.rotateX(ax).rotateY(ay).rotateZ(az)


    def project_ortho(self, camera: Camera, sx: float=1, sz: float=1) -> tuple[float,float]:
        # x = scale_x * self.x + camera.x
        # y = scale_z * self.z + camera.z
        point_matrix = self.to_matrix()

        scale_matrix = Matrix([
            [sx, 0 , 0 ],
            [0 , 0 , sz]
        ])
        camera_matrix = Matrix([
            [camera.x],
            [camera.z]
        ])

        point_matrix = scale_matrix.mult(point_matrix)
        point_matrix = point_matrix.add(camera_matrix)
        return tuple(point_matrix.cols[0])


    def old_project_perspective(self, camera: Camera) -> tuple[float,float]:
        # camera_matrix = Matrix([
            # [camera.x],
            # [camera.y],
            # [camera.z]
        # ])
        # translated_point = self.to_matrix().sub(camera_matrix)
        # ex, ey, ez = [1,1,1]
        # d = Point3D().from_matrix(translated_point).rotate(camera.ax, camera.ay, camera.az)
        # bx = (ex / d.z) * d.x + ex
        # by = (ez / d.z) * d.y + ey
        # return (bx, by)def project_perspective(self, camera: Camera) -> tuple[float,float]:
        # Step 1: Translate the point relative to the camera position
        camera_matrix = Matrix([
            [camera.x],
            [camera.y],
            [camera.z]
        ])
        translated_point = self.to_matrix(direction="vert").sub(camera_matrix)
        
        # Step 2: Rotate the point according to camera orientation
        point_obj = Point3D.from_matrix(translated_point)
        rotated_point = point_obj.rotateX(camera.ax).rotateY(camera.ay).rotateZ(camera.az)
        
        # Step 3: Apply perspective projection
        # Define focal length (distance from camera to projection plane)
        focal_length = camera.focal_length
        
        # Avoid division by zero
        if rotated_point.z <= 0:
            rotated_point.z = 0.01
        
        # Calculate projected coordinates
        projected_x = (focal_length / rotated_point.z) * rotated_point.x
        projected_y = (focal_length / rotated_point.z) * rotated_point.y
        
        # Apply screen center offset if needed
        screen_center_x = 0  # Adjust as needed
        screen_center_y = 0  # Adjust as needed
        
        return (projected_x + screen_center_x, projected_y + screen_center_y)
    
    def project_perspective(self, camera, screen_width, screen_height) -> tuple[float,float]:
        camera_matrix = Matrix([
            [camera.x],
            [camera.y],
            [camera.z]
        ])
        translated_point = self.to_matrix(direction="vert").sub(camera_matrix)
        translated = Point3D.from_matrix(translated_point)
        translated = translated.rotateX(camera.ax).rotateY(camera.ay).rotateZ(camera.az)
        
        if translated.z <= 10:
            return None  # Point is behind or too close to camera - don't render
        
        # Use a larger focal length for better scaling
        focal_length = camera.focal_length
        
        # Calculate projected coordinates with scaling factor
        scale = focal_length / translated.z
        projected_x = translated.x * scale
        projected_y = translated.y * scale
        
        # Center on screen
        screen_x = projected_x + screen_width / 2
        screen_y = projected_y + screen_height / 2
        
        # Clipping - don't return points too far outside the screen
        # This prevents extreme values from causing issues
        margin = 500  # Allow some points outside the visible area for partial objects
        if (screen_x < -margin or screen_x > screen_width + margin or 
            screen_y < -margin or screen_y > screen_height + margin):
            return None
            
        return (screen_x, screen_y)

