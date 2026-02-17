class AltitudeService:

    def check_altitude(self, airplane):

        if airplane.altitude < 2000:
            print("DANGER: Very low altitude")

        elif airplane.altitude < 10000:
            print("WARNING: Low altitude")

        else:
            print("SAFE altitude")
