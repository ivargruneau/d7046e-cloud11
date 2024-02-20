import numpy as np
import xarray
import netCDF4
from matplotlib import pyplot as plt
import pickle

from pprint import pprint   

import os

def train(path):
    train = np.load(path + 'skogs_json_train.npy', allow_pickle=True)
    answers = {}
    for t in train:
        answers['skgs_'+t['ValideringsobjektBildId']+'.nc'] = t['MolnDis']
    
    with open('train_labels.pkl', 'wb') as f:
        pickle.dump(answers, f)
    
    with open('train_labels.pkl', 'rb') as f:
        thing = pickle.load(f)
    pprint(thing)

def val(path):
    validation = np.load(path + 'skogs_json_val.npy', allow_pickle=True)
    answers = {}
    for v in validation:
        answers['skgs_'+v['ValideringsobjektBildId']+'.nc'] = v['MolnDis']

    with open('val_labels.pkl', 'wb') as f:
        pickle.dump(answers, f)
    

    with open('val_labels.pkl', 'rb') as f:
        thing = pickle.load(f)
    pprint(thing)


if __name__ == '__main__':
    path = './skogsstyrelsen-data/'

    train(path)

    val(path)
