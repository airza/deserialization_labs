import pickle
class Tsukimi:
    def __init__(self, fur, brain):
        self.fur = fur
        self.brain = brain
    @property
    def brain(self):
        return self._brain.lower()
    @brain.setter
    def brain(self, value):
        self._brain = value
cat = Tsukimi("Fluffy", "Empty")
pickle.dump(cat, open("tsukimi.pickle", "wb"))