class FA:

    def __init__(self, states, starting_state):
        self.states = states
        self.current = starting_state

    def start_checking(self, w):
        current_transition = self.current.transitions
        accepted_for_next_step = []

        # filling accepted_for_next_step
        if w != "":
            accepted_for_next_step = list(filter(lambda tans: w[0] in tans.conditions, current_transition))

        if w == "":
            print("In State {}\nWord = '{}'\n".format(self.current.name, w))
            if self.current.is_final_state:
                return True
            return False
        elif len(accepted_for_next_step) != 0:
            transition = accepted_for_next_step[0]
            print("In State {}\nWord = '{}'\nGo To State {} by reading '{}'\n"
                  .format(self.current.name, w, transition.to_state, w[0]))
            self.current = self.states[transition.to_state]
            return self.start_checking(w[1:])
        else:
            return False
