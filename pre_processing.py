import numpy as np
import pickle

from pprint import pprint   

import os

def train_labels(path):
    train = np.load(path + 'skogs_json_train.npy', allow_pickle=True)
    answers = {}
    for t in train:
        answers['skgs_'+t['ValideringsobjektBildId']+'.nc'] = t['MolnDis']
    
    with open('train_labels.pkl', 'wb') as f:
        pickle.dump(answers, f)
    
    with open('train_labels.pkl', 'rb') as f:
        thing = pickle.load(f)
    pprint(thing)

def val_labels(path):
    validation = np.load(path + 'skogs_json_val.npy', allow_pickle=True)
    answers = {}
    for v in validation:
        answers['skgs_'+v['ValideringsobjektBildId']+'.nc'] = v['MolnDis']

    with open('val_labels.pkl', 'wb') as f:
        pickle.dump(answers, f)
    

    with open('val_labels.pkl', 'rb') as f:
        thing = pickle.load(f)
    pprint(thing)


def find_files(filetype, path="."):
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(filetype):
                filelist += [os.path.join(root, file)]
    return filelist

def train_files(full_list=None):
    if full_list == None:
        full_list = find_files('.nc')
    res = np.array([])
    
    train_list = np.load('./skogsstyrelsen-data/skogs_names_train.npy')
    for item in full_list:
        hate = '../data/skogsstyrelsen/2A-netcdfs-cropped-from-nuria/' + item[52:]
        if np.isin(hate, train_list):
            res = np.append(res, item)

    with open('train_file_names.npy', 'wb') as f:
        np.save(f, res)
    
    return res
        
def val_files(full_list=None):
    if full_list == None:
        full_list = find_files('.nc')
    res = np.array([])
    val_list = np.load('./skogsstyrelsen-data/skogs_names_val.npy')
    for item in full_list:
        hate = '../data/skogsstyrelsen/2A-netcdfs-cropped-from-nuria/' + item[52:]
        if np.isin(hate, val_list):
            res = np.append(res, item)

    with open('val_file_names.npy', 'wb') as f:
        np.save(f, res)
    
    return res

def test_files(full_list=None):
    if full_list == None:
        full_list = find_files('.nc')
    res = np.array([])
    test_list = np.load('./skogsstyrelsen-data/skogs_names_test.npy')
    for item in full_list:
        hate = '../data/skogsstyrelsen/2A-netcdfs-cropped-from-nuria/' + item[52:]
        if np.isin(hate, test_list):
            res = np.append(res, item)

    with open('test_file_names.npy', 'wb') as f:
        np.save(f, res)
    
    return res

if __name__ == '__main__':
    path = './skogsstyrelsen-data/'
    filelist = find_files('.nc')
    t = train_files(filelist)
    v = val_files(filelist)
    t2 = test_files(filelist)

    print(filelist)
    

