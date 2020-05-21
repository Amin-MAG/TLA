from PythonCodes.model.automatons.pda import PDA
from PythonCodes.model.components.state import BaseState

from PythonCodes.model.components.state_transitions import BaseTransition, PushDownTransition

from PythonCodes.model.automatons.fa import FA


class Languages:

    @staticmethod
    def check_word_for_language_number_1(word):

        # states
        q1 = BaseState("Q1", True)
        q2 = BaseState("Q2")

        # set transitions
        q1.add_to_transition(BaseTransition(["a", "b", "c"], q2.name))
        q2.add_to_transition(BaseTransition(["a", "b", "c"], q1.name))

        # create and run
        fa = FA({q1.name: q1, q2.name: q2}, q1)

        if fa.start_checking(word):
            print(True)
        else:
            print(False)

    @staticmethod
    def check_word_for_language_number_2(word):

        # states
        q10 = BaseState("Q10", True)
        q21 = BaseState("Q21", True)
        q02 = BaseState("Q02", True)
        q00 = BaseState("Q00")
        q01 = BaseState("Q01")
        q20 = BaseState("Q20")
        q22 = BaseState("Q22")
        q11 = BaseState("Q11")
        q12 = BaseState("Q12")

        # set transitions
        q10.add_to_transition(BaseTransition(["c"], q10.name))
        q21.add_to_transition(BaseTransition(["c"], q21.name))
        q02.add_to_transition(BaseTransition(["c"], q02.name))
        q00.add_to_transition(BaseTransition(["c"], q00.name))
        q01.add_to_transition(BaseTransition(["c"], q01.name))
        q20.add_to_transition(BaseTransition(["c"], q20.name))
        q22.add_to_transition(BaseTransition(["c"], q22.name))
        q11.add_to_transition(BaseTransition(["c"], q11.name))
        q12.add_to_transition(BaseTransition(["c"], q12.name))

        q00.add_to_transition(BaseTransition(["a"], q10.name))
        q10.add_to_transition(BaseTransition(["a"], q20.name))
        q20.add_to_transition(BaseTransition(["a"], q00.name))
        q01.add_to_transition(BaseTransition(["a"], q11.name))
        q02.add_to_transition(BaseTransition(["a"], q12.name))
        q12.add_to_transition(BaseTransition(["a"], q22.name))
        q22.add_to_transition(BaseTransition(["a"], q02.name))
        q11.add_to_transition(BaseTransition(["a"], q21.name))
        q21.add_to_transition(BaseTransition(["a"], q01.name))

        q00.add_to_transition(BaseTransition(["b"], q01.name))
        q10.add_to_transition(BaseTransition(["b"], q11.name))
        q20.add_to_transition(BaseTransition(["b"], q21.name))
        q01.add_to_transition(BaseTransition(["b"], q02.name))
        q02.add_to_transition(BaseTransition(["b"], q00.name))
        q12.add_to_transition(BaseTransition(["b"], q10.name))
        q22.add_to_transition(BaseTransition(["b"], q20.name))
        q11.add_to_transition(BaseTransition(["b"], q12.name))
        q21.add_to_transition(BaseTransition(["b"], q22.name))

        # create and run
        fa = FA({
            q00.name: q00,
            q01.name: q01,
            q02.name: q02,
            q10.name: q10,
            q11.name: q11,
            q12.name: q12,
            q20.name: q20,
            q21.name: q21,
            q22.name: q22
        },
            q00)

        if fa.start_checking(word):
            print(True)
        else:
            print(False)

    @staticmethod
    def check_word_for_language_number_3(word):

        # states
        q0 = BaseState("Q0")
        q1 = BaseState("Q1")
        qf = BaseState("Qf", True)

        # set transitions
        q0.add_to_transition(PushDownTransition(["a"], q0.name, PushDownTransition.LAMBDA, "a"))
        q0.add_to_transition(PushDownTransition(["b"], q0.name, PushDownTransition.LAMBDA, "b"))
        q0.add_to_transition(PushDownTransition(["c"], q0.name, PushDownTransition.LAMBDA, "c"))

        q1.add_to_transition(PushDownTransition(["a"], q1.name, "a", PushDownTransition.LAMBDA))
        q1.add_to_transition(PushDownTransition(["b"], q1.name, "b", PushDownTransition.LAMBDA))
        q1.add_to_transition(PushDownTransition(["c"], q1.name, "c", PushDownTransition.LAMBDA))

        q0.add_to_transition(PushDownTransition(["c"], q1.name, PushDownTransition.LAMBDA, PushDownTransition.LAMBDA))

        q1.add_to_transition(PushDownTransition([PushDownTransition.LAMBDA], qf.name, PushDownTransition.DOLLAR_SIGN,
                                                PushDownTransition.DOLLAR_SIGN))

        # create and run
        fa = PDA({
            q0.name: q0,
            q1.name: q1,
            qf.name: qf
        },
            q0)

        if fa.start_checking(word):
            print(True)
        else:
            print(False)

    @staticmethod
    def check_word_for_language_number_4(word):

        # states
        q0 = BaseState("Q0")
        q1 = BaseState("Q1")
        q2 = BaseState("Q2")
        q3 = BaseState("Q3")
        q4 = BaseState("Q4")
        qf = BaseState("Qf", True)

        # set transitions
        q0.add_to_transition(PushDownTransition(["a"], q1.name, PushDownTransition.LAMBDA, "1"))

        q1.add_to_transition(PushDownTransition(["a"], q1.name, PushDownTransition.LAMBDA, "1"))
        q1.add_to_transition(PushDownTransition(["b"], q2.name, "1", PushDownTransition.LAMBDA))

        q2.add_to_transition(PushDownTransition(["b"], q3.name, PushDownTransition.LAMBDA, "1"))
        q2.add_to_transition(PushDownTransition(["b"], q2.name, "1", PushDownTransition.LAMBDA))

        q3.add_to_transition(PushDownTransition(["a"], q4.name, "1", PushDownTransition.LAMBDA))
        q3.add_to_transition(PushDownTransition(["b"], q3.name, PushDownTransition.LAMBDA, "1"))

        q4.add_to_transition(PushDownTransition(["a"], q4.name, "1", PushDownTransition.LAMBDA))
        q4.add_to_transition(PushDownTransition([PushDownTransition.LAMBDA], qf.name, PushDownTransition.DOLLAR_SIGN,
                                                PushDownTransition.DOLLAR_SIGN))

        # create and run
        fa = PDA({
            q0.name: q0,
            q1.name: q1,
            q2.name: q2,
            q3.name: q3,
            q4.name: q4,
            qf.name: qf
        },
            q0)

        if fa.start_checking(word):
            print(True)
        else:
            print(False)
