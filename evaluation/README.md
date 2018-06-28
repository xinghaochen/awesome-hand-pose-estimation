# Evaluations on hand pose estimation

## Description
This project provides codes to evaluate performances of hand pose estimation on several public datasets, including [NYU](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm), [ICVL](https://labicvl.github.io/hand.html), [MSRA](https://github.com/geliuhao/CVPR2016_HandPoseEstimation/issues/4) hand pose dataset. We collect predicted labels of some prior work **_which are available online_** and visualize the performances.

## Evaluation metric
There are two types of evaluation metrics that are widely used for hand pose estimation:

(1) Mean error for each joint

(2) Success rate:
 - The proportion of test frames whose average error falls below a threshold
 - The proportion of test frames whose maximum error falls below a threshold
 - The proportion of all joints whose error falls below a threshold

## Methods and corresponding predicted labels
### ICVL
- LRF \[1\]: CVPR'14, [Predicted labels](https://imperialcollegelondon.app.box.com/s/xivvoc1njhop2wjpt05z5z5ol0gwi0vw)
- DeepModel \[2\]: IJCAI'16, [Predicted labels](http://xingyizhou.xyz/IJCAI16_ICVL.txt)
- Guo-Baseline \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_basic.txt)
- REN-4x6x6 \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_ren_4x6x6.txt)
- REN-9x6x6 \[7\]: JVCI'18, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/icvl_ren_9x6x6.txt)
- Pose-REN \[8\]: NEUCOM'18, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/icvl/arXiv17_ICVL_Pose_REN.txt)
- DenseReg \[10\]: CVPR'18, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/icvl.txt)
- V2V-PoseNet \[12\]: CVPR'18, [Predicted labels](http://cv.snu.ac.kr/research/V2V-PoseNet/ICVL/coordinate/result.txt)

### NYU
- DeepPrior \[4\]: CVWW'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/CVWW15_ICVL_Prior.txt)
- DeepPrior-Refinement \[4\]: CVWW'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/CVWW15_ICVL_Prior-Refinement.txt)
- Feedback \[5\]: CVPR'15, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/ICCV15_NYU_Feedback.txt)
- DeepModel \[2\]: IJCAI'16, [Predicted labels](http://xingyizhou.xyz/IJCAI16_NYU.txt)
- Lie-X \[6\]: IJCV'16, [Predicted labels](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X/lie_hand_jnts_estm_result.txt)
- Guo-Baseline \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_basic.txt)
- REN-4x6x6 \[3\]: ICIP'17, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_ren_4x6x6.txt)
- REN-9x6x6 \[7\]: JVCI'18, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/nyu_ren_9x6x6.txt)
- Pose-REN \[8\]: NEUCOM'18, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/nyu/arXiv17_NYU_Pose_REN.txt)
- DeepPrior++ \[9\]: ICCVW'17, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/3d_hand_pose/ICCVW17_NYU_DeepPrior__.txt)
- DenseReg \[10\]: CVPR'18, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/nyu.txt)
- [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017) \[11\]: CVPR'17, [Predicted labels](https://drive.google.com/file/d/1M1iZyPZ3jU1_KIH0kJKvg1TwolpwLQxy/view?usp=sharing)
- V2V-PoseNet \[12\]: CVPR'18, [Predicted labels](http://cv.snu.ac.kr/research/V2V-PoseNet/NYU/coordinate/result.txt)
- FeatureMapping \[13\]: CVPR'18, [Predicted labels](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Downloads/team_lepetit/FeatureMapping/CVPR18_NYU_DeepPrior___FM.txt.zip)

### MSRA
- REN-9x6x6 \[7\]: JVCI'18, [Predicted labels](https://github.com/guohengkai/region-ensemble-network/blob/master/results/msra_ren_9x6x6.txt)
- Pose-REN \[8\]: NEUCOM'18, [Predicted labels](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation/results/msra/arXiv17_MSRA_Pose_REN.txt)
- DenseReg \[10\]: CVPR'18, [Predicted labels](https://github.com/melonwan/denseReg/blob/master/exp/result/msra.txt)
- [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017) \[11\]: CVPR'17, [Predicted labels](https://drive.google.com/file/d/1M1iZyPZ3jU1_KIH0kJKvg1TwolpwLQxy/view?usp=sharing)

### Notes
- Note that only 14 out of 36 joints are used for evaluation and we use the joints with id [0, 3, 6, 9, 12, 15, 18, 21, 24, 25, 27, 30, 31, 32]. All labels are in the format of (u, v, d) where u and v are pixel coordinates.

- **The code to plot errors over different yaw and pitch angles for MSRA is still under construction and needs further improvement. Stay tuned.**

- For [Lie-X](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X.html), the original predicted labels are in format of (x, y, z) and the order of joints is different. We convert the labels from xyz to uvd and permute the order of joints to keep consistent with other methods (see src/convert_results_xyz2uvd_LieX.py).

- For [DenseReg](https://github.com/melonwan/denseReg), we convert the original predicted labels from xyz to uvd (see src/convert_results_xyz2uvd_denseReg.py).

- Since [DeepPrior[4]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) and [DeepPrior++[9]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) only provide predicted labels of Sequence A (702 frames) for ICVL dataset (totally 1596 frames for two test sequences), we haven't included these method in comparisons for ICVL dataset yet.

- [DeepPrior++[9]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) also provides predicted labels of for MSRA dataset online. However, the results seem to be shuffled so we haven't included these results yet, stay tuned.

- For [3DCNN](https://sites.google.com/site/geliuhaontu/home/cvpr2017), we convert the original predicted labels from xyz to uvd (see src/convert_results_xyz2uvd_3DCNN.py).

- The annotations for MSRA dataset for [V2V-PoseNet](http://cv.snu.ac.kr/research/V2V-PoseNet/MSRA/coordinate/result.txt) are slightly different from prior work so we haven't included its results yet.

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

|Methods|3D Error (mm)|
|------|------|
| DeepPrior [4] | 20.750 |
| DeepPrior-Refine [4] | 19.726 |
| DeepModel [2] |17.036  |
| Feedback [5] |15.973  |
|  Guo_Baseline [3] |14.588 |
|  Lie-X [6] | 14.507 |
|  3DCNN [11] |14.113 |
|  REN-4x6x6 [3] | 13.393  |
|  REN-9x6x6 [7] | 12.694  |
|  DeepPrior++ [9] |12.238 |
|  Pose-REN [8] | 11.811  |
|  DenseReg [10] | 10.214 |
|  V2V-PoseNet [12] |8.419  |
|  FeatureMapping [13] | 7.441  |

### Results on ICVL dataset
![figures/icvl_error_bar.png](figures/icvl_error.png)

|Methods|3D Error (mm)|
|------|------|
|  LRF [1] | 12.578 |
| DeepModel [2] | 11.561 |
|  Guo_Baseline [3] | 8.358 |
|  REN-4x6x6 [3] | 7.628  |
|  REN-9x6x6 [7] | 7.305  |
|  DenseReg [10] | 7.239 |
|  Pose-REN [8] | 6.791  |
|  V2V-PoseNet [12] | 6.284  |

### Results on MSRA dataset
![figures/msra_error_bar.png](figures/msra_error.png)

|Methods|3D Error (mm)|
|------|------|
|  REN-9x6x6 [7] | 9.792  |
|  3DCNN [11] | 9.584  |
|  Pose-REN [8] | 8.649  |
|  DenseReg [10] | 7.234 |

## Reference
- \[1\] "[Latent regression forest: Structured estimation of 3d articulated hand posture.](http://www.iis.ee.ic.ac.uk/dtang/cvpr_14.pdf)", Danhang Tang, Hyung Jin Chang, Alykhan Tejani, and Tae-Kyun Kim, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2014.
- \[2\] "[Model-based Deep Hand Pose Estimation.](http://xingyizhou.xyz/zhou2016model.pdf)", Xingyi Zhou, Qingfu Wan, Wei Zhang, Xiangyang Xue, and Yichen Wei, Proceedings of the Twenty-Fifth International Joint Conference on Artificial Intelligence (**IJCAI**), 2016.
- \[3\] "[Region Ensemble Network: Improving Convolutional Network for Hand Pose Estimation.](https://arxiv.org/pdf/1702.02447.pdf)", Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang, Fei Qiao, and Huazhong Yang, Proceedings of the IEEE International Conference on Image Processing (**ICIP**) 2017.
- \[4\] "[Hands Deep in Deep Learning for Hand Pose Estimation.](https://arxiv.org/pdf/1502.06807)", Markus Oberweger, Paul Wohlhart, and Vincent Lepetit, Computer Vision Winter Workshop (**CVWW**) 2015.
- \[5\] "[Training a Feedback Loop for Hand Pose Estimation.](https://arxiv.org/pdf/1609.09698)", Markus Oberweger, Paul Wohlhart, and Vincent Lepetit, Proceedings of the IEEE International Conference on Computer Vision (**ICCV**) 2015.
- \[6\] "[Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups.](https://arxiv.org/pdf/1609.03773)", Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, and Li Cheng, International Journal of Computer Vision (**IJCV**) 2017.
- \[7\] "[Region Ensemble Network: Towards Good Practices for Deep 3D Hand Pose Estimation.](https://www.sciencedirect.com/science/article/pii/S1047320318300816)", Guijin Wang, Xinghao Chen\*, Hengkai Guo\*, Cairong Zhang, Journal of Visual Communication and Image Representation (**JVCI**) 2018.
- \[8\] "[Pose Guided Structured Region Ensemble Network for Cascaded Hand Pose Estimation.](https://arxiv.org/pdf/1708.03416)", Xinghao Chen, Guijin Wang, Hengkai Guo, and Cairong Zhang, arXiv preprint arXiv:1708.03416 (**Neurocomputing**) 2018.
- \[9\] "[DeepPrior++: Improving Fast and Accurate 3D Hand Pose Estimation.](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_lepetit/publications/oberweger_iccvw17.pdf)", Markus Oberweger, and Vincent Lepetit, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**ICCVW**) 2017.
- \[10\] "[Dense 3D Regression for Hand Pose Estimation.](https://arxiv.org/pdf/1711.08996.pdf)", Chengde Wan, Thomas Probst, Luc Van Gool, and Angela Yao, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2018.
- \[11\] "[3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images](https://drive.google.com/open?id=0B5nUFeZt3D19bzR3NXNURHc0Rkk)", Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2017.
- \[12\] "[V2V-PoseNet: Voxel-to-Voxel Prediction Network for Accurate 3D Hand and Human Pose Estimation from a Single Depth Map](https://arxiv.org/pdf/1711.07399.pdf)", Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2018.
- \[13\] "[Feature Mapping for Learning Fast and Accurate 3D Pose Inference from Synthetic Images](https://arxiv.org/pdf/1712.03904.pdf)", Mahdi Rad, Markus Oberweger, Vincent Lepetit, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (**CVPR**) 2018.
