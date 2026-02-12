class InstructionService:

    def send_instruction(self, controller, pilot, instruction_text): # System pilot ko instruction bhejta hai

        print(f"Controller {controller.name} sending instruction...")

        pilot.current_instruction = instruction_text

        print(f"Pilot {pilot.name} received instruction: {pilot.current_instruction}")

