'''
This file is modified on https://github.com/guohengkai/region-ensemble-network/blob/master/evaluation/compute_error.py

Xinghao Chen
Aug 18, 2017

'''

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors as colors
from util import get_errors, get_msra_viewpoint

FONT_SIZE_XLABEL= 15
FONT_SIZE_YLABEL= 15
FONT_SIZE_LEGEND = 11.8
FONT_SIZE_TICK = 11.8


def print_usage():
    print('usage: {} icvl/nyu/msra max-frame/mean-frame/joint method_name in_file'.format(sys.argv[0]))
    exit(-1)


def draw_error_bar(dataset, errs, eval_names, fig):
    if dataset == 'icvl':
        joint_idx = range(17)
        names = ['Palm', 'Thumb.R', 'Thumb.M', 'Thumb.T', 'Index.R', 'Index.M', 'Index.T', 'Mid.R', 'Mid.M', 'Mid.T', 'Ring.R', 'Ring.M', 'Ring.T', 'Pinky.R', 'Pinky.M', 'Pinky.T', 'Mean']
        max_range = 25
    elif dataset == 'nyu':
        joint_idx = range(13, -1, -1)+[14]
        names = ['Palm', 'Wrist1', 'Wrist2', 'Thumb.R1', 'Thumb.R2', 'Thumb.T', 'Index.R', 'Index.T', 'Mid.R', 'Mid.T', 'Ring.R', 'Ring.T', 'Pinky.R', 'Pinky.T', 'Mean']
        max_range = 30
    elif dataset == 'msra':
        joint_idx = range(22)
        names = ['Wrist', 'Index.M', 'Index.P', 'Index.D', 'Index.T', 'Mid.M', 'Mid.P', 'Mid.D', 'Mid.T', 'Ring.M', 'Ring.P', 'Ring.D', 'Ring.T', 'Pinky.M', 'Pinky.P', 'Pinky.D', 'Pinky.T', 'Thumb.M', 'Thumb.P', 'Thumb.D', 'Thumb.T', 'Mean']
        max_range = 24
    
    eval_num = len(errs)
    bar_range = eval_num + 1
    # new figure
    #fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1,2,1)
    # color map
    values = range(bar_range-1)
    jet = plt.get_cmap('jet') 
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=jet)
    
    for eval_idx in xrange(eval_num):
        x = np.arange(eval_idx, bar_range*len(joint_idx), bar_range)
        mean_errs = np.mean(errs[eval_idx], axis=0)
        mean_errs = np.append(mean_errs, np.mean(mean_errs))
        print('mean error: {:.3f}mm --- {}'.format(mean_errs[-1], eval_names[eval_idx]))
        colorVal = scalarMap.to_rgba(eval_idx)
        plt.bar(x, mean_errs[joint_idx], label=eval_names[eval_idx], color=colorVal)
    x = np.arange(0, bar_range*len(joint_idx), bar_range)
    plt.xticks(x + 0.5*bar_range, names, rotation='vertical')
    plt.ylabel('Mean Error (mm)', fontsize=FONT_SIZE_YLABEL)
    plt.legend(loc='best', fontsize=FONT_SIZE_LEGEND)
    plt.grid(True)
    major_ticks = np.arange(0, max_range+1, 2)                                              
    minor_ticks = np.arange(0, max_range+1, 1)                                          
    ax.set_yticks(major_ticks)                                                       
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', alpha=0.2, linestyle=':', linewidth=0.3)                                                
    ax.grid(which='major', alpha=0.5, linestyle='--', linewidth=0.3)
    ax.set_ylim(0, max_range)                       
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    left='off',         # ticks along the top edge are off
    labelsize=FONT_SIZE_TICK)
    plt.subplots_adjust(bottom=0.14)
    fig.tight_layout()


def draw_error_curve(errs, eval_names, metric_type, fig):
    eval_num = len(errs)
    thresholds = np.arange(0, 85, 1)
    results = np.zeros(thresholds.shape+(eval_num,))
    #fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1,2,2)
    xlabel = 'Mean distance threshold (mm)'
    ylabel = 'Fraction of frames within distance (%)'
    # color map
    jet = plt.get_cmap('jet') 
    values = range(eval_num)
    if eval_num < 3:
          jet = plt.get_cmap('prism') 
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=jet)
    
    l_styles = ['-','--']
    for eval_idx in xrange(eval_num):
        if metric_type == 'mean-frame':
            err = np.mean(errs[eval_idx], axis=1)
        elif  metric_type == 'max-frame':
            err = np.max(errs[eval_idx], axis=1)
            xlabel = 'Maximum allowed distance to GT (mm)'
        elif  metric_type == 'joint':
            err = errs[eval_idx]
            xlabel = 'Distance Threshold (mm)'
            ylabel = 'Fraction of joints within distance (%)'
        err_flat = err.ravel()
        for idx, th in enumerate(thresholds):
            results[idx, eval_idx] = np.where(err_flat <= th)[0].shape[0] * 1.0 / err_flat.shape[0]
        colorVal = scalarMap.to_rgba(eval_idx)
        ls = l_styles[eval_idx%len(l_styles)]
        if eval_idx == eval_num - 1:
            ls = '-'
        ax.plot(thresholds, results[:, eval_idx]*100, label=eval_names[eval_idx], 
                color=colorVal, linestyle=ls)
    plt.xlabel(xlabel, fontsize=FONT_SIZE_XLABEL)
    plt.ylabel(ylabel, fontsize=FONT_SIZE_YLABEL)
    ax.legend(loc='best', fontsize=FONT_SIZE_LEGEND)
    plt.grid(True)
    major_ticks = np.arange(0, 81, 10)                                              
    minor_ticks = np.arange(0, 81, 5)                                               
    ax.set_xticks(major_ticks)                                                       
    ax.set_xticks(minor_ticks, minor=True)   
    major_ticks = np.arange(0, 101, 10)                                              
    minor_ticks = np.arange(0, 101, 5)                                          
    ax.set_yticks(major_ticks)                                                       
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', alpha=0.2, linestyle=':', linewidth=0.3)                                                
    ax.grid(which='major', alpha=0.5, linestyle='--', linewidth=0.3)
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 100)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    left='off',         # ticks along the top edge are off
    labelsize=FONT_SIZE_TICK)
    fig.tight_layout()    


def draw_viewpoint_error_curve(dataset, errs, eval_names, viewpoint, yp_idx, fig2):
    jet = plt.get_cmap('jet') 
    eval_num = len(errs)
    values = range(eval_num)
    if eval_num < 3:
          jet = plt.get_cmap('prism') 
    cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cm.ScalarMappable(norm=cNorm, cmap=jet)
    
    yaw_pitch = ['yaw', 'pitch']
    #fig = plt.figure(figsize=(8, 6))
    #ax = fig.add_subplot(1,1,1)
    ax = fig2.add_subplot(1,2,1+yp_idx)
    xlabel = '{} angle (deg)'.format(yaw_pitch[yp_idx])
    ylabel = 'Mean error distance (mm)'

    l_styles = ['-','--']
    for eval_idx in xrange(eval_num):
        # calculate error for each frame
        err = np.mean(errs[eval_idx], axis=1)
        if yp_idx == 0:
            x = np.arange(-40, 41, 2)   # yaw
        else:
            x = np.arange(-10, 91, 2)   # pitch
        x_error = np.zeros_like(x, dtype=np.float32)
        for idx in xrange(len(x)):
            x_idx = np.round(viewpoint[:,yp_idx]*0.5)*2 == x[idx]
            x_error[idx] = np.mean(err[x_idx])
            # print idx, np.mean(err[x_idx])
        colorVal = scalarMap.to_rgba(eval_idx)
        ls = l_styles[eval_idx%len(l_styles)]
        if eval_idx == eval_num - 1:
            ls = '-'
        ax.plot(x, x_error, label=eval_names[eval_idx], 
                color=colorVal, linestyle=ls)
    plt.xlabel(xlabel, fontsize=FONT_SIZE_XLABEL)
    plt.ylabel(ylabel, fontsize=FONT_SIZE_YLABEL)
    plt.legend(loc='upper right', fontsize=FONT_SIZE_LEGEND)
    # ax.grid(True)
    # major ticks every 20, minor ticks every 5    
    if yp_idx == 0:                                  
        major_ticks = np.arange(-40, 41, 10)                                              
        minor_ticks = np.arange(-40, 41, 5)      
        ax.set_xlim(-40, 40)
        ax.set_ylim(5, 24)    
    else:
        major_ticks = np.arange(-10, 91, 10)                                              
        minor_ticks = np.arange(-10, 91, 5)      
        ax.set_xlim(-10, 90)
        ax.set_ylim(5, 24)                                     
    ax.set_xticks(major_ticks)                                                       
    ax.set_xticks(minor_ticks, minor=True)   
    major_ticks = np.arange(5, 25, 1)                                              
    minor_ticks = np.arange(5, 24.5, 0.5)                                          
    ax.set_yticks(major_ticks)                                                       
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='minor', alpha=0.2, linestyle=':', linewidth=0.3)                                                
    ax.grid(which='major', alpha=0.5, linestyle='--', linewidth=0.3)

    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    left='off',         # ticks along the top edge are off
    labelsize=FONT_SIZE_TICK)
    fig2.tight_layout()


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

    fig = plt.figure(figsize=(16, 6))
    plt.figure(fig.number)
    draw_error_bar(dataset, eval_errs, eval_names, fig)
    #plt.savefig('figures/{}_error_bar.png'.format(dataset))
    draw_error_curve(eval_errs, eval_names, metric_type, fig)
    plt.savefig('figures/{}_error.png'.format(dataset))
    
    # msra viewpoint
    if dataset == 'msra':
        fig2 = plt.figure(figsize=(16, 6))
        plt.figure(fig2.number)
        # see https://github.com/xinghaochen/region-ensemble-network/blob/master/evaluation/get_angle.py
        # for how to calculate yaw and pitch angles for MSRA dataset
        msra_viewpoint = get_msra_viewpoint('groundtruth/{}/{}_angle.txt'.format(dataset, dataset))
        # yaw
        draw_viewpoint_error_curve(dataset, eval_errs, eval_names, msra_viewpoint, 0, fig2)
        #plt.savefig('figures/{}_yaw.pdf'.format(dataset))
        # pitch
        draw_viewpoint_error_curve(dataset, eval_errs, eval_names, msra_viewpoint, 1, fig2)
        plt.savefig('figures/{}_yaw_pitch.png'.format(dataset))
        
    plt.show()


if __name__ == '__main__':
    main()
