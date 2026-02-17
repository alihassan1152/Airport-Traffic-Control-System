from Presentation.menu import Menu

def main():
    menu = Menu()

    menu.show_airplane_position()
    menu.track_airplane_movement()
    menu.manage_landing_sequence()
    menu.maintain_safe_distance()
    menu.send_instruction_to_pilot()
    menu.handle_emergency_situation()
    menu.update_real_time_information()

if __name__ == "__main__":
    main()