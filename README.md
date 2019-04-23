# Awesome Hand Pose Estimation [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

A curated list of related resources for hand pose estimation. Feel free to [contribute](#Contribute)!

## Contents
 - [Evaluation](#evaluation)
 - [arXiv Papers](#arxiv-papers)
 - [Journal Papers](#journal-papers)
   - [TPAMI / IJCV](#tpami--ijcv)
   - [Others](#others)
 - [Conference Papers](#conference-papers)
   - 2019: [CVPR](#2019-cvpr), [Others](#2019-others)
   - 2018: [CVPR](#2018-cvpr), [ECCV](#2018-eccv), [Others](#2018-others)
   - 2017: [CVPR](#2017-cvpr), [ICCV](#2017-iccv), [Others](#2017-others)
   - 2016: [CVPR](#2016-cvpr), [ECCV](#2016-eccv), [Others](#2016-others)
   - 2015: [CVPR](#2015-cvpr), [ICCV](#2015-iccv), [Others](#2015-others)
   - 2014: [CVPR](#2014-cvpr), [Others & Before](#2014-others--before)
 - [Theses](#theses)
 - [Datasets](#datasets)
 - [Workshops](#workshops)
 - [Challenges](#challenges)
 - [Other Related Papers](#other-related-papers)

\* indicates equal contribution

## Evaluation
See folder [``evaluation``](./evaluation) to get more details about performance evaluation for hand pose estimation.

## arXiv Papers

##### [\[arXiv:1904.07528\]](https://arxiv.org/abs/1904.07528) Disentangling Pose from Appearance in Monochrome Hand Images. [\[PDF\]](https://arxiv.org/pdf/1904.07528.pdf)
_Yikang Li, Chris Twigg, Yuting Ye, Lingling Tao, Xiaogang Wang_

##### [\[arXiv:1902.09305\]](https://arxiv.org/abs/1902.09305) End-to-end Hand Mesh Recovery from a Monocular RGB Image. [\[PDF\]](https://arxiv.org/pdf/1902.09305.pdf)  [\[Code\]](https://github.com/MandyMo/HAMR)
_Xiong Zhang\*, Qiang Li\*, Wenbo Zhang, Wen Zheng_

##### [\[arXiv:1811.09916\]](https://arxiv.org/abs/1811.09916) Generating Realistic Training Images Based on Tonality-Alignment Generative Adversarial Networks for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1811.09916.pdf)
_Liangjian Chen, Shih-Yao Lin, Yusheng Xie, Hui Tang, Yufan Xue, Xiaohui Xie, Yen-Yu Lin, Wei Fan_

##### [\[arXiv:1811.07123\]](https://arxiv.org/abs/1811.07376) RGB-based 3D Hand Pose Estimation via Privileged Learning with Depth Images. [\[PDF\]](https://arxiv.org/pdf/1811.07376.pdf)
_Shanxin Yuan, Bjorn Stenger, Tae-Kyun Kim_

##### [\[arXiv:1811.07123\]](https://arxiv.org/abs/1811.07123) Explicit Pose Deformation Learning for Tracking Human Poses. [\[PDF\]](https://arxiv.org/pdf/1811.07123.pdf)
_Xiao Sun, Chuankang Li, Stephen Lin_

##### [\[arXiv:1807.00898\]](https://arxiv.org/abs/1807.00898) Model-based Hand Pose Estimation for Generalized Hand Shape with Appearance Normalization. [\[PDF\]](https://arxiv.org/pdf/1807.00898.pdf)
_Jan Wöhlke, Shile Li, Dongheui Lee_

##### [\[arXiv:1705.09606\]](https://arxiv.org/abs/1705.09606) End-to-end Global to Local CNN Learning for Hand Pose Recovery in Depth data. [\[PDF\]](https://arxiv.org/pdf/1705.09606.pdf)
_Meysam Madadi, Sergio Escalera, Xavier Baro, Jordi Gonzalez_

##### [\[arXiv:1704.02224\]](https://arxiv.org/abs/1704.02224) Hand3D: Hand Pose Estimation using 3D Neural Network. [\[PDF\]](https://arxiv.org/pdf/1704.02224.pdf)  [\[Project\]](http://www.idengxm.com/hand3d/index.html)
_Xiaoming Deng\*, Shuo Yang\*, Yinda Zhang\*, Ping Tan, Liang Chang, Hongan Wang_

##### [\[arXiv:1612.00596\]](https://arxiv.org/abs/1612.00596) Learning to Search on Manifolds for 3D Pose Estimation of Articulated Objects. [\[PDF\]](https://arxiv.org/pdf/1612.00596.pdf)
*Yu Zhang, Chi Xu, Li Cheng*

[\[back to top\]](#contents)

## Journal Papers

### TPAMI / IJCV

##### \[2019 TPAMI\] Generalized Feedback Loop for Joint Hand-Object Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1903.10883) [\[Project\]](https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/joint-3d-hand-object-pose-estimation/)
_Markus Oberweger, Paul Wohlhart, Vincent Lepetit_

##### \[2019 TPAMI\] Feature Boosting Network For 3D Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/document/8621059)
_Jun Liu, Henghui Ding, Amir Shahroudy, Ling-Yu Duan, Xudong Jiang, Gang Wang, Alex C. Kot_

##### \[2018 TPAMI\] Opening the Black Box: Hierarchical Sampling Optimization for Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8386667)
_Danhang Tang\*, Qi Ye\*, Shanxin Yuan, Jonathan Taylor, Pushmeet Kohli, Cem Keskin, Tae-Kyun Kim, Jamie Shotton_

##### \[2018 IJCV\] Depth-Based Hand Pose Estimation: Methods, Data, and Challenges. [\[PDF\]](https://link.springer.com/content/pdf/10.1007%2Fs11263-018-1081-7.pdf)  [\[Project\]](http://arrummzen.net/#HandData) [\[Code\]](https://github.com/jsupancic/deep_hand_pose)
*James Steven Supančič III, Grégory Rogez, Yi Yang, Jamie Shotton, Deva Ramanan*

##### \[2018 TPAMI\] Real-time 3D Hand Pose Estimation with 3D Convolutional Neural Networks. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8338122)
_Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann_

##### \[2016 IJCV\] Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups. [\[PDF\]](https://arxiv.org/pdf/1609.03773.pdf) [\[Project\]](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X.html)
*Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, Li Cheng*

##### \[2016 TPAMI\] Latent Regression Forest: Structured Estimation of 3D Hand Poses. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7539555)
*Danhang Tang, Hyung Chang, Alykhan Tejani, Tae-Kyun Kim*

##### \[2016 IJCV\] Capturing Hands in Action using Discriminative Salient Points and Physics Simulation. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf) [\[Project\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/)
*Dimitrios Tzionas, Luca Ballan, Abhilash Srikantha, Pablo Aponte, Marc Pollefeys, Juergen Gall*

##### \[2015 IJCV\] Estimate Hand Poses Efficiently from Single Depth Images. [\[PDF\]](https://web.bii.a-star.edu.sg/~xuchi/pdf/XuEtAl_IJCV15.pdf) [\[Project\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)  [\[Code\]](https://github.com/lzddzh/HandPoseEstimation)
*Chi Xu, Ashwin Nanjappa, Xiaowei Zhang, Li Cheng*

[\[back to top\]](#contents)

### Others

##### \[2018 Neurocomputing\] A CRNN module for hand pose estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0925231218315273#!)
_Zhongxu Hu, Youmin Hu, Jie Liu, Bo Wu, Dongmin Han, Thomas Kurfess_

##### \[2018 IVC\] Large-scale Multiview 3D Hand Pose Dataset. [\[PDF\]](https://arxiv.org/pdf/1707.03742.pdf)  [\[Project\]](http://www.rovit.ua.es/dataset/mhpdataset/)
_Francisco Gomez-Donoso, Sergio Orts-Escolano and Miguel Cazorla_

##### \[2018 TCSVT\] Mask-pose Cascaded CNN for 2D Hand Pose Estimation from Single Color Image. [\[PDF\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.pdf)  [\[Project\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.html)  [\[Code\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.html)
_Yangang Wang, Cong Peng and Yebin Liu_

##### \[2018 IVC\] Top-down model fitting for hand pose recovery in sequences of depth images. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0262885618301513#aep-article-footnote-id1)
_Meysam Madadi, Sergio Escalera, Alex Carruesco, Carlos Andujar, Xavier Baró, Jordi Gonzàlez_

##### \[2018 TCYB\] Context-Aware Deep Spatio-Temporal Network for Hand Pose Estimation from Depth Images. [\[PDF\]](https://arxiv.org/pdf/1810.02994.pdf)
_Yiming Wu, Wei Ji, Xi Li, Gang Wang, Jianwei Yin, Fei Wu_

##### \[2018 IEEE Access\] SHPR-Net: Deep Semantic Hand Pose Regression From Point Clouds. [\[PDF\]](https://ieeexplore.ieee.org/document/8425735/)  [\[Project\]](https://sites.google.com/view/xinghaochen/projects/SHPR-Net)
_Xinghao Chen, Guijin Wang, Cairong Zhang, Tae-Kyun Kim, Xiangyang Ji_

##### \[2018 Neurocomputing\]  Pose Guided Structured Region Ensemble Network for Cascaded Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1708.03416.pdf)  [\[Project\]](https://sites.google.com/view/xinghaochen/projects/Pose-REN)  [\[Code\]](https://github.com/xinghaochen/Pose-REN)
_Xinghao Chen, Guijin Wang, Hengkai Guo, Cairong Zhang_

##### \[2018 PR\]  Learning a deep network with spherical part model for 3D hand pose estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0031320318300839)
_Tzu-Yang Chen, Pai-Wen Ting, Min-Yu Wu, Li-Chen Fu_

##### \[2018 TIP\] Robust 3D Hand Pose Estimation from Single Depth Images using Multi-View CNNs. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8357595)
_Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann_

##### \[2018 JVCI\] Region Ensemble Network: Towards Good Practices for Deep 3D Hand Pose Estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S1047320318300816) [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
_Guijin Wang, Xinghao Chen\*, Hengkai Guo\*, Cairong Zhang_

##### \[2017 TCYB\] Hough Forest with Optimized Leaves for Global Hand Pose Estimation with Arbitrary Postures. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8237190)
*Hui Liang, Junsong Yuan, J. Lee, Liuhao Ge and Daniel Thalmann*

##### \[2017 TCSVT\] Robust RGB-D Hand Tracking Using Deep Learning Priors. [\[PDF\]](http://ieeexplore.ieee.org/abstract/document/7955084/)
*Jordi Sanchez-Riera, Kathiravan Srinivasan, Kai-Lung Hua, Wen-Huang Cheng, M. Anwar Hossain, and Mohammed F. Alhamid*

##### [2017 CVIU] Hand Pose Estimation through Semi-Supervised and Weakly-Supervised Learning. [\[PDF\]](https://arxiv.org/pdf/1511.06728.pdf)
*Natalia Neverova, Christian Wolf, Florian Nebout, Graham Taylor*

##### \[2017 Neurocomputing\] Multi-task, Multi-domain Learning: application to semantic segmentation and pose regression. [\[PDF\]](http://liris.cnrs.fr/christian.wolf/papers/neurocomputing2017.pdf)
*Damien Foururea, Rémi Emonet, Elisa Fromont, Damien Muselet, Natalia Neverova, Alain Trémeaua, Christian Wolf*

##### \[2016 CVIU\] Guided Optimisation through Classification and Regression for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/1-s2.0-s107731421630193x-main.pdf) [\[Project\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### \[2015 TCSVT\] Resolving Ambiguous Hand Pose Predictions by Exploiting Part Correlations. [\[PDF\]](https://ieeexplore.ieee.org/document/6926804/)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

##### \[2014 TMM\] Parsing the Hand in Depth Images. [\[PDF\]](https://ieeexplore.ieee.org/document/6740010) [\[Project\]](https://sites.google.com/site/seraphlh/projects)  [\[Code\]](https://github.com/shrekei/RandomDecisionForest)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

[\[back to top\]](#contents)

## Conference Papers

### 2019 CVPR

##### Disentangling Latent Hands for Image Synthesis and Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1812.01002.pdf)
_Linlin Yang, Angela Yao_

##### Point-to-Pose Voting based Hand Pose Estimation using Residual Permutation Equivariant Layer. [\[PDF\]](https://arxiv.org/pdf/1812.02050.pdf)
_Shile Li, Dongheui Lee_

##### H+O: Unified Egocentric Recognition of 3D Hand-Object Poses and Interactions. [\[PDF\]](https://arxiv.org/pdf/1904.05349)  *(Oral)*
_Bugra Tekin, Federica Bogo, Marc Pollefeys_

##### Self supervised 3D hand pose estimation. [\[PDF\]](http://www.vision.ee.ethz.ch/~wanc/papers/cvpr2019.pdf) [\[Code\]](https://github.com/melonwan/sphereHand) *(Oral)*
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### CrossInfoNet: Multi-Task Information Sharing Based Hand Pose Estimation. \[PDF\] [\[Code\]](https://github.com/dumyy/handpose)
_Kuo Du, Xiangbo Lin, Yi Sun, Xiaohong Ma_

##### Expressive Body Capture: 3D Hands, Face, and Body from a Single Image.  [\[PDF\]](https://arxiv.org/pdf/1904.05866)  [\[Project\]](https://smpl-x.is.tue.mpg.de/) *(Oral)*
_Georgios Pavlakos\*, Vasileios Choutas\*, Nima Ghorbani, Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas, Michael J. Black_

##### Learning joint reconstruction of hands and manipulated objects. [\[PDF\]](https://ps.is.tuebingen.mpg.de/uploads_file/attachment/attachment/499/obman.pdf) [\[Code\]](https://github.com/hassony2/manopth)  [\[Project\]](https://www.di.ens.fr/willow/research/obman/)
_Yana Hasson, Gül Varol, Dimitris Tzionas, Igor Kalevatykh, Michael J. Black, Ivan Laptev, and Cordelia Schmid_

##### 3D Hand Shape and Pose Estimation from a Single RGB Image. [\[PDF\]](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxnZWxpdWhhb250dXxneDo3ZjE0ZjY3OWUzYjJkYjA2) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2019) [\[Code\]](https://github.com/geliuhao/3DHandShapePosefromRGB) *(Oral)*
_Liuhao Ge, Zhou Ren, Yuncheng Li, Zehao Xue, Yingying Wang, Jianfei Cai, Junsong Yuan_

##### 3D Hand Shape and Pose from Images in the Wild. [\[PDF\]](https://arxiv.org/pdf/1902.03451.pdf)  [\[Code\]](https://github.com/boukhayma/3dhand) *(Oral)*
_Adnane Boukhayma, Rodrigo de Bem, Philip H.S. Torr_

##### Pushing the Envelope for RGB-based Dense 3D Hand Pose Estimation via Neural Rendering. [\[PDF\]](https://arxiv.org/pdf/1904.04196)
_Seungryul Baek, Kwang In Kim, Tae-Kyun Kim_

##### Monocular Total Capture: Posing Face, Body, and Hands in the Wild. [\[PDF\]](https://arxiv.org/pdf/1812.01598.pdf) [\[Project\]](http://domedb.perception.cs.cmu.edu/monototalcapture.html) *(Oral)*
_Donglai Xiang, Hanbyul Joo, Yaser Sheikh_

[\[back to top\]](#contents)

### 2019 Others

##### [2019 ICRA] Vision-based Teleoperation of Shadow Dexterous Hand using End-to-End Deep Neural Network. [\[PDF\]](https://arxiv.org/pdf/1809.06268.pdf) [\[Code\]](https://github.com/TAMS-Group/TeachNet_Teleoperation)
_Shuang Li\*, Xiaojian Ma\*, Hongzhuo Liang, Michael Görner, Philipp Ruppel, Bing Fang, Fuchun Sun, Jianwei Zhang_

##### [2019 WACV] MURAUER: Mapping Unlabeled Real Data for Label AUstERity. [\[PDF\]](https://poier.github.io/murauer/documents/poier2019wacv_selfpublishing.pdf) [\[Project\]](https://poier.github.io/murauer/) [\[Code\]](https://github.com/poier/murauer)
_Georg Poier, Michael Opitz, David Schinagl and Horst Bischof_

[\[back to top\]](#contents)

### 2018 ECCV

##### HandMap: Robust Hand Pose Estimation via Intermediate Dense Guidance Map Supervision. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Xiaokun_Wu_HandMap_Robust_Hand_ECCV_2018_paper.pdf)  [\[Project\]](https://xkunwu.github.io/research/18HandPose/18HandPose)  [\[Code\]](https://github.com/xkunwu/depth-hand)
_Xiaokun Wu, Daniel Finnegan, Eamonn O'Neill, Yongliang Yang_

##### HBE: Hand Branch Ensemble network for real time 3D hand pose estimation.  [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Yidan_Zhou_HBE_Hand_Branch_ECCV_2018_paper.pdf)
_Yidan Zhou, Jian Lu, Kuo Du, Xiangbo Lin, Yi Sun, Xiaohong Ma_

##### Point-to-Point Regression PointNet for 3D Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Liuhao_Ge_Point-to-Point_Regression_PointNet_ECCV_2018_paper.pdf)
_Liuhao Ge, Zhou Ren, Junsong Yuan_

##### Weakly-supervised 3D Hand Pose Estimation from Monocular RGB Images. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Yujun_Cai_Weakly-supervised_3D_Hand_ECCV_2018_paper.pdf) *(Oral)*
_Yujun Cai, Liuhao Ge, Jianfei Cai, Junsong Yuan_

##### Joint 3D tracking of a deformable object in interaction with a hand. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Aggeliki_Tsoli_Joint_3D_tracking_ECCV_2018_paper.pdf)  [\[Project\]](https://www.ics.forth.gr/cvrl/deformable_interaction/)
_Aggeliki Tsoli, Antonis A. Argyros_

##### Occlusion-aware Hand Pose Estimation Using Hierarchical Mixture Density Network. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Qi_Ye_Occlusion-aware_Hand_Pose_ECCV_2018_paper.pdf)  *(Oral)*
_Qi Ye, Tae-Kyun Kim_

##### Hand Pose Estimation via Latent 2.5D Heatmap Regression. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Umar_Iqbal_Hand_Pose_Estimation_ECCV_2018_paper.pdf)
_Umar Iqbal, Pavlo Molchanov, Thomas Breuel, Juergen Gall, Jan Kautz_

##### [Hands18 Workshop] Adapting Egocentric Visual Hand Pose Estimation Towards a Robot-Controlled Exoskeleton. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-11024-6_16)
_Gerald Baulig, Thomas Gulde, Cristobal Curio_

##### [Hands18 Workshop] Estimating 2D Multi-Hand Poses From Single Depth Images. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-11024-6_17)
_Le Duan, Minmin Shen, Song Cui, Zhexiao Guo, Oliver Deussen_

##### [Hands18 Workshop] Task-Oriented Hand Motion Retargeting for Dexterous Manipulation Imitation. [\[PDF\]](https://arxiv.org/pdf/1810.01845.pdf) [\[Project\]](https://daphneantotsiou.github.io/task-oriented-retargeting.html)
_Dafni Antotsiou, Guillermo Garcia-Hernando, Tae-Kyun Kim_

[\[back to top\]](#contents)

### 2018 CVPR

##### First-Person Hand Action Benchmark with RGB-D Videos and 3D Hand Pose Annotations. [\[PDF\]](https://arxiv.org/pdf/1704.02463.pdf) [\[Project\]](https://guiggh.github.io/publications/first-person-hands/)  [\[Code\]](https://github.com/guiggh/hand_pose_action)
*Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, Tae-Kyun Kim*


##### Learning Pose Specific Representations by Predicting Different Views. [\[PDF\]](https://arxiv.org/pdf/1804.03390.pdf)  [\[Project\]](https://poier.github.io/PreView/)  [\[Code\]](https://github.com/poier/PreView)
_Georg Poier, David Schinagl, Horst Bischof_

##### Hand PointNet: 3D Hand Pose Estimation using Point Sets. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Ge_Hand_PointNet_3D_CVPR_2018_paper.pdf)  [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2018) [\[Code\]](https://sites.google.com/site/geliuhaontu/HandPointNet.zip?attredirects=0&d=1) *(Spotlight)*
_Liuhao Ge, Yujun Cai, Junwu Weng, Junsong Yuan_

##### Dense 3D Regression for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1711.08996.pdf)  [\[Code\]](https://github.com/melonwan/denseReg)
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### Cross-modal Deep Variational Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1803.11404) [\[Project\]](https://ait.ethz.ch/projects/2018/vae_hands/) [\[Code\]](https://github.com/spurra/vae-hands-3d) *(Spotlight)*
_Adrian Spurr, Jie Song, Seonwook Park, Otmar Hilliges_

##### Feature Mapping for Learning Fast and Accurate 3D Pose Inference from Synthetic Images. [\[PDF\]](https://arxiv.org/pdf/1712.03904.pdf)  [\[Project\]](https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/feature-mapping/)
_Mahdi Rad, Markus Oberweger, Vincent Lepetit_

##### GANerated Hands for Real-Time 3D Hand Tracking from Monocular RGB. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018.pdf) [\[Supp\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018_Supp.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/) *(Spotlight)*
_Franziska Mueller, Florian Bernard, Oleksandr Sotnychenko, Dushyant Mehta, Srinath Sridhar, Dan Casas, Christian Theobalt_


##### V2V-PoseNet: Voxel-to-Voxel Prediction Network for Accurate 3D Hand and Human Pose Estimation from a Single Depth Map. [\[PDF\]](https://arxiv.org/pdf/1711.07399.pdf) [\[Code\]](https://github.com/mks0601/V2V-PoseNet_RELEASE)
_Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee_

##### Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals. [\[PDF\]](https://arxiv.org/pdf/1712.03917.pdf) *(Spotlight)*
_Shanxin Yuan, Guillermo Garcia-Hernando, Bjorn Stenger, Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee, Pavlo Molchanov, Jan Kautz, Sina Honari, Liuhao Ge, Junsong Yuan, Xinghao Chen, Guijin Wang, Fan Yang, Kai Akiyama, Yang Wu, Qingfu Wan, Meysam Madadi, Sergio Escalera, Shile Li, Dongheui Lee, Iason Oikonomidis, Antonis Argyros, Tae-Kyun Kim_

##### Augmented skeleton space transfer for depth-based hand pose estimation. [\[PDF\]](https://arxiv.org/pdf/1805.04497.pdf) *(Oral)*
_Seungryul Baek, Kwang In Kim, Tae-Kyun Kim_

##### [\[3D HUMANS Workshop\]](https://project.inria.fr/humans2018/) Monocular RGB Hand Pose Inference From Unsupervised Refinable Nets. [\[PDF\]](http://openaccess.thecvf.com/CVPR2018_workshops/content_CVPR_2018/papers/w17/Dibra_Monocular_RGB_Hand_CVPR_2018_paper.pdf)
_Endri Dibra, Silvan Melchior, Ali Balkis, Thomas Wolf, Cengiz Oztireli, Markus Gross_

[\[back to top\]](#contents)

### 2018 Others

##### [2018 ACCV] Hand Pose Estimation based on 3D Residual Network with Data Padding and Skeleton Steadying. \[PDF\]
_Pai-Wen Ting, En-Te Chou, Ya-Hui Tang, Li-Chen Fu_

##### [2018 ACCV] Partially Occluded Hands: A challenging new dataset for single-image hand pose estimation. \[PDF\] [\[Project\]](http://occludedhands.com/)  *(Oral)*
_Battushig Myanganbayar, Cristina Mata, Gil Dekel, Boris Katz, Guy Ben-Yosef, Andrei Barbu_

##### [2018 ACCV] Domain Transfer for 3D Pose Estimation from Color Images without Manual Annotations. [\[PDF\]](https://arxiv.org/pdf/1810.03707.pdf)  *(Oral)*
_Mahdi Rad, Markus Oberweger, Vincent Lepetit_

##### [2018 PCM] Hand Pose Estimation with Attention-and-Sequence Network. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_51)
_Tianping Hu\*, Wenhai Wang\*, Tong Lu_

##### [2018 PCM] Mutiple Transfer Net with Region Ensemble for Deep Hand Pose Estimation. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_58)
_Haoqian Wang, Da Li, Xingzheng Wang_

##### [2018 ICPR] Local Regression Based Hourglass Network for Hand Pose Estimation from a Single Depth Image. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8545460)
_Jia Li, Zengfu Wang_

##### [2018 ICPR] Dynamic Projected Segmentation Networks for Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8546330)
_Yunlong Che, Yue Qi_

##### [2018 3DV] DeepHPS: End-to-end Estimation of 3D Hand Pose and Shape by Learning from Synthetic Depth. [\[PDF\]](https://arxiv.org/pdf/1808.09208.pdf)
_Jameel Malik, Ahmed Elhayek, Fabrizio Nunnari, Kiran Varanasi, Kiarash Tamaddon, Alexis Heloir, Didier Stricker_

##### [2018 ICIP] Networks Effectively Utilizing 2D Spatial Information for Accurate 3D Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8451509/)
_Baoen Liu, Shiliang Huang, Zhongfu Ye_

##### [2018 ICIP] On the Fusion of RGB and Depth Information For Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/document/8451022/) [\[Code\]](https://github.com/ekazakos/fusenet-hand-pose)
_Evangelos Kazakos, Christophoros Nikou, Ioannis Kakadiaris_

##### [2018 ICIP] Fast Lifting for 3D Hand Pose Estimation in AR/VR Applications. [\[PDF\]](https://drive.google.com/file/d/1kbNSb0ySAkhpQ6ntxPhs0wPvFDbsGu8v/view)
_Onur Guleryuz, Christine Kaeser-Chen_

##### [2018 BMVC] Structure-Aware 3D Hourglass Network for Hand Pose Estimation from Single Depth Image. [\[PDF\]](http://bmvc2018.org/papers/1133.pdf)
_Fuyang Huang, Ailing Zeng, Minhao Liu, Jing Qin, Qiang Xu_

##### [2018 BMVC] 3D Hand Pose Estimation using Simulation and Partial-Supervision with a Shared Latent Space. [\[PDF\]](https://arxiv.org/pdf/1807.05380.pdf) [\[Code\]](https://github.com/masabdi/LSPS) *(Oral)*
_Masoud Abdi, Ehsan Abbasnejad, Chee Peng Lim, Saeid Nahavandi_

##### [2018 FG] Kinematic Constrained Cascaded Autoencoder for Real-time Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8373810/)
_Yushun Lin, Xiujuan Chai, Xilin Chen_

##### [2018 WACV] Using a single RGB frame for real time 3D hand pose estimation in the wild. [\[PDF\]](https://arxiv.org/pdf/1712.03866.pdf)  [\[Project\]](http://users.ics.forth.gr/~argyros/res_rgbmonohand.html)
_Paschalis Panteleris, Iason Oikonomidis, Antonis Argyros_

[\[back to top\]](#contents)

### 2017 ICCV
##### Learning to Estimate 3D Hand Pose from Single RGB Images. [\[PDF\]](https://arxiv.org/pdf/1705.01389.pdf)  [\[Project\]](https://lmb.informatik.uni-freiburg.de/projects/hand3d/)   [\[Code\]](https://github.com/lmb-freiburg/hand3d)
_Christian Zimmermann, Thomas Brox_

##### Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/)
*Franziska Mueller, Dushyant Mehta, Oleksandr Sotnychenko, Srinath Sridhar, Dan Casas, Christian Theobalt*

##### Robust Hand Pose Estimation during the Interaction with an Unknown Object. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Robust_Hand_Pose_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Robust_Hand_Pose_ICCV_2017_supplemental.pdf) [\[Project\]](https://engineering.purdue.edu/cdesign/wp/robust-hand-pose-estimation-during-the-interaction-with-an-unknown-object/)
*Chiho Choi, Sang Ho Yoon, Chin-Ning Chen, Karthik Ramani*

##### Learning Hand Articulations by Hallucinating Heat Distribution. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Learning_Hand_Articulations_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Learning_Hand_Articulations_ICCV_2017_supplemental.pdf)  [\[Project\]](https://engineering.purdue.edu/cdesign/wp/learning-hand-articulations-by-hallucinating-heat-distribution/)
*Chiho Choi, Sangpil Kim, Karthik Ramani*

##### Low-Dimensionality Calibration through Local Anisotropic Scaling for Robust Hand Model Personalization. [\[PDF\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/index.php) [\[Code\]](https://github.com/edoRemelli/hadjust)
_Edoardo Remelli*, Anastasia Tkach*, Andrea Tagliasacchi, Mark Pauly_

##### [Hands17 Workshop] Back to RGB: 3D tracking of hands and hand-object interactions based on short-baseline stereo. [\[PDF\]](https://arxiv.org/pdf/1705.05301.pdf)
_Paschalis Panteleris, Antonis Argyros_

##### [Hands17 Workshop] DeepPrior++: Improving Fast and Accurate 3D Hand Pose Estimation. [\[PDF\]](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_lepetit/publications/oberweger_iccvw17.pdf) [\[Project\]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) [\[Code\]](https://github.com/moberweger/deep-prior-pp)
*Markus Oberweger and Vincent Lepetit*

##### [Hands17 Workshop] Hand Pose Estimation Using Deep Stereovision and Markov-chain Monte Carlo. [\[PDF\]](http://openaccess.city.ac.uk/18087/1/BasaruICCVW2017_MCMC.pdf)
*Rilwan Remilekun Basaru, Chris Child, Eduardo Alonso, Greg Slabaugh*

[\[back to top\]](#contents)

### 2017 CVPR
##### Hand Keypoint Detection in Single Images using Multiview Bootstrapping. [\[PDF\]](https://arxiv.org/pdf/1704.07809) [\[Project\]](http://www.cs.cmu.edu/~tsimon/projects/mvbs.html) [\[Code\]](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
*Tomas Simon, Hanbyul Joo, Iain Matthews, Yaser Sheikh*

##### Crossing Nets: Combining GANs and VAEs with a Shared Latent Space for Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wan_Crossing_Nets_Combining_CVPR_2017_paper.pdf) [\[Code\]](https://github.com/melonwan/crossingNet)
*Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao*

##### Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis. [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)
_Shanxin Yuan\*, Qi Ye\*, Bjorn Stenger, Siddhand Jain, Tae-Kyun Kim_

##### 3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Ge_3D_Convolutional_Neural_CVPR_2017_paper.pdf) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2017)
*Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann*

[\[back to top\]](#contents)

### 2017 Others

##### [2017 3DV] Simultaneous Hand Pose and Skeleton Bone-Lengths Estimation from a Single Depth Image. [\[PDF\]](https://arxiv.org/pdf/1712.03121.pdf)
_Jameel Malik, Ahmed Elhayek, Didier Stricker_

##### [2017 3DV] How to Refine 3D Hand Pose Estimation from Unlabelled Depth Data? [\[PDF\]](https://graphics.ethz.ch/~edibra/Publications/How%20to%20Refine%203D%20Hand%20Pose%20Estimation%20from%20Unlabelled%20Depth%20Data.pdf)
_Endri Dibra\*, Thomas Wolf\*, Cengiz Öztireli, Markus Gross_

##### [2017 ICIP] Region Ensemble Network: Improving Convolutional Network for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1702.02447.pdf)  [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
*Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang, Fei Qiao, Huazhong Yang*

##### [2017 ICIP] A Hand Pose Tracking Benchmark from Stereo Matching. [\[PDF\]](http://www.cs.cityu.edu.hk/~jianbjiao2/pdfs/icip.pdf)  [\[Project\]](https://sites.google.com/site/zhjw1988/)
*Jiawei Zhang, Jianbo Jiao, Mingliang Chen, Liangqiong Qu, Xiaobin Xu, and Qingxiong Yang*

##### [2017 SIGGRAPH Asia] Articulated distance fields for ultra-fast tracking of hands interacting. [\[PDF\]](https://dl.acm.org/citation.cfm?id=3130853)
_Jonathan Taylor\*, Vladimir Tankovich\*, Danhang Tang\*, Cem Keskin\*, David Kim, Philip Davidson, Adarsh Kowdle, Shahram Izadi_

##### [2017 SIGGRAPH Asia] Online Generative Model Personalization for Hand Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2017/HOnline/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2017/HOnline/index.php)
_Anastasia Tkach\*, Andrea Tagliasacchi\*, Edoardo Remelli, Mark Pauly, Andrew Fitzgibbon_

##### [2017 SIGGRAPH Asia] Embodied Hands: Modeling and Capturing Hands and Bodies Together. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/392/Embodied_Hands_SiggraphAsia2017.pdf)  [\[Project\]](http://ps.is.tue.mpg.de/publications/embodiedhands)
_Javier Romero\*, Dimitrios Tzionas\* and Michael J. Black_

##### [2017 BMVC] Hand Pose Learning: Combining Deep Learning and Hierarchical Refinement for 3D Hand Pose Estimation. [\[PDF\]](https://www.dropbox.com/s/3y96pnutxum3p4v/0569.pdf?dl=1)
*Min-Yu Wu, Ya Hui Tang, Pai-Wei Ting and Li-Chen Fu*

##### [2017 BMVC] Generative 3D Hand Tracking with Spatially Constrained Pose Sampling. [\[PDF\]](http://users.ics.forth.gr/~argyros/mypapers/2017_09_BMVC_RDSRoditak.pdf) [\[Project\]](http://users.ics.forth.gr/~argyros/res_handRDS.html)
*Konstantinos Roditakis, Alexandros Makris and Antonis Argyros*

##### [2017 ICRA] Learning a deep network with spherical part model for 3D hand pose estimation. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7989303)
*Tzu-Yang Chen, Pai-Wen Ting, Min-Yu Wu, Li-Chen Fu*

##### [2017 FG] Occlusion aware hand pose recovery from sequences of depth images. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961746) [\[Slide\]](http://sergioescalera.com/wp-content/uploads/2017/06/FG2017Hand.pdf)
*Meysam Madadi, Sergio Escalera, Alex Carruesco Llorens, Carlos Andujar, Xavier Baro, Jordi Gonzalez*

##### [2017 FG] 3D Hand-Object Pose Estimation from Depth with Convolutional Neural Networks. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961770) [\[Project\]](http://www.cs.man.ac.uk/~goudied/research.html)
*Duncan Goudie, Aphrodite Galata*

[\[back to top\]](#contents)

### 2016 ECCV
##### Spatial Attention Deep Net with Partial PSO for Hierarchical Hybrid Hand Pose Estimation. [\[PDF\]](https://labicvl.github.io/docs/pubs/Qi_Shanxin_ECCV_2016.pdf) [\[Project\]](https://sites.google.com/site/qiyeincv/home/eccv2016)
_Qi Ye\*, Shanxin Yuan\*, Tae-Kyun Kim_

##### Hand Pose Estimation from Local Surface Normals. [\[PDF\]](http://www.vision.ee.ethz.ch/~yaoa/pdfs/wan_eccv16.pdf)
*Chengde Wan, Angela Yao, and Luc Van Gool*

##### Real-time Joint Tracking of a Hand Manipulating an Object from RGB-D Input. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/content/RealtimeHO_ECCV2016.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/)
*Srinath Sridhar, Franziska Mueller, Michael Zollhöfer, Dan Casas, Antti Oulasvirta, Christian Theobalt*

[\[back to top\]](#contents)

### 2016 CVPR
##### Robust 3D Hand Pose Estimation in Single Depth Images: From Single-View CNN to Multi-View CNNs. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2016/papers/Ge_Robust_3D_Hand_CVPR_2016_paper.pdf) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2016) [\[Code\]](https://github.com/geliuhao/CVPR2016_HandPoseEstimation)
*Liuhao Ge, Hui Liang, Junsong Yuan, Daniel Thalmann*

##### DeepHand: Robust Hand Pose Estimation by Completing a Matrix Imputed With Deep Features.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Sinha_DeepHand_Robust_Hand_CVPR_2016_paper.pdf)[\[Project\]](https://engineering.purdue.edu/cdesign/wp/deephand-robust-hand-pose-estimation/)
_Ayan Sinha\*, Chiho Choi\*, Karthik Ramani_

##### Efficiently Creating 3D Training Data for Fine Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvpr16.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/semi-auto-anno)
*Markus Oberweger, Gernot Riegler, Paul Wohlhart, Vincent Lepetit*

##### Fits Like a Glove: Rapid and Reliable Hand Shape Personalization.  [\[PDF\]](http://www.samehkhamis.com/tan-cvpr2016.pdf) [\[Project\]](http://campar.in.tum.de/Main/DavidTan)
*David Joseph Tan, Thomas Cashman, Jonathan Taylor, Andrew Fitzgibbon, Daniel Tarlow, Sameh Khamis, Shahram Izadi, Jamie Shotton*

[\[back to top\]](#contents)

### 2016 Others

##### [2016 NIPS] DISCO Nets : Dissimilarity Coefficient Networks. [\[PDF\]](http://www.robots.ox.ac.uk/~diane/DISCONET_camera_ready.pdf) [\[Project\]](http://www.robots.ox.ac.uk/~diane/DiscoNets.html) [\[Code\]](https://github.com/oval-group/DISCONets)
*Diane Bouchacourt, M. Pawan Kumar, Sebastian Nowozin*

##### \[2016 ACCV\] Hand Pose Regression via A Classification-guided Approach. [\[PDF\]](http://staff.ustc.edu.cn/~juyong/Papers/HandTracking-2016.pdf)
*Hongwei Yang, Juyong Zhang*

##### \[2016 ICPR\] Deep learning for integrated hand detection and pose estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/7899702/)
*Tzu-Yang Chen, Min-Yu Wu, Yu-Hsun Hsieh, Li-Chen Fu*

##### \[2016 ICPR\] Depth-based 3D hand pose tracking. [\[PDF\]](http://ieeexplore.ieee.org/abstract/document/7900051)
*Kha Gia Quach, Chi Nhan Duong, Khoa Luu, and Tien D. Bui.*

##### \[2016 IJCAI\] Model-based Deep Hand Pose Estimation. [\[PDF\]](http://xingyizhou.xyz/zhou2016model.pdf) [\[Project\]](http://xingyizhou.xyz/) [\[Code\]](https://github.com/tenstep/DeepModel)
*Xingyi Zhou, Qingfu Wan, Wei Zhang, Xiangyang Xue, Yichen Wei*

##### \[2016 SIGGRAPH\] Efficient and precise interactive hand tracking through joint, continuous optimization of pose and correspondences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/SIGGRAPH2016-SmoothHandTracking.pdf)
*Jonathan Taylor et al.*

##### \[2016 SIGGRAPH Asia\] Sphere-Meshes for Real-Time Hand Modeling and Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2016/HModel/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2016/HModel/index.php) [\[Code\]](https://github.com/OpenGP/hmodel)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

[\[back to top\]](#contents)

### 2015 ICCV
##### Training a Feedback Loop for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_iccv15.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### Opening the Black Box: Hierarchical Sampling Optimization for Estimating Human Hand Pose.  [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_ICCV_2015.pdf)
*Danhang Tang, Jonathan Taylor, Pushmeet Kohli, Cem Keskin, Tae-Kyun Kim, Jamie Shotton*

##### Depth-based hand pose estimation: data, methods, and challenges. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Supancic_Depth-Based_Hand_Pose_ICCV_2015_paper.pdf) [\[Project\]](http://arrummzen.net/#HandData) [\[Code\]](https://github.com/jsupancic/deep_hand_pose)
*James Supancic III, Deva Ramanan, Gregory Rogez, Yi Yang, Jamie Shotton*

##### 3D Hand Pose Estimation Using Randomized Decision Forest with Segmentation Index Points. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Li_3D_Hand_Pose_ICCV_2015_paper.pdf)
*Peiyi Li, Haibin Ling*

##### A collaborative filtering approach to real-time hand pose estimation. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2015/08/iccv_2015_hand_pose_estimation.pdf) [\[Project\]](https://engineering.purdue.edu/cdesign/wp/a-collaborative-filtering-approach-to-real-time-hand-pose-estimation/)
*Chiho Choi, Ayan Sinha, Joon Hee Choi, Sujin Jang, Karthik Ramani*

##### Lending A Hand: Detecting Hands and Recognizing Activities in Complex Egocentric Interactions. [\[PDF\]](http://homes.sice.indiana.edu/sbambach/papers/iccv-egohands.pdf)
*Sven Bambach, Stefan Lee, David Crandall, Chen Yu*

##### Understanding Everyday Hands in Action from RGB-D Images. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Rogez_Understanding_Everyday_Hands_ICCV_2015_paper.pdf)
*Gregory Rogez, James Supancic III, Deva Ramanan*

[\[back to top\]](#contents)

### 2015 CVPR
##### Cascaded Hand Pose Regression.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf)
*Xiao Sun, Yichen Wei, Shuang Liang, Xiaoou Tang, and Jian Sun*

##### Fast and Robust Hand Tracking Using Detection-Guided Optimization. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/content/FastHandTracker_CVPR2015.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/)
*Srinath Sridhar, Franziska Mueller, Antti Oulasvirta, Christian Theobalt*

##### Learning an Efficient Model of Hand Shape Variation from Depth Images. [\[PDF\]](http://www.samehkhamis.com/khamis-cvpr2015.pdf)
*Sameh Khamis, Jonathan Taylor, Jamie Shotton, Cem Keskin, Shahram Izadi, Andrew Fitzgibbon*

[\[back to top\]](#contents)

### 2015 Others

##### \[2015 BMVC\] Hybrid One-Shot 3D Hand Pose Estimation by Exploiting Uncertainties. [\[PDF\]](https://arxiv.org/pdf/1510.08039.pdf) [\[Project\]](https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/hybridhpe/)
*Georg Poier, Konstantinos Roditakis, Samuel Schulter, Damien Michel, Horst Bischof and Antonis A. Argyros*

##### \[2015 BMVC\] Rule of Thumb: Deep Derotation for Improved Fingertip Detection. [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf) [\[Project\]](http://www.cs.technion.ac.il/~twerd/HandNet/)
*Aaron Wetzler, Ron Slossberg and Ron Kimmel*

##### \[2015 CHI\] Accurate, Robust, and Flexible Real-time Hand Tracking. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/publication/accurate-robust-and-flexible-real-time-hand-tracking/)
*Toby Sharp, Cem Keskin, Duncan Robertson, Jonathan Taylor, Jamie Shotton, David Kim, Christoph Rhemann, Ido Leichter, Alon Vinnikov, Yichen Wei, Daniel Freedman, Pushmeet Kohli, Eyal Krupka, Andrew Fitzgibbon, Shahram Izadi*

##### \[2015 CVWW\] Hands Deep in Deep Learning for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvww15.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/deep-prior)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### \[2015 FG\] Combining Discriminative and Model Based Approaches for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/final_fg2015.pdf) [\[Project\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### \[2015 SGP\] Robust Articulated-ICP for Real-Time Hand Tracking. [\[PDF\]](http://gfx.uvic.ca/pubs/2015/htrack//paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2015/Htrack_ICP/index.php) [\[Code\]](https://github.com/OpenGP/htrack)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

[\[back to top\]](#contents)

### 2014 CVPR
##### Realtime and robust hand tracking from depth. [\[PDF\]](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/yichenw-cvpr14_handtracking.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/people/yichenw/)
*Chen Qian, Xiao Sun, Yichen Wei, Xiaoou Tang and Jian Sun*

##### Latent regression forest: Structured estimation of 3d articulated hand posture. [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_CVPR_2014.pdf) [\[Project\]](https://labicvl.github.io/hand.html)
*Danhang Tang, Hyung Jin Chang, Alykhan Tejani, T-K. Kim*

##### User-specific hand modeling from monocular depth sequences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CVPR2014-UserSpecificHandModeling.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/publication/user-specific-hand-modeling-from-monocular-depth-sequences/)
*Jonathan Taylor, Richard Stebbing, Varun Ramakrishna, Cem Keskin, Jamie Shotton, Shahram Izadi, Aaron Hertzmann, Andrew Fitzgibbon*

##### Evolutionary Quasi-random Search for Hand Articulations Tracking. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Oikonomidis_Evolutionary_Quasi-random_Search_2014_CVPR_paper.pdf) [\[Project\]](http://users.ics.forth.gr/~oikonom/pb/publications)
*Iason Oikonomidis, Manolis IA Lourakis, Antonis A Argyros*

[\[back to top\]](#contents)

### 2014 Others & Before
##### \[2014 SIGGRAPH\] Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks. [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf) [\[Project\]](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm)
*Jonathan Tompson, Murphy Stein, Yann Lecun and Ken Perlin*

##### \[2013 ICCV\] Real-time Articulated Hand Pose Estimation using Semi-supervised Transductive Regression Forests. [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_ICCV_2013.pdf) [\[Project\]](https://labicvl.github.io/hand.html)
*Danhang Tang, Tsz Ho Yu and T-K. Kim*

##### \[2013 ICCV\] Interactive Markerless Articulated Hand Motion Tracking Using RGB and Depth Data. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/)
*Srinath Sridhar, Antti Oulasvirta, Christian Theobalt*

##### \[2013 ICCV\] Efficient Hand Pose Estimation from a Single Depth Image. [\[PDF\]](http://web.bii.a-star.edu.sg/~xuchi/pdf/iccv2013.pdf) [\[Project\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)
*Chi Xu, Li Cheng*

##### \[2012 ECCV\] Motion Capture of Hands in Action using Discriminative Salient Points. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/76/jgall_handcapture_eccv12.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/btgg12)
*Ballan, L. and Taneja, A. and Gall, J. and van Gool, L. and Pollefeys, M.*

##### \[2012 ECCV\] Hand pose estimation and hand shape classification using multi-layered randomized decision forests.
*Cem KeskinFurkan, KıraçYunus Emre, KaraLale Akarun*

##### \[2011 CVPRW\] Real Time Hand Pose Estimation using Depth Sensors. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf)
*Cem Keskin, Furkan Kırac, Yunus Emre Kara, Lale Akarun*

##### \[2011 BMVC\] Efficient Model-based 3D Tracking of Hand Articulations using Kinect. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf) [\[Project\]](http://users.ics.forth.gr/~argyros/research/kinecthandtracking.htm) [\[Code\]](https://github.com/FORTH-ModelBasedTracker/HandTracker)
*Iason Oikonomidis, Nikolaos Kyriazis, Antonis A. Argyros*

[\[back to top\]](#contents)

## Theses

##### \[2018\] Articulated Human Pose Estimation in Unconstrained Images and Videos. [\[PDF\]](http://hss.ulb.uni-bonn.de/2018/5292/5292.pdf)
*Umar Iqbal, University of Bonn*

##### \[2018\] Real-Time Generative Hand Modeling and Tracking. [\[PDF\]](https://infoscience.epfl.ch/record/256674/files/EPFL_TH8573.pdf)
*Anastasia Tkach, EPFL*

##### \[2018\] Recovery of the 3D Virtual Human: Monocular Estimation of 3D Shape and Pose with Data Driven Priors. [\[PDF\]](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/266852/Endri_Dibra_Thesis_Final.pdf?sequence=3&isAllowed=y)  [\[Project\]](https://www.research-collection.ethz.ch/handle/20.500.11850/266852)
*[Endri Dibra](https://graphics.ethz.ch/~edibra/), ETH Zürich*

##### \[2017\] Human Segmentation, Pose Estimation and Applications. [\[PDF\]](http://sergioescalera.com/wp-content/uploads/2017/10/MeysamPhDv2.pdf) [\[Slides\]](http://sergioescalera.com/wp-content/uploads/2017/10/Thesis-presentation.pdf)
*Meysam Madadi, Universitat Autònoma de Barcelonato*

##### \[2017\] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/tzionas-thesis-phd)
*[Dimitrios Tzionas](http://ps.is.tue.mpg.de/person/dtzionas), University of Bonn*

##### \[2016\] Tracking Hands in Action for Gesture-based Computer Input. [\[PDF\]](http://cs.stanford.edu/people/ssrinath/pubs/Dissertation_SrinathSridhar.pdf)
*[Srinath Sridhar](http://cs.stanford.edu/people/ssrinath/),  Max Planck Institute for Informatics*

##### \[2016\] 3D hand pose regression with variants of decision forests. [\[PDF\]](https://spiral.imperial.ac.uk/bitstream/10044/1/31531/1/Tang-D-2016-PhD-Thesis.pdf) [\[Project\]](https://spiral.imperial.ac.uk/handle/10044/1/31531)
*[Danhang Tang](http://www.iis.ee.ic.ac.uk/dtang/), Imperial College London*

##### \[2016\] Deep Learning for Human Motion Analysis. [\[PDF\]](https://tel.archives-ouvertes.fr/tel-01470466v1/document) [\[Project\]](https://tel.archives-ouvertes.fr/tel-01470466v1)
*[Natalia Neverova](https://nneverova.github.io/), National Institut of Applied Science (INSA de Lyon), France*

##### \[2016\] Real time hand pose estimation for human computer interaction. [\[PDF\]](http://epubs.surrey.ac.uk/809973/1/thesis.pdf) [\[Project\]](http://epubs.surrey.ac.uk/809973/)
*[Philip Krejov](http://www.krejov.com/), University of Surrey*

##### \[2015\] Efficient Tracking of the 3D Articulated Motion of Human Hands. [\[PDF\]](http://users.ics.forth.gr/~oikonom/pb/oikonomidisPhDthesis.pdf)
*[Iason Oikonomidis](http://users.ics.forth.gr/~oikonom/pb/), University of Crete*

##### \[2015\] Vision-based hand pose estimation and gesture recognition. [\[PDF\]](https://repository.ntu.edu.sg/bitstream/handle/10356/65842/ThesisMain.pdf?sequence=1&isAllowed=y)
*[Hui Liang](https://sites.google.com/site/seraphlh/home), Nanyang Technological University*

##### \[2015\] Localization of Humans in Images Using Convolutional Networks. [\[PDF\]](http://www.cims.nyu.edu/~tompson/others/thesis.pdf)
*[Jonathan Tompson](http://cims.nyu.edu/~tompson/), New York University*

[\[back to top\]](#contents)

## Datasets

- S/R: Synthetic (S) or Real (R) or Both (B)
- C/D: Color (RGB) or Depth (D)
- Obj: Interaction with objects or not
- #J:  No. of joints
- V: view (3rd or egocentric)
- #S: No. of subjects
- #F: No. of frames (train/test)

|Dataset|Year|S/R|C/D|Obj|#J|V|#S|#F|Related Paper|
|------|------|------|------|------|------|------|------|------|----------------|
|[NYU Hand Pose](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm) | 2014 | R | D | No | 36 | 3rd | 2 | 72k/8k | Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks, SIGGRAPH 2014 [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf)|
|[ICVL](https://labicvl.github.io/hand.html) | 2014 | R | D | No |  16 | 3rd  |  10 | 331k/1.5k | Latent regression forest: Structured estimation of 3d articulated hand posture, CVPR 2014 [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_CVPR_2014.pdf)|
|[MSRA15](https://github.com/geliuhao/CVPR2016_HandPoseEstimation/issues/4) | 2015 | R | D | No |  21 | 3rd  |  9 | 76,375 | Cascaded Hand Pose Regression, CVPR 2015 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf)|
|[BigHand2.2M](http://icvl.ee.ic.ac.uk/hands17/challenge/) | 2017 | R | D | No |  21 | 3rd  |  10 | 2.2M | Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis, CVPR 2017 [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)|
|[FHAD](https://guiggh.github.io/publications/first-person-hands/) | 2018 | R | D | Yes |  21 | ego  |  6 | 100k | First-Person Hand Action Benchmark with RGB-D Videos and 3D Hand Pose Annotations, CVPR 2018 [\[PDF\]](https://arxiv.org/pdf/1704.02463)|
|[GANerated Hands](https://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/GANeratedDataset.htm) | 2018 | S | C | Both |  21 | ego  |  - | 330k | GANerated Hands for Real-Time 3D Hand Tracking from Monocular RGB, CVPR 2018 [\[PDF\]](https://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018.pdf)|
|[EgoDexter](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm) | 2017 | R | C+D | Yes |  5 | ego  |  4 | 1485 | Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor, ICCV 2017 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf)|
|[SynthHands](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/SynthHands.htm) | 2017 | S | C+D | Both |  21 | ego  |  2 | 63,530  | Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor, ICCV 2017 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf)|
|[RHD](https://lmb.informatik.uni-freiburg.de/resources/datasets/RenderedHandposeDataset.en.html) | 2017 | S | C+D | No |  21 | 3rd  |  20 | 41k/2.7k  | Learning to Estimate 3D Hand Pose from Single RGB Images, ICCV 2017 [\[PDF\]](https://arxiv.org/pdf/1705.01389.pdf)|
|[STB](https://sites.google.com/site/zhjw1988/) | 2017 | R | C+D | No |  21 | 3rd |  1 | 18k | A Hand Pose Tracking Benchmark from Stereo Matching, ICIP 2017 [\[PDF\]](http://www.cs.cityu.edu.hk/~jianbjiao2/pdfs/icip.pdf)|
|[CMU Panoptic HandDB](http://domedb.perception.cs.cmu.edu/handdb.html) | 2017 | B | C | No |  21 | 3rd  |  - | 14,817 | Hand Keypoint Detection in Single Images using Multiview Bootstrapping, CVPR 2017 [\[PDF\]](https://arxiv.org/pdf/1704.07809)|
|[Dexter+Object](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/dexter+object.htm) | 2016 | R | C+D | Yes |  5 | 3rd  |  2 | 3,014 | Real-time Joint Tracking of a Hand Manipulating an Object from RGB-D Input, ECCV 2016 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/content/RealtimeHO_ECCV2016.pdf)|
|[MSRC (FingerPaint)](https://www.microsoft.com/en-us/download/details.aspx?id=52288)  | 2015| S | D | No |  21 | both  |  1 | 100k | Accurate, Robust, and Flexible Real-time Hand Tracking, CHI 2015 [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf)|
|[HandNet](http://www.cs.technion.ac.il/~twerd/HandNet/) | 2015 | R | D | No |  6 | 3rd  |  10 | 202k/10k  | Rule of Thumb: Deep Derotation for Improved Fingertip Detection, BMVC 2015 [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf)|
|[UCI-EGO](http://pascal.inrialpes.fr/data2/grogez/UCI-EGO/UCI-EGO.tar.gz) | 2014 | R | D+C | No |  26 | ego  |  2 | 400 | 3D Hand Pose Detection in Egocentric RGB-D Images, ECCVW 2014 [\[PDF\]](https://www.cs.cmu.edu/~deva/papers/egocentric_depth_workshop.pdf)|
|[Hands in Action](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/) | 2014 | R | D | Yes |  - | 3rd  |  - | - | Capturing Hands in Action using Discriminative Salient Points and Physics Simulation, IJCV 2016 [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf)|
|[MSRA14](https://jimmysuen.github.io/) | 2014|  R | D | No |  21 | 3rd  |  6 | 2,400 | Realtime and Robust Hand Tracking from Depth, CVPR 2014 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Qian_Realtime_and_Robust_2014_CVPR_paper.pdf)|
|[Dexter1](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/dexter1.htm) | 2013 | R | D+C | No |  6 | 3rd |  1 | 2,137 | Interactive Markerless Articulated Hand Motion Tracking Using RGB and Depth Data, ICCV 2013 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf)|
|[ASTAR](http://hpes.bii.a-star.edu.sg/) | 2013 | R | D | No |  20 | 3rd  |  30 | 870 | Efficient hand pose estimation from a single depth image, ICCV 2013 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_iccv_2013/papers/Xu_Efficient_Hand_Pose_2013_ICCV_paper.pdf)|

**Credits:**
- [1] Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis, CVPR 2017 [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)
- [2] Depth-based hand pose estimation: methods, data, and challenges, ICCV 2015  [Link](http://arrummzen.net/#HandData)
- [3] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects, IJCV 2016 [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf)
- [4] [MPI Hand Tracking Central](http://handtracker.mpi-inf.mpg.de/)

[\[back to top\]](#contents)

## Workshops

[1] *Workshops on Observing and Understanding Hands in Action:*

##### [HANDS 2018](https://sites.google.com/view/hands2018/), In conjunction with ECCV 2018
- HANDS18: Methods, Techniques and Applications for Hand Observation. [\[PDF\]](https://arxiv.org/abs/1810.10818)

##### [HANDS 2017](http://icvl.ee.ic.ac.uk/hands17/), In conjunction with ICCV 2017
- Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Yuan_Depth-Based_3D_Hand_CVPR_2018_paper.pdf)

##### [HANDS 2016](https://labicvl.github.io/hand/Hands2016/), In conjunction with CVPR 2016
##### [HANDS 2015](http://www.ics.uci.edu/~jsupanci/HANDS-2015/), In conjunction with CVPR 2015
<br>

[2] *Workshops on Capturing and modeling human bodies, faces and hands:*

##### [PeopleCap 2018](https://peoplecap2018.weebly.com/), In conjunction with ECCV 2018
##### [PeopleCap 2017](http://peoplecap.weebly.com/), In conjunction with ICCV 2017

[\[back to top\]](#contents)

## Challenges

##### [The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation](http://icvl.ee.ic.ac.uk/hands17/challenge/)
*[HANDS 2017](http://icvl.ee.ic.ac.uk/hands17/), [ICCV 2017](http://iccv2017.thecvf.com/)*
- Submission Website: [Frame and Tracking Task](https://competitions.codalab.org/competitions/17356#results), [Hand-Object Task](https://competitions.codalab.org/competitions/17452#results)
- Documents
    - [The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation](https://arxiv.org/pdf/1707.02237.pdf), arXiv 2017
    - [Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals.](https://arxiv.org/pdf/1712.03917.pdf), CVPR 2018

[\[back to top\]](#contents)

## Other Related Papers

##### \[2018 SIGGRAPH\] Online Optical Marker-based Hand Tracking with Deep Labels. [\[PDF\]](https://research.fb.com/wp-content/uploads/2018/06/Online-Optical-Marker-based-Hand-Tracking-with-Deep-Labels.pdf) [\[Code\]](https://github.com/Beibei88/Mocap_SIG18_Data)
*Shangchen Han, Beibei Liu, Robert Wang, Yuting Ye, Christopher D. Twigg, Kenrick Kin*

##### \[2018 CVPRW\] HandyNet: A One-stop Solution to Detect, Segment, Localize & Analyze Driver Hands. [\[PDF\]](https://arxiv.org/pdf/1804.07834.pdf) [\[Code\]](https://github.com/arangesh/HandyNet)
*Akshay Rangesh, Mohan M. Trivedi*

##### \[2018 CVPR\] DensePose: Dense Human Pose Estimation In The Wild. [\[PDF\]](https://arxiv.org/pdf/1802.00434.pdf)  [\[Project\]](http://densepose.org/) [\[Code\]](https://github.com/facebookresearch/DensePose)
*Rıza Alp Güler, Natalia Neverova, Iasonas Kokkinos*

##### \[2018 CVPR\] Analysis of Hand Segmentation in the Wild. [\[PDF\]](https://arxiv.org/pdf/1803.03317.pdf) [\[Code\]](https://github.com/aurooj/Hand-Segmentation-in-the-Wild)
*Aisha Urooj Khan, Ali Borji*

##### \[2018 CVPR\] Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies. [\[PDF\]](https://arxiv.org/pdf/1801.01615.pdf) [\[Project\]](http://www.cs.cmu.edu/~hanbyulj/totalcapture/) *(CVPR Best Student Paper Award)*
*Hanbyul Joo, Tomas Simon, Yaser Sheikh*

##### \[2017 CVPR\] SurfNet: Generating 3D shape surfaces using deep residual networks. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2017/03/Sinha_CVPR17.pdf)
*Ayan Sinha, Asim Unmesh, Qixing Huang, Karthik Ramani*

##### \[2017 CVPR\] Learning from Simulated and Unsupervised Images through Adversarial Training. [\[PDF\]](https://arxiv.org/pdf/1511.06728) [\[Project\]](https://machinelearning.apple.com/2017/07/07/GAN.html) [\[Code-Tensorflow\]](https://github.com/carpedm20/simulated-unsupervised-tensorflow) [\[Code-Keras\]](https://github.com/wayaai/SimGAN) [\[Code-Tensorflow-NYU-Hand\]](https://github.com/shinseung428/simGAN_NYU_Hand) *(CVPR Best Paper Award)*
*Ashish Shrivastava, Tomas Pfister, Oncel Tuzel, Josh Susskind, Wenda Wang, Russ Webb*

##### \[2016 3DV\] Learning to Navigate the Energy Landscape. [\[PDF\]](http://www.robots.ox.ac.uk/~tvg/publications/2016/LNEL.pdf) [\[Project\]](http://graphics.stanford.edu/projects/reloc/)
*Julien Valentin, Angela Dai, Matthias Niessner, Pushmeet Kohli, Philip H.S. Torr, Shahram Izadi*

##### [2015 ICCV] 3D Object Reconstruction from Hand-Object Interactions. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/In-Hand-Scanning/ICCV15_Reconstruction_from_HandObject_Interactions.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/-886ddd69-ebde-4f83-8b77-9c41f8af1065)
*Dimitrios Tzionas and Juergen Gall*

[\[back to top\]](#contents)

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

Please feel free to [pull requests](https://github.com/xinghaochen/awesome-hand-pose-estimation/pulls), [open an issue](https://github.com/xinghaochen/awesome-hand-pose-estimation/issues) or send me email (chenxinghaothu@gmail.com) to add awesome papers.


## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, [xinghaochen](https://github.com/xinghaochen) has waived all copyright and
related or neighboring rights to this work.
