from PythonCodes.model.automatons.fa import FA
from PythonCodes.model.components.state_transitions import TuringTransition


class Turing(FA):

    def __init__(self, states, starting_state):
        super().__init__(states, starting_state)
        self.tape = [TuringTransition.DOLLAR_SIGN, TuringTransition.DOLLAR_SIGN]
        self.pointer_index = 1

    def start_checking(self, w):
        read = self.tape[self.pointer_index]
        current_transition = self.current.transitions
        accepted_for_next_step = list(filter(lambda trans: read in trans.conditions, current_transition))

        # halts
        if len(accepted_for_next_step) == 0:
            print("In State {} Pointer Index is {} Reading '{}'\nTape = {}\n"
                  .format(self.current.name, self.pointer_index, self.tape[self.pointer_index], self.tape))
            # check if we are in final state
            if self.current.is_final_state:
                return True
            return False
        # still can go
        else:
            transition = accepted_for_next_step[0]
            print("In State {} Pointer Index is {} Reading '{}'\nTape = {}\nPut '{}' Instead Of {} And Go to {}\n"
                  .format(self.current.name, self.pointer_index, self.tape[self.pointer_index], self.tape,
                          transition.writing_data, self.tape[self.pointer_index], transition.direction))
            self.tape[self.pointer_index] = transition.writing_data
            if transition.direction == TuringTransition.R:
                self.pointer_index += 1
            else:
                self.pointer_index -= 1
            self.current = self.states[transition.to_state]
            return self.start_checking(w)

    # Utils Functions
    @staticmethod
    def get_tape_from_word(word):
        tape = []
        tape.append(TuringTransition.DOLLAR_SIGN)
        for letter in word:
            tape.append(letter)
        tape.append(TuringTransition.DOLLAR_SIGN)
        return tape
