'''
This script convert the predicted labels of denseReg to uvd format.

Predicted labels:
    https://github.com/melonwan/denseReg/blob/master/exp/result/

Ref:
    Chengde Wan, Thomas Probst, Luc Van Gool, and Angela Yao, 
    "Dense 3D Regression for Hand Pose Estimation." 
    arXiv preprint arXiv:1707.1711.08996 (arXiv) 2017.
'''

import os
import sys
import numpy as np
from util import *


def print_usage():
    print('usage: {} icvl/nyu/msra in_file out_file'.format(sys.argv[0]))
    exit(-1)

def get_positions_without_filename(in_file):
    with open(in_file) as f:
        positions = [list(map(float, line.strip().split()[1:])) for line in f]
    return np.reshape(np.array(positions), (-1, len(positions[0]) / 3, 3))
	
def save_results(results, out_file):
    with open(out_file, 'w') as f:
        for i in range(results.shape[0]):
            for j in range(results.shape[1]):
                for k in range(results.shape[2]):
                    f.write('{:.3f} '.format(results[i, j, k]))
            f.write('\n')


def main():
    if len(sys.argv) < 3:
        print_usage()

    dataset = sys.argv[1]
    in_file = sys.argv[2]
    out_file = sys.argv[3]
    joints_xyz = get_positions_without_filename(in_file)
    params = get_param(dataset)
    if dataset == 'nyu':
        joints_uvd = world2pixel(joints_xyz, 588.03, 587.07, 320, 240)
    else:
		joints_uvd = world2pixel(joints_xyz, *params)
    save_results(joints_uvd, out_file)

if __name__ == '__main__':
    main()
