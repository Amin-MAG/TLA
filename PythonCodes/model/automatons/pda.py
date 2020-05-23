from PythonCodes.model.automatons.fa import FA
from PythonCodes.model.components.state_transitions import PushDownTransition


class PDA(FA):

    def __init__(self, states, starting_state):
        super().__init__(states, starting_state)
        self.tab_counter = 0

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
            tab_distance = self.tab_counter * "\t"
            # check if we are in final state
            if self.current.is_final_state:
                print("{}In State {}\n{}Word = '{}'\n{}Stack = {}\n\n{}[*] Halts\n"
                      .format(tab_distance,
                              self.current.name,
                              tab_distance,
                              w,
                              tab_distance,
                              stack,
                              tab_distance))
                return True
            # check if we can go to final state with lambda transition
            lambda_transition = list(
                filter(lambda transition: PushDownTransition.LAMBDA in transition.conditions, current_transition))
            if len(lambda_transition) != 0:
                lambda_transition = lambda_transition[0]
                self.print_lambda(stack, tab_distance, w)
                lambda_stack = list(stack)
                self.current = self.states[lambda_transition.to_state]
                if self.pop_push_stack(
                        lambda_stack,
                        lambda_transition.pop_data,
                        lambda_transition.push_data
                ) and self.start_checking(w, lambda_stack):
                    return True
                else:
                    print(tab_distance + "[!] Halts And Returns\n")
                    return False
            else:
                print(tab_distance + "[!] Halts And Returns\n")
                return False
        # still have to read next letter
        elif len(accepted_for_next_step) != 0:
            for index, accepted_transition in enumerate(accepted_for_next_step):
                new_stack = list(stack)
                if self.pop_push_stack(new_stack, accepted_transition.pop_data, accepted_transition.push_data):
                    temp_state = self.current
                    if len(accepted_for_next_step) > 1:
                        tab_distance = self.tab_counter * "\t"
                        print("{}Way Number {} In State {} With Stack {}\n"
                              .format(tab_distance, index + 1, self.current.name, new_stack))
                        self.tab_counter += 1
                    tab_distance = self.tab_counter * "\t"
                    self.print_step(accepted_transition, new_stack, tab_distance, w)
                    self.current = self.states[accepted_transition.to_state]
                    if self.start_checking(w[1:], new_stack):
                        return True
                    if len(accepted_for_next_step) > 1:
                        self.tab_counter -= 1
                    self.current = temp_state
        return False

    def print_lambda(self, stack, tab_distance, w):
        print("{}In State {}\n{}Word = '{}'\n{}Stack = {}\n{}We Can Go To State: Lambda_Transition\n"
              .format(tab_distance,
                      self.current.name,
                      tab_distance,
                      w,
                      tab_distance,
                      stack,
                      tab_distance))

    def print_step(self, accepted_transition, new_stack, tab_distance, w):
        print("{}In State {}\n{}Word = '{}'\n{}Stack = {}\n{}We Can Go To State {} FROM {}\n"
              .format(tab_distance,
                      self.current.name,
                      tab_distance,
                      w,
                      tab_distance,
                      new_stack,
                      tab_distance,
                      accepted_transition.to_state,
                      self.current.name))

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
