import time

class RealtimeService:

    def update_airplane_status(self, airplane): # System real time information update karta hai

        print("Starting real-time tracking...\n")

        for i in range(3):  # simulate 3 updates

            airplane.altitude -= 1000
            airplane.speed -= 20

            print(
                f"Update {i+1} → "
                f"Altitude: {airplane.altitude}, "
                f"Speed: {airplane.speed}"
            )

            time.sleep(1)

        print("\nReal-time update completed.")



