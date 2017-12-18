'''
This script convert the predicted labels of LieX to uvd format.

Predicted labels:
    https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X/lie_hand_jnts_estm_result.txt

Ref:
    Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, and Li Cheng, 
    "Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups."
    International Journal of Computer Vision (IJCV) 2017.
'''

import os
import sys
import numpy as np
from util import *


def print_usage():
    print('usage: {} icvl/nyu/msra in_file out_file'.format(sys.argv[0]))
    exit(-1)


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
    joints_xyz = get_positions(in_file)
    params = get_param(dataset)
    convert_id = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 13, 0]
    joints_xyz = joints_xyz[:, convert_id, :]
    joints_uvd = world2pixel(joints_xyz, *params)
    save_results(joints_uvd, out_file)

if __name__ == '__main__':
    main()
