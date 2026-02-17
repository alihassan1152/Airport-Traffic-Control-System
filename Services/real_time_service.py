import time

class RealtimeService:

    def update_airplane_status(self, airplane):

        print("Starting real_time Tracking...\n")

        for i in range (3):
            airplane.altitude -= 1000
            airplane.speed -= 20

            print(
                f"Update {i+1} → "
                f"Altitude: {airplane.altitude}, "
                f"Speed: {airplane.speed}"
            )

            time.sleep(0.4)

        print("\n Real_Time_Update Tracking...")






