from PythonCodes.model.automatons.fa import FA
from PythonCodes.model.components.state_transitions import PushDownTransition


class PDA(FA):

    def __init__(self, states, starting_state):
        super().__init__(states, starting_state)

    def start_checking(self, w, stack=None):
        current_transition = self.current.transitions
        accepted_for_next_step = []

        if stack is None:
            stack = []

        # filling accepted_for_next_step
        if w != "":
            accepted_for_next_step = list(filter(lambda transition: w[0] in transition.conditions, current_transition))

        # the word has been finished
        if w == "":
            # check if we are in final state
            if self.current.is_final_state:
                return True
            # check if we can go to final state with lambda transition
            lambda_transition = list(
                filter(lambda transition: PushDownTransition.LAMBDA in transition.conditions, current_transition))
            if len(lambda_transition) != 0:
                lambda_transition = lambda_transition[0]
                lambda_stack = list(stack)
                self.current = self.states[lambda_transition.to_state]
                return self.pop_push_stack(
                    lambda_stack,
                    lambda_transition.pop_data,
                    lambda_transition.push_data
                ) and self.start_checking(w, lambda_stack)
        # still have to read next letter
        elif len(accepted_for_next_step) != 0:
            for accepted_transition in accepted_for_next_step:
                new_stack = list(stack)
                if self.pop_push_stack(new_stack, accepted_transition.pop_data, accepted_transition.push_data):
                    temp_state = self.current
                    self.current = self.states[accepted_transition.to_state]
                    if self.start_checking(w[1:], new_stack):
                        return True
                    self.current = temp_state
        return False

    # Utils Functions
    @staticmethod
    def pop_push_stack(stack, pop_data, push_data):

        if pop_data == push_data == PushDownTransition.DOLLAR_SIGN:
            return len(stack) == 0
        else:
            # pop data
            if pop_data != PushDownTransition.LAMBDA:
                if len(stack) != 0 and stack[-1] == pop_data:
                    stack.pop()
                else:
                    return False
            # push data
            if push_data != PushDownTransition.LAMBDA:
                stack.append(push_data)
        return True
