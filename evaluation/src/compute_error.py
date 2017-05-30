'''
This file is modified on https://github.com/guohengkai/region-ensemble-network/blob/master/evaluation/compute_error.py
'''

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from util import get_errors


def print_usage():
    print('usage: {} icvl/nyu/msra max-frame/mean-frame/joint method_name in_file'.format(sys.argv[0]))
    exit(-1)


def draw_error(dataset, errs, eval_names):
    if dataset == 'icvl':
        joint_idx = range(17)
        names = ['Palm', 'Thumb.R', 'Thumb.M', 'Thumb.T', 'Index.R', 'Index.M', 'Index.T', 'Mid.R', 'Mid.M', 'Mid.T', 'Ring.R', 'Ring.M', 'Ring.T', 'Pinky.R', 'Pinky.M', 'Pinky.T', 'Mean']
    elif dataset == 'nyu':
        joint_idx = range(13, -1, -1)+[14]
        names = ['Palm', 'Wrist1', 'Wrist2', 'Thumb.R1', 'Thumb.R2', 'Thumb.T', 'Index.R', 'Index.T', 'Mid.R', 'Mid.T', 'Ring.R', 'Ring.T', 'Pinky.R', 'Pinky.T', 'Mean']
    elif dataset == 'msra':
        joint_idx = range(22)
        names = ['Wrist', 'Index.M', 'Index.P', 'Index.D', 'Index.T', 'Mid.M', 'Mid.P', 'Mid.D', 'Mid.T', 'Ring.M', 'Ring.P', 'Ring.D', 'Ring.T', 'Pinky.M', 'Pinky.P', 'Pinky.D', 'Pinky.T', 'Thumb.M', 'Thumb.P', 'Thumb.D', 'Thumb.T', 'Mean']
    
    colors = ['b', 'r', ]
    eval_num = len(errs)
    plt.figure()
    bar_range = eval_num + 1
    for eval_idx in xrange(eval_num):
        x = np.arange(eval_idx, bar_range*len(joint_idx), bar_range)
        mean_errs = np.mean(errs[eval_idx], axis=0)
        mean_errs = np.append(mean_errs, np.mean(mean_errs))
        print('mean error: {:.3f}mm --- {}'.format(mean_errs[-1], eval_names[eval_idx]))
        plt.bar(x, mean_errs[joint_idx], label=eval_names[eval_idx], color=cm.jet(1.*eval_idx/eval_num))
    x = np.arange(0, bar_range*len(joint_idx), bar_range)
    plt.xticks(x + 0.5*bar_range, names, rotation='vertical')
    plt.ylabel('Mean Error (mm)')
    plt.legend(loc='best')
    plt.grid(True)


def draw_map(errs, eval_names, metric_type):
    eval_num = len(errs)
    thresholds = np.arange(0, 85, 1)
    results = np.zeros(thresholds.shape+(eval_num,))
    plt.figure()
    xlabel = 'Mean distance threshold (mm)'
    ylabel = 'Fraction of frames within distance'
    for eval_idx in xrange(eval_num):
        if metric_type == 'mean-frame':
            err = np.mean(errs[eval_idx], axis=1)
        elif  metric_type == 'max-frame':
            err = np.max(errs[eval_idx], axis=1)
            xlabel = 'Maximum allowed distance to GT (mm)'
        elif  metric_type == 'joint':
            err = errs[eval_idx]
            xlabel = 'Distance Threshold (mm)'
            ylabel = 'Fraction of joints within distance'
        err_flat = err.ravel()
        for idx, th in enumerate(thresholds):
            results[idx, eval_idx] = np.where(err_flat <= th)[0].shape[0] * 1.0 / err_flat.shape[0]
        plt.plot(thresholds, results[:, eval_idx], label=eval_names[eval_idx])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(loc='best')
    plt.grid(True)
    

def main():
    if len(sys.argv) < 3:
        print_usage()

    dataset = sys.argv[1]
    metric_type = sys.argv[2]
    eval_names = []
    eval_files = []
    eval_errs = []

    for idx in xrange(3, len(sys.argv), 2):
        in_name = sys.argv[idx]
        in_file = sys.argv[idx+1]
        eval_names.append(in_name)
        eval_files.append(in_file)
        err = get_errors(dataset, in_file)
        eval_errs.append(err)

    draw_error(dataset, eval_errs, eval_names)
    draw_map(eval_errs, eval_names, metric_type)
    plt.show()


if __name__ == '__main__':
    main()
