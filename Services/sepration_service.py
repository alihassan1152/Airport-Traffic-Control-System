class SeparationService:

    def maintain_safe_distance(self, airplane1, airplane2):  # System planes ke darmiyan safe distance rakhta hai

        if airplane1.position == airplane2.position:
            print(" Warning: Unsafe distance between airplanes!")
        else:
            print(" Safe Distance Maintained.")



