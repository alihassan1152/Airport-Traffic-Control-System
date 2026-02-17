class InstructionService:

    def send_instruction(self, controller, pilot, instruction_text):

        print(f"Controller {controller.name} sending instruction...")

        pilot.current_instruction = instruction_text

        print(f"Pilot {pilot.name} received instruction: {pilot.current_instruction}")

