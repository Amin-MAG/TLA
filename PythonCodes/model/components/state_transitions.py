class BaseTransition:

    def __init__(self, conditions, state):
        self.conditions = conditions
        self.to_state = state


class PushDownTransition(BaseTransition):

    LAMBDA = "LAMBDA"
    DOLLAR_SIGN = "$"

    def __init__(self, conditions, state, pop_data, push_data):
        super().__init__(conditions, state)
        self.pop_data = pop_data
        self.push_data = push_data


class TuringTransition(BaseTransition):

    R = "RIGHT"
    L = "LEFT"
    DOLLAR_SIGN = "$"

    def __init__(self, conditions, state, writing_data, direction):
        super().__init__(conditions, state)
        self.writing_data = writing_data
        self.direction = direction
