class RunwayOperationService:

    def manage_landing(self, airplane, runway):
        if runway.is_available:
         airplane.status = "Landing"
         runway.is_available = False

        # runway free hai?
        # to plane land kare ga
        # runay free nahi.
        # to plane land nahe karega


    def manage_takeoff(self, airplane, runway):
        if runway.is_available:
            airplane.status = "Takeoff"
            runway.is_available = False

        # 2 planes zada pass to nahe.

