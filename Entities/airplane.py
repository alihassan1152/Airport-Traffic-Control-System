class Airplane:
    def __init__(self, plane_id, name):
        self.plane_id = plane_id
        self.name = name

        self.position = None
        self.speed = None
        self.altitude = None

        self.status = "ON_GROUND"
        self.emergency = False



"""
position  FR-01 FR-02
speed  FR-02
altitude  FR-04
status  landing / takeoff
emergency  FR-06
"""


