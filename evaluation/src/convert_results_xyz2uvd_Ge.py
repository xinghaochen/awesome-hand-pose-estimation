'''
This script convert the predicted labels of CVPR17 3DCNN, CVPR18 Hand PointNet, ECCV18 Point-to-Point to uvd format.

Predicted labels:
    https://sites.google.com/site/geliuhaontu/home/cvpr2017
    https://drive.google.com/file/d/1M1iZyPZ3jU1_KIH0kJKvg1TwolpwLQxy/view?usp=sharing
	
	https://sites.google.com/site/geliuhaontu/home/cvpr2018
	https://drive.google.com/file/d/1hYsgLvpuKpWpBkVzrIdCetJPWzGCtooB/view
	
	https://sites.google.com/site/geliuhaontu/home/eccv2018
	https://drive.google.com/file/d/1hvAf7iee7bysDi26639qP9LfvucXBcTM/view

Ref:
    3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images
    Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann, 
    IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017
	
	Hand PointNet: 3D Hand Pose Estimation using Point Sets
	Liuhao Ge, Yujun Cai, Junwu Weng, Junsong Yuan
	IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018 (Spotlight)

	Point-to-Point Regression PointNet for 3D Hand Pose Estimation
	Liuhao Ge, Zhou Ren, Junsong Yuan
	European Conference on Computer Vision (ECCV), 2018
'''

import os
import sys
import numpy as np
import scipy.io as sio
from util import *


def print_usage():
    print('usage: {} icvl/nyu/msra in_file out_file'.format(sys.argv[0]))
    exit(-1)

def get_positions_from_mat(in_file, dataset):
    data = sio.loadmat(in_file)
    if dataset == 'nyu':
        pred_xyz = data['xyz_estimation']
    elif dataset == 'icvl':
        pred_xyz = data['joint_est_wld_xyz']
    elif dataset == 'msra':
        pred_xyz = np.asarray(data['P0_xyz_estimation'])
        for test_id in xrange(1, 9):
            pred_xyz_test_id = np.asarray(data['P{}_xyz_estimation'.format(test_id)])
            #print pred_xyz_test_id.shape
            pred_xyz = np.concatenate((pred_xyz, pred_xyz_test_id), axis=0)
    return np.asarray(pred_xyz)

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
    joints_xyz = get_positions_from_mat(in_file, dataset)
	
    if dataset == 'msra':
        # to deal with annoying camera intrinsic parameters
        joints_xyz[:, :, 1:] = -joints_xyz[:, :, 1:]
    
    params = get_param(dataset)
    joints_uvd = world2pixel(joints_xyz, *params)
    save_results(joints_uvd, out_file)

if __name__ == '__main__':
    main()
