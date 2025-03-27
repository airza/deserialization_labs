import pickle
from tsukimi import Tsukimi
cat = Tsukimi("Fluffy", "Empty")
pickle.dump(cat, open("tsukimi.pickle", "wb"))