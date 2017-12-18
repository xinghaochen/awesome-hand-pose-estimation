# Evaluations on hand pose estimation

## Description
This project provides codes to evaluate performances of hand pose estimation on several public datasets, including [NYU](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm), [ICVL](https://labicvl.github.io/hand.html), [MSRA](https://jimmysuen.github.io/) hand pose dataset. We collect predicted labels of some prior works **_which are available online_** and visualize the performances.

## Evaluation metric
There are two types of evaluation metrics that are widely used for hand pose estimation:

(1) Mean error for each joint

(2) Success rate:
 - The proportion of test frames whose average error falls below a threshold
 - The proportion of test frames whose maximum error falls below a threshold
 - The proportion of all joints whose error falls below a threshold

## Methods and corresponding predicted labels
### ICVL
- LRF \[1\]: CVPR'14, [Predicted labels](http://www.iis.ee.ic.ac.uk/~dtang/dataset/Results.tar.gz)
- DeepModel \[2\]: IJCAI'16, [Predicted labels](http://xingyizhou.xyz/IJCAI16_ICVL.txt)
- Guo-Baseline \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_basic.txt)
- REN-4x6x6 \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_ren_4x6x6.txt)
- REN-9x6x6 \[7\]: arXiv'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_ren_9x6x6.txt)
- Pose-REN \[8\]: arXiv'17, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/icvl/arXiv17_ICVL_Pose_REN.txt)
- DenseReg \[10\]: arXiv'17, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/icvl.txt)

### NYU
- DeepPrior \[4\]: CVWW'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/CVWW15_ICVL_Prior.txt)
- DeepPrior-Refinement \[4\]: CVWW'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/CVWW15_ICVL_Prior-Refinement.txt)
- Feedback \[5\]: CVPR'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/ICCV15_NYU_Feedback.txt)
- DeepModel \[2\]: IJCAI'16, [Predicted labels](http://xingyizhou.xyz/IJCAI16_NYU.txt)
- Lie-X \[6\]: IJCV'16, [Predicted labels](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X/lie_hand_jnts_estm_result.txt)
- Guo-Baseline \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_basic.txt)
- REN-4x6x6 \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_ren_4x6x6.txt)
- REN-9x6x6 \[7\]: arXiv'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_ren_9x6x6.txt)
- Pose-REN \[8\]: arXiv'17, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/nyu/arXiv17_NYU_Pose_REN.txt)
- DeepPrior++ \[9\]: ICCVW'17, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/ICCVW17_NYU_DeepPrior__.txt)
- DenseReg \[10\]: arXiv'17, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/nyu.txt)
- [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017) \[11\]: CVPR'17, [Predicted labels](https://drive.google.com/file/d/1M1iZyPZ3jU1_KIH0kJKvg1TwolpwLQxy/view?usp=sharing)

### MSRA
- REN-9x6x6 \[7\]: arXiv'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/msra_ren_9x6x6.txt)
- Pose-REN \[8\]: arXiv'17, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/msra/arXiv17_MSRA_Pose_REN.txt)
- DenseReg \[10\]: arXiv'17, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/msra.txt)
- [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017) \[11\]: CVPR'17, [Predicted labels](https://drive.google.com/file/d/1M1iZyPZ3jU1_KIH0kJKvg1TwolpwLQxy/view?usp=sharing)

### Notes
- Note that only 14 out of 36 joints are used for evaluation and we use the joints with id [0, 3, 6, 9, 12, 15, 18, 21, 24, 25, 27, 30, 31, 32]. All labels are in the format of (u, v, d) where u and v are pixel coordinates.

- **The code to plot errors over different yaw and pitch angles for MSRA is still under construction and needs further improvement. Stay tuned.**

- For [Lie-X](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X.html), the original predicted labels are in format of (x, y, z) and the order of joints is different. We convert the labels from xyz to uvd and permute the order of joints to keep consistent with other methods (see src/convert_results_xyz2uvd_LieX.py).

- For [DenseReg](https://github.com/melonwan/denseReg), we convert the original predicted labels from xyz to uvd (see src/convert_results_xyz2uvd_denseReg.py).

- Since [DeepPrior[4]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) and [DeepPrior++[9]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) only provide predicted labels of Sequence A (702 frames) for ICVL dataset (totally 1596 frames for two test sequences), we havn't included these method in comparisions for ICVL dataset yet.

- [DeepPrior++[9]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) also provides predicted labels of for MSRA dataset online. However, the results seem to be shuffled so we havn't included these results yet, stay tuned.

- For [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017), we convert the original predicted labels from xyz to uvd (see src/convert_results_xyz2uvd_3DCNN.py).

## Usage
Use the python code to show the evaluation results:
```
python compute_error.py icvl/nyu/msra max-frame/mean-frame/joint method_names in_files
```
The first parameter indicates which dataset is being evaluated while the second one indicates which type of success rate that is listed above is being chosen. The following parameters specify the names of methods and their corresponding predict label files.

We provide easy-to-use bash scripts to display performances of some methods, just run the following command:
```
sh evaluate_{dataset}.sh
```
## Results
### Results on NYU dataset
![figures/nyu_error_bar.png](figures/nyu_error.png)

### Results on ICVL dataset
![figures/icvl_error_bar.png](figures/icvl_error.png)

### Results on MSRA dataset
![figures/msra_error_bar.png](figures/msra_error.png)

## Reference
- \[1\] Danhang Tang, Hyung Jin Chang, Alykhan Tejani, and Tae-Kyun Kim, "[Latent regression forest: Structured estimation of 3d articulated hand posture.](http://www.iis.ee.ic.ac.uk/dtang/cvpr_14.pdf)", Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2014.
- \[2\] Xingyi Zhou, Qingfu Wan, Wei Zhang, Xiangyang Xue, and Yichen Wei, "[Model-based deep hand pose estimation.](http://xingyizhou.xyz/zhou2016model.pdf)", Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence (**IJCAI**), 2016.
- \[3\] Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang, Fei Qiao, and Huazhong Yang, "[Region Ensemble Network: Improving Convolutional Network for Hand Pose Estimation.](https://arxiv.org/pdf/1702.02447.pdf)", Proceedings of the IEEE International Conference on Image Processing (**ICIP**) 2017.
- \[4\] Markus Oberweger, Paul Wohlhart, and Vincent Lepetit, "[Hands deep in deep learning for hand pose estimation.](https://arxiv.org/pdf/1502.06807)", Computer Vision Winter Workshop (**CVWW**) 2015.
- \[5\] Markus Oberweger, Paul Wohlhart, and Vincent Lepetit, "[Training a feedback loop for hand pose estimation.](https://arxiv.org/pdf/1609.09698)", Proceedings of the IEEE International Conference on Computer Vision (**ICCV**) 2015.
- \[6\] Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, and Li Cheng, "[Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups.](https://arxiv.org/pdf/1609.03773)" International Journal of Computer Vision (**IJCV**) 2017.
- \[7\] Hengkai Guo, Guijin Wang, Xinghao Chen, and Cairong Zhang, "[Towards Good Practices for Deep 3D Hand Pose Estimation.](https://arxiv.org/pdf/1707.07248.pdf)" arXiv preprint arXiv:1707.07248 (**arXiv**) 2017.
- \[8\] Xinghao Chen, Guijin Wang, Hengkai Guo, and Cairong Zhang, "[Pose Guided Structured Region Ensemble Network for Cascaded Hand Pose Estimation.](https://arxiv.org/pdf/1708.03416)" arXiv preprint arXiv:1708.03416 (**arXiv**) 2017.
- \[9\] Markus Oberweger, and Vincent Lepetit, "[DeepPrior++: Improving Fast and Accurate 3D Hand Pose Estimation.](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_lepetit/publications/oberweger_iccvw17.pdf)", Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**ICCVW**) 2017.
- \[10\] Chengde Wan, Thomas Probst, Luc Van Gool, and Angela Yao, "[Dense 3D Regression for Hand Pose Estimation.](https://arxiv.org/pdf/1711.08996.pdf)" arXiv preprint arXiv:1707.1711.08996 (**arXiv**) 2017.
- \[11\] Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann, "[3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images](https://drive.google.com/open?id=0B5nUFeZt3D19bzR3NXNURHc0Rkk)", Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2017.
