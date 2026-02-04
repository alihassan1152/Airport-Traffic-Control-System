class TrackingService:

    def show_position(self, airplane):
        position = airplane.position
        altitude = airplane.altitude

        print(f"Airplane at {position}, altitude {altitude}")

        # Controller ko airplane ki current position dikhani hai


    def track_movement(self, airplane, radar_data):
        airplane.position = radar_data.position
        airplane.speed = radar_data.speed
        airplane.altitude = radar_data.altitude

        # Radar + Data + Plane + Update
        # Radar se data laina or plane ko update karna.


    def update_real_time(self, airplane):
        airplane.last_updated = "now"

        # Data fresh rakhne ke liye



