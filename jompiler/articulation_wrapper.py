import sapien.core as sapien


class SapArticulation(sapien.Articulation):
    def __init__(self, name, articulation, **kwargs):
        self.name = name
        self.articulation = articulation
