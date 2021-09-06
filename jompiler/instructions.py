import numpy as np
import sapien.core as sapien
import mplib
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
        super().__init__("move to pose {}".format(pose))
        self.pose = pose
        self.grasp = grasp


    def execute(self, env, full_state):
        env.robot.unpack(full_state['robot'])
        self.robot = env.robot
        self._setup_planner()
        active_joints = self.robot.get_active_joints()
        result = self.planner.plan(self.pose, self.robot.get_qpos(),time_step=1/250)
        if result['status'] != "Success":
            print("error")
            return env, full_state

        n_step = result['position'].shape[0]
        for i in range(n_step):
            qf = self.robot.compute_passive_force(
                gravity=True,
                coriolis_and_centrifugal=True
            )
            self.robot.set_qf(qf)
            for j in range(7):
                active_joints[j].set_drive_target(result['position'][i][j])
                active_joints[j].set_drive_velocity_target(result['velocity'][i][j])
            env.scene.step()
            if i % 4 == 0:
                env.scene.update_render()
                env.viewer.render()
        full_state['robot'] = self.robot.pack()
        full_state['articulation'] = []
        for art in env.articulation:
            full_state['articulation'].append(art.pack())
        return env, full_state

    def _setup_planner(self):
        link_names = [link.get_name() for link in self.robot.get_links()]
        joint_names = [joint.get_name() for joint in self.robot.get_active_joints()]
        self.planner = mplib.Planner(
            urdf="../../bigbrainrobotics/assets/panda/panda.urdf",
            srdf="../../bigbrainrobotics/assets/panda/panda.srdf",
            user_link_names=link_names,
            user_joint_names=joint_names,
            move_group="panda_hand",
            joint_vel_limits=np.ones(7),
            joint_acc_limits=np.ones(7))
class IsAbove(Relational):
    def __init__(self):
        super().__init__("Top")
        pass
    def check(self, full_state):
        pass

