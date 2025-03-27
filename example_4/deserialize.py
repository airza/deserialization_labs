import os
import pickle
cat = pickle.load(open('tsukimi.pickle', 'rb'))
print(cat.fur)
print(cat.brain)