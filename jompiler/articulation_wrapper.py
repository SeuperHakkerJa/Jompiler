import sapien.core as sapien


class SapArticulation():
    def __init__(self, name, articulation, **kwargs):
        self.name = name
        self.articulation:sapien.Articulation = articulation
