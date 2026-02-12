from Services.tracking_service import TrackingService
from Services.landing_service import LandingService
from Services.sepration_service import SeparationService
from Services.instruction_service import InstructionService
from Services.emergency_service import EmergencyService
from Services.real_time_service import RealtimeService
from Entities.airplane import Airplane
from Entities.radar_data import RadarData
from Entities.air_traffic_controller import AirTrafficController
from Entities.pilot import Pilot


class Menu:

    def __init__(self):
    # yahan sab function ki services ko add kar ke unko call kiya jata hai.
        self.tracking_service = TrackingService()                   # FR- 01-02
        self.landing_service = LandingService()                     # FR-03
        self.sepration_service = SeparationService()                # FR-04
        # self.instruction_service = InstructionService()             # FR-05
        self.emergency_service = EmergencyService()                 # FR-06
        # self.real_time_service = RealtimeService()                  # FR-07

    # FR-01
    def show_airplane_position(self):
        airplane = Airplane(
            id = 1,
            position = "Point A",
            speed = 500,
            altitude = 30000
        )
        self.tracking_service.show_position(airplane)

    # FR-02
    def track_airplane_movement(self):
        airplane = Airplane(
            id = 2,
            position = "Near Airport",
            speed = 450,
            altitude = 28000
        )

        radar_data = RadarData(

            signal_strength = "Strong",
            detected_position = "Zone A"
        )
        self.tracking_service.track_movement(airplane, radar_data)

        # FR-03
    def manage_landing_sequence(self):
            airplane1 = Airplane(
                id = 1,
                position = "Air",
                speed = 400,
                altitude = 15000
            )

            airplane2 = Airplane(
                id = 2,
                position = "Air",
                speed = 420,
                altitude = 12000
            )
            self.landing_service.manage_sequence(airplane1,airplane2)


    # FR-04
    def maintain_safe_distance(self):
        airplane1 = Airplane(
            id = 6,
            position = "Air",
            speed = 900,
            altitude = 1100
        )

        airplane2 = Airplane(
            id = 7,
            position = "Earth",
            speed = 0,
            altitude = 0
        )
        self.sepration_service.maintain_safe_distance(airplane1,airplane2)

    # FR-05
    # def send_instruction_to_pilot(self):
    #     controller = AirTrafficController(
    #         controller_id = 1,
    #         name="Ali Controller"
    #     )
    #
    #     pilot = Pilot(
    #         pilot_id = 101,
    #         name="Captain Hassan"
    #     )
    #
    #     instruction_text = "Reduce altitude to 10000 ft"
    #
    #     self.instruction_service.send_instruction(controller, pilot, instruction_text)

    # FR-06
    def handle_emergency_situation(self):
        airplane = Airplane(
            id = 10,
            position = "Near Airport",
            speed = 300,
            altitude = 8000
        )

        pilot = Pilot(
            pilot_id = 200,
            name="Captain Handrikson"
        )

        controller = AirTrafficController(
            controller_id = 2,
            name="Senior Controller"
        )

        emergency_type = "Engine Failure"

        self.emergency_service.handle_emergency(airplane,pilot,controller,emergency_type)

    # FR-07
    # def update_real_time_information(self):
    #     airplane = Airplane(
    #         id = 50,
    #         position = "Approaching Airport",
    #         speed = 500,
    #         altitude = 15000
    #     )
    #     self.real_time_service.update_airplane_status(airplane)












































































