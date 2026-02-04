class EmergencyService:

    def handle_emergency(self, airplane, emergency):
        airplane.emergency_status = emergency
        airplane.priority = "High"


        # Handles emergency situations



