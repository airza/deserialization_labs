class Tsukimi:
    def __init__(self, fur, brain):
        self.fur = fur
        self.brain = brain
        self.cutest = self
    @property
    def brain(self):
        return self._brain.lower()
    @brain.setter
    def brain(self, value):
        self._brain = value