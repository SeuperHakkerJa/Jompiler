import numpy as np
import sapien.core as sapien
from articulation_wrapper import SapArticulation
class MyObject:
    def __init__(self, name):
        self.name = name



class Instruction():
    def __init__(self, instruction_str):
        self.instruction_str = instruction_str

    def execute(self, **kwargs):
        raise NotImplementedError

    def get_reward(self, **kwargs):
        raise NotImplementedError

    @classmethod
    def parse(cls, text:str) :
        pass

    def __str__(self):
        return self.instruction_str




class Relational():
    def __init__(self, instruction_str):
        self.instruction_str=instruction_str

    def check(self, full_state):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class MoveTo(Instruction):
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
        super().__init__("Top")
        pass
    def check(self, full_state):
        pass

