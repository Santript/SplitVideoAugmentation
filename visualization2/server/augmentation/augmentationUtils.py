import os

def createDirectories(sm):
    if not os.path.exists(os.path.join('dataset', sm)):
        os.mkdir(os.path.join('dataset', sm))
    if not os.path.exists(os.path.join('augmentedDataset/train', sm)):
        os.mkdir(os.path.join('augmentedDataset/train', sm))
    if not os.path.exists(os.path.join('augmentedDataset/validation', sm)):
        os.mkdir(os.path.join('augmentedDataset/validation', sm))
