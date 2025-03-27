import pickle
class Tsukimi:
    def __init__(self, fur, brain):
        self.fur = fur
        self.brain = brain
    @property
    def brain(self):
        return "All fluff"
    @brain.setter
    def brain(self, value):
        self._brain = value
cat = pickle.load(open('tsukimi.pickle', 'rb'))
print(cat.fur)
print(cat.brain)