import numpy as np
import sapien.core as sapien

class Instruction():
    def __init__(self, instruction_str):
        self.instruction_str=instruction_str

    def execute(self):
        raise NotImplementedError

    def get_reward(self):
        raise NotImplementedError

    @classmethod
    def parse(cls, text:str):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError




class Relational():
    def __init__(self, instruction_str):
        self.instruction_str=instruction_str

    def check(self, full_state):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class MOVETO(Instruction):
    def __init__(self, pose:sapien.Pose, grasp=False):
        super().__init__("move to pose p:{}  q:{}".format(pose.p, pose.q))
        self.pose = pose
        self.grasp = grasp

    def execute(self, full_state):
        err_state = ...
        full_state = ...
        return ...

class IsAbove(Relational):
    def __init__(self):
        pass
    def check(self, full_state):
        pass

class 




