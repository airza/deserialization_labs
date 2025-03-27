class Tsukimi:
    def __init__(self, fur, brain):
        self.fur = fur
        self._brain = brain
        self.brain_file = open(brain, 'r+')
    def __reduce__(self):
        return (self.__class__, (self.fur, self._brain))
    @property
    def brain(self):
        self.brain_file.seek(0)
        return self.brain_file.read()
    @brain.setter
    def brain(self, value):
        self.brain_file.seek(0)
        self.brain_file.write(value)