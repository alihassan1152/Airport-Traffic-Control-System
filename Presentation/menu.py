from Services.tracking_service import TrackingService
from Entities.airplane import Airplane
from Entities.radar_data import RadarData

class Menu:

    def __init__(self):
        self.tracking_service = TrackingService()

    # FR-01
    def show_airplane_position(self):
        airplane = Airplane(
            id=1,
            position="Point A",
            speed=500,
            altitude=30000
        )
        self.tracking_service.show_position(airplane)


    # FR-02
    def track_airplane_movement(self):
        airplane = Airplane(
            id=2,
            position="Near Airport",
            speed=450,
            altitude=28000
        )

        radar_data = RadarData(
            signal_strength="Strong",
            detected_position="Zone A"
        )

        self.tracking_service.track_movement(airplane, radar_data)

















































































        # # FR-03
        # def manage_landing_sequence(self):
        #     airplane = Airplane(
        #         id=3,
        #         position="Approaching Airport",
        #         speed=300,
        #         altitude=5000
        #     )
        #
        #     runway = Runway(
        #         name="Runway A",
        #         is_available=True
        #     )
        #
        #     self.landing_service.manage_landing_takeoff(airplane, runway)
        #























    # def track_airplane_movement(self):
    #     airplane = Airplane(
    #         id=2,
    #         position="Near Airport",
    #         speed=450,
    #         altitude=28000
    #     )
    #     self.tracking_service.track_movement(airplane)
    #
