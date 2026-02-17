class TrackingService:

    def show_position(self,airplane):
        position = airplane.position
        altitude = airplane.altitude

        print(f"Airplane at {position}, altitude {altitude}")


    def track_movement(self, airplane, radar_data):

        print(
            f"Tracking airplane {airplane.id} | "
            f"Radar: {radar_data.detected_position}, "
            f"Speed: {airplane.speed}, "                   
            f"Altitude: {airplane.altitude}"
        )

    


















































































