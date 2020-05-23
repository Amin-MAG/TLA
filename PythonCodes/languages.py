from PythonCodes.model.automatons.pda import PDA
from PythonCodes.model.automatons.turing import Turing
from PythonCodes.model.components.state import BaseState

from PythonCodes.model.components.state_transitions import BaseTransition, PushDownTransition, TuringTransition

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
            print("[*] It is Accepted")
        else:
            print("[!] It is Failed")

        print("---------------------------------------------------------------------")

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
            print("[*] It is Accepted")
        else:
            print("[!] It is Failed")

        print("---------------------------------------------------------------------")

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
        pda = PDA({
            q0.name: q0,
            q1.name: q1,
            qf.name: qf
        },
            q0)

        if pda.start_checking(word):
            print("[*] It is Accepted")
        else:
            print("[!] It is Failed")

        print("---------------------------------------------------------------------")

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
        pda = PDA({
            q0.name: q0,
            q1.name: q1,
            q2.name: q2,
            q3.name: q3,
            q4.name: q4,
            qf.name: qf
        },
            q0)

        if pda.start_checking(word):
            print("[*] It is Accepted")
        else:
            print("[!] It is Failed")

        print("---------------------------------------------------------------------")

    @staticmethod
    def check_word_for_language_number_5(word):

        # states
        q0 = BaseState("Q0")
        q1 = BaseState("Q1")
        q2 = BaseState("Q2")
        q3 = BaseState("Q3")
        q4 = BaseState("Q4")
        q5 = BaseState("Q5")
        q6 = BaseState("Q6")
        q7 = BaseState("Q7")
        q8 = BaseState("Q8")
        q9 = BaseState("Q9")
        qf = BaseState("Qf", True)

        # set transitions
        q0.add_to_transition(TuringTransition(["a"], q1.name, "1", TuringTransition.R))
        q0.add_to_transition(TuringTransition(["b"], q1.name, "2", TuringTransition.R))
        q0.add_to_transition(TuringTransition(["c"], q1.name, "3", TuringTransition.R))

        q1.add_to_transition(TuringTransition(["a"], q1.name, "a", TuringTransition.R))
        q1.add_to_transition(TuringTransition(["b"], q1.name, "b", TuringTransition.R))
        q1.add_to_transition(TuringTransition(["c"], q1.name, "c", TuringTransition.R))

        q1.add_to_transition(TuringTransition(["1"], q2.name, "1", TuringTransition.L))
        q1.add_to_transition(TuringTransition(["2"], q2.name, "2", TuringTransition.L))
        q1.add_to_transition(TuringTransition(["3"], q2.name, "3", TuringTransition.L))
        q1.add_to_transition(TuringTransition([TuringTransition.DOLLAR_SIGN], q2.name, TuringTransition.DOLLAR_SIGN,
                                              TuringTransition.L))

        q2.add_to_transition(TuringTransition(["a"], q3.name, "1", TuringTransition.L))
        q2.add_to_transition(TuringTransition(["b"], q3.name, "2", TuringTransition.L))
        q2.add_to_transition(TuringTransition(["c"], q3.name, "3", TuringTransition.L))

        q3.add_to_transition(TuringTransition(["a"], q3.name, "a", TuringTransition.L))
        q3.add_to_transition(TuringTransition(["b"], q3.name, "b", TuringTransition.L))
        q3.add_to_transition(TuringTransition(["c"], q3.name, "c", TuringTransition.L))

        q3.add_to_transition(TuringTransition(["1"], q0.name, "1", TuringTransition.R))
        q3.add_to_transition(TuringTransition(["2"], q0.name, "2", TuringTransition.R))
        q3.add_to_transition(TuringTransition(["3"], q0.name, "3", TuringTransition.R))

        q0.add_to_transition(TuringTransition(["1"], q4.name, "1", TuringTransition.L))
        q0.add_to_transition(TuringTransition(["2"], q4.name, "2", TuringTransition.L))
        q0.add_to_transition(TuringTransition(["3"], q4.name, "3", TuringTransition.L))

        q4.add_to_transition(TuringTransition(["1"], q4.name, "a", TuringTransition.L))
        q4.add_to_transition(TuringTransition(["2"], q4.name, "b", TuringTransition.L))
        q4.add_to_transition(TuringTransition(["3"], q4.name, "c", TuringTransition.L))

        q4.add_to_transition(TuringTransition([TuringTransition.DOLLAR_SIGN], q5.name, TuringTransition.DOLLAR_SIGN,
                                              TuringTransition.R))

        q5.add_to_transition(TuringTransition(["a"], q6.name, "1", TuringTransition.R))
        q5.add_to_transition(TuringTransition(["b"], q7.name, "2", TuringTransition.R))
        q5.add_to_transition(TuringTransition(["c"], q8.name, "3", TuringTransition.R))

        q6.add_to_transition(TuringTransition(["a"], q6.name, "a", TuringTransition.R))
        q6.add_to_transition(TuringTransition(["b"], q6.name, "b", TuringTransition.R))
        q6.add_to_transition(TuringTransition(["c"], q6.name, "c", TuringTransition.R))
        q6.add_to_transition(TuringTransition(["0"], q6.name, "0", TuringTransition.R))

        q7.add_to_transition(TuringTransition(["a"], q7.name, "a", TuringTransition.R))
        q7.add_to_transition(TuringTransition(["b"], q7.name, "b", TuringTransition.R))
        q7.add_to_transition(TuringTransition(["c"], q7.name, "c", TuringTransition.R))
        q7.add_to_transition(TuringTransition(["0"], q7.name, "0", TuringTransition.R))

        q8.add_to_transition(TuringTransition(["a"], q8.name, "a", TuringTransition.R))
        q8.add_to_transition(TuringTransition(["b"], q8.name, "b", TuringTransition.R))
        q8.add_to_transition(TuringTransition(["c"], q8.name, "c", TuringTransition.R))
        q8.add_to_transition(TuringTransition(["0"], q8.name, "0", TuringTransition.R))

        q6.add_to_transition(TuringTransition(["1"], q9.name, "0", TuringTransition.L))
        q7.add_to_transition(TuringTransition(["2"], q9.name, "0", TuringTransition.L))
        q8.add_to_transition(TuringTransition(["3"], q9.name, "0", TuringTransition.L))

        q9.add_to_transition(TuringTransition(["a"], q9.name, "a", TuringTransition.L))
        q9.add_to_transition(TuringTransition(["b"], q9.name, "b", TuringTransition.L))
        q9.add_to_transition(TuringTransition(["c"], q9.name, "c", TuringTransition.L))
        q9.add_to_transition(TuringTransition(["0"], q9.name, "0", TuringTransition.L))

        q9.add_to_transition(TuringTransition(["1"], q5.name, "1", TuringTransition.R))
        q9.add_to_transition(TuringTransition(["2"], q5.name, "2", TuringTransition.R))
        q9.add_to_transition(TuringTransition(["3"], q5.name, "3", TuringTransition.R))

        q5.add_to_transition(TuringTransition(["0"], qf.name, "0", TuringTransition.L))

        # create and run
        turing = Turing({
            q0.name: q0,
            q1.name: q1,
            q2.name: q2,
            q3.name: q3,
            q4.name: q4,
            q5.name: q5,
            q6.name: q6,
            q7.name: q7,
            q8.name: q8,
            q9.name: q9,
            qf.name: qf
        },
            q0)

        turing.tape = Turing.get_tape_from_word(word)

        if turing.start_checking(word):
            print("[*] It is Accepted")
        else:
            print("[!] It is Failed")

        print("---------------------------------------------------------------------")
