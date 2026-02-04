class InstructionService:

    def send_instruction(self, pilot, instruction):
        pilot.current_instruction = instruction

        # Sends instruction from ATC to pilot.


