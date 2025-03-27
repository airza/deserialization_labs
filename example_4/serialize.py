import pickle
from tsukimi import Tsukimi
cat = Tsukimi("fluffy","brain.txt")
cat.brain = "meow meow meow meow meow meow"
pickle.dump(cat, open("tsukimi.pickle", "wb"))

