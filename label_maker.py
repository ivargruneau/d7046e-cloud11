import numpy as np
import xarray
import netCDF4
from matplotlib import pyplot as plt
import pickle

from pprint import pprint   

import os


if __name__ == '__main__':
    path = './skogsstyrelsen-data/'
    train = np.load(path + 'skogs_json_val.npy', allow_pickle=True)
    answers = {}
    for t in train:
        answers[t['ValideringsobjektBildId']] = t['MolnDis']
    
    #with open('val_labels.pkl', 'wb') as f:
    #    pickle.dump(answers, f)

    with open('val_labels.pkl', 'rb') as f:
        thing = pickle.load(f)
    pprint(thing)
