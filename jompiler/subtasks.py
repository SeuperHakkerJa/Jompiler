from instructions import Instruction, Relational
import sapien.core as sapien

class Open(Instruction):
    def __init__(self, object):
        super().__init__("Open")
        self.object = object

    def execute(self, env, full_state, render=False, recorder=None):
        next_state = ...
        err_state = ...
        if render:
            pass
        return next_state


    def compute_rewrard(self, s, a, ns):
        pass

    def __str__(self):
        return "Opening door of {}".format(self.object.name)



class Put(Instruction):

    def __init__(self, object1, relation:Relational, object2=None):
        super().__init__("Put")
        self.object1 = object1
        self.relation = relation
        self.object2 = object2

    def execute(self, full_state):
        return full_state

    def __str__(self) -> str:
        s = "Putting {} to the {}".format(self.object1.name, self.relation.instruction_str)
        if self.object2 is not None:
            s += " of the {}".format(self.object2.name)
        return s


