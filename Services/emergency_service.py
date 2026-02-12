class EmergencyService:

    def handle_emergency(self, airplane, pilot, controller, emergency_type): # System emergency situations handle karta hai

        print(f" EMERGENCY DETECTED: {emergency_type}")
        print(f"Airplane ID: {airplane.id}")
        print(f"Pilot: {pilot.name}")

        print(f"Notifying Controller {controller.name}...")

        print("Priority landing initiated.")

