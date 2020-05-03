#!/usr/bin/env python

import os
import sys
import math
import numpy as np

TODIR = '../tacotron2/filelists/'
assert(os.path.isdir(TODIR)), \
    "Make sure {} exists, maybe check you pulled the submodules".format(TODIR)

TRAIN = 0.9
VAL = 0.05
TEST = 0.05

np.random.seed(0)

directory = sys.argv[1]
assert(os.path.isdir(directory))

paths = [x for x in os.listdir(directory) if '_background_noise_' not in x and os.path.isdir(os.path.join(directory, x))]
print("Going through {}".format(paths))

for word in paths:
    curr_dir = os.path.abspath(os.path.join(directory, word))
    files = [x for x in os.listdir(curr_dir) if os.path.isfile(os.path.join(curr_dir, x))]
    indices = np.arange(0, len(files))
    np.random.shuffle(indices)

    train_stop = math.floor(len(indices) * TRAIN)
    val_stop = train_stop + math.floor(len(indices) * VAL)
    print(train_stop, val_stop, len(indices))

    with open(os.path.join(TODIR, 'sc_audio_text_train_filelist.txt'), 'a') as myFile:
        for idx in indices[0:train_stop]:
            myFile.write(os.path.join(curr_dir, files[idx]) + '|' + word + '\n')

    with open(os.path.join(TODIR, 'sc_audio_text_val_filelist.txt'), 'a') as myFile:
        for idx in indices[train_stop:val_stop]:
            myFile.write(os.path.join(curr_dir, files[idx]) + '|' + word + '\n')
    
    with open(os.path.join(TODIR, 'sc_audio_text_test_filelist.txt'), 'a') as myFile:
        for idx in indices[val_stop:]:
            myFile.write(os.path.join(curr_dir, files[idx]) + '|' + word + '\n')
    
    
    
     
 
