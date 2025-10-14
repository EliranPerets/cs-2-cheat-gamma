from pygame.math import Vector2, Vector3
class Entity:
    def __init__(self, controller_ptr: int, pawn_ptr: int):
        self.controller_ptr: int = controller_ptr
        self.pawn_ptr: int = pawn_ptr
        self.raw_position: Vector3 = Vector3(0, 0, 0)
        self.map_position: Vector2 = Vector2(0, 0)
        self.health: int = 0
        self.get_bone_position : Vector3 = Vector3(0, 0, 0)

    def convert_to_map_position(self, map_data: tuple) -> None:
        upper_left_x: int
        upper_left_y: int
        scale: float
        upper_left_x, upper_left_y, scale = map_data
        self.map_position = Vector2(
            (self.raw_position.x - upper_left_x) / scale,
            (self.raw_position.y - upper_left_y) / -scale
        )

    def update(self, handle, map_data: tuple) -> None:
        if self.health <= 0:
            return
        self.raw_position = Vector3(*handle.get_position(self))
        self.convert_to_map_position(map_data)