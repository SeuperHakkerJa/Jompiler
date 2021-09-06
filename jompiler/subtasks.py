from .instructions import Instruction, Relational
import sapien.core as sapien
from .articulation_wrapper import SapArticulation
from .instructions import MoveTo
class Open(Instruction):
    def __init__(self, object, robot=None):
        super().__init__("Open")
        self.object = object
        self.robot = robot

    def execute(self, env, full_state, render=True, recorder=None):

        env.robot.unpack(full_state['robot'])
        self.robot = env.robot
        env, full_state = self._open_gripper(env, full_state, True)

        import numpy as np
        from transforms3d.euler import euler2quat
        poses=[
            [0.7, -0.05, 0.6] + list(euler2quat(-np.deg2rad(90), np.deg2rad(0), -np.deg2rad(90))),
            [0.75, -0.05, 0.6] + list(euler2quat(-np.deg2rad(90), np.deg2rad(0), -np.deg2rad(90))),
            [0.8011, -0.049, 0.6] + list(euler2quat(-np.deg2rad(90), np.deg2rad(0), -np.deg2rad(90)))

        ]
        subtasks=[]
        for pose in poses:
            task=MoveTo(pose)
            subtasks.append(task)

        for subtask in subtasks:
            env, full_state = subtask.execute(env, full_state)


        env, full_state = self._close_gripper(env, full_state, True)
        pose = [0.65, -0.05,0.6] + list(euler2quat(-np.deg2rad(90),np.deg2rad(0),-np.deg2rad(90)))
        task = MoveTo(pose)
        for _ in range(10):
             env, full_state = task.execute(env, full_state)
        return env,full_state




    def compute_rewrard(self, s, a, ns):
        pass

    def __str__(self):
        return "Opening door of {}".format(self.object.name)


    def _open_gripper(self, env, full_state, render):
        active_joints = self.robot.get_active_joints()
        for joint in active_joints[-2:]:
            joint.set_drive_target(0.4)
        for i in range(100):
            qf = self.robot.compute_passive_force(
                gravity=True,
                coriolis_and_centrifugal=True
            )
            self.robot.set_qf(qf)
            env.scene.step()
            if i % 4 == 0 and render:
                env.scene.update_render()
                env.viewer.render()
        full_state['robot'] = self.robot.pack()
        full_state['articulation'] = []
        for art in env.articulation:
            full_state['articulation'].append(art.pack())
        return env, full_state
    def _close_gripper(self, env,full_state, render):
        active_joints = self.robot.get_active_joints()
        for joint in active_joints[-2:]:
            joint.set_drive_target(0)
            joint.set_drive_velocity_target(-100)
        for i in range(100):
            qf = self.robot.compute_passive_force(
                gravity=True,
                coriolis_and_centrifugal=True
            )
            self.robot.set_qf(qf)
            env.scene.step()

            if i % 4 == 0 and render:
                env.scene.update_render()
                env.viewer.render()

        full_state['robot'] = self.robot.pack()
        full_state['articulation'] = []
        for art in env.articulation:
            full_state['articulation'].append(art.pack())
        return env, full_state


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


