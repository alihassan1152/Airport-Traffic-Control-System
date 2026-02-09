from Presentation.menu import Menu                                    # Presentation ke folder se menu ko import karna.




# FR-01
def main():
    menu = Menu()                                                                               # Menu ka object bnana.
    menu.show_airplane_position()                                        # Controller ko plane ki position show karwana.

if __name__ == "__main__":                                    # Contoroller ko batana ke yahan se function start kardo.
    main()



# FR-02
def main():
    menu = Menu()
    menu.track_airplane_movement()

if __name__ == "__main__":
    main()

































































# def __init__(self):
#     self.tracking_service = TrackingService()
#     self.landing_service = LandingService()
