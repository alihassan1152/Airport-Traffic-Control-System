class TrackingService:

    # @staticmethod
    def show_position(airplane):
        position = airplane.position
        altitude = airplane.altitude

        print(f"Airplane at {position}, altitude {altitude}")         # Controller ko plane ki current position dikhna.




    # @staticmethod
    def track_movement(airplane, radar_data):
        print(
            f"Tracking airplane {airplane.id} | "
            f"Radar: {radar_data.detected_position}, "
            f"Speed: {airplane.speed}, "
            f"Altitude: {airplane.altitude}"
        )


                                                                            # Radar se data lina or plne ko show karna.
    # @staticmethod
    def update_real_time(airplane):
        airplane.last_updated = "now"

                                                                                        # Data ko fresh rakhne ke liye.
















































































 # def track_movement(airplane, radar_data):
    #     airplane.position = radar_data.position
    #     airplane.speed = radar_data.speed
    #     airplane.altitude = radar_data.altitude
