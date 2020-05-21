class BaseState:

    def __init__(self, name, is_final_state=False):
        self.name = name
        self.is_final_state = is_final_state
        self.transitions = []

    def add_to_transition(self, transition):
        self.transitions.append(transition)
