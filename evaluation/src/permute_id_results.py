import os
import sys
import numpy as np
from util import *

'''
Permute the id of joints to keep consistent with other papers.
Our cnn-pose for NYU dataset uses id [33, 31, 32, 25, 26, 28, 1, 4, 7, 10, 13, 16, 19, 22] (matlab code)
Previous papers use id [0, 3, 6, 9, 12, 15, 18, 21, 24, 25, 27, 30, 31, 32] (python code)
Just use for current version of cnn-pose.
'''


def print_usage():
    print('usage: {} in_file out_file'.format(sys.argv[0]))
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

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    joints = get_positions(in_file)
    convert_id = [6,7,8,9,10,11,12,13,3,4,5,1,2,0]
    joints = joints[:, convert_id, :]
    save_results(joints, out_file)

if __name__ == '__main__':
    main()
