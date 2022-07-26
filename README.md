# Awesome Hand Pose Estimation

A curated list of related resources for hand pose estimation. Feel free to [contribute](#Contribute)!

## Contents
 - [Evaluation](#evaluation)
 - [arXiv Papers](#arxiv-papers)
 - [Journal Papers](#journal-papers)
   - [TPAMI / IJCV](#tpami--ijcv)
   - [Others](#other-journals)
 - [Conference Papers](#conference-papers)
   - 2022: [CVPR](#2022-cvpr), [ECCV](#2022-eccv), [Others](#2022-others)
   - 2021: [CVPR](#2021-cvpr), [ICCV](#2021-iccv), [Others](#2021-others)
   - 2020: [CVPR](#2020-cvpr), [ECCV](#2020-eccv), [Others](#2020-others)
   - 2019: [CVPR](#2019-cvpr), [ICCV](#2019-iccv), [Others](#2019-others)
   - 2018: [CVPR](#2018-cvpr), [ECCV](#2018-eccv), [Others](#2018-others)
   - 2017: [CVPR](#2017-cvpr), [ICCV](#2017-iccv), [Others](#2017-others)
   - 2016: [CVPR](#2016-cvpr), [ECCV](#2016-eccv), [Others](#2016-others)
   - 2015: [CVPR](#2015-cvpr), [ICCV](#2015-iccv), [Others](#2015-others)
   - 2014: [CVPR](#2014-cvpr), [Others & Before](#2014-others--before)
 - [Theses](#theses)
 - [Datasets](#datasets)
   - [Depth](#depth)
   - [RGB+Depth](#rgbdepth)
   - [RGB](#rgb)
 - [Workshops](#workshops)
 - [Challenges](#challenges)
 - [Other Related Papers](#other-related-papers)

\* indicates equal contribution

## Evaluation
See folder [``evaluation``](./evaluation) to get more details about performance evaluation for hand pose estimation.

## arXiv Papers

##### • [\[arXiv:2206.07117\]](https://arxiv.org/abs/2206.07117) TriHorn-Net: A Model for Accurate Depth-Based 3D Hand Pose Estimation.  [\[PDF\]](https://arxiv.org/abs/2206.07117)  [\[Code\]](https://github.com/mrezaei92/TriHorn-Net)
_Mohammad Rezaei, Razieh Rastgoo, Vassilis Athitsos_

##### • [\[arXiv:2202.04533\]](https://arxiv.org/abs/2202.04533) NIMBLE: A Non-rigid Hand Model with Bones and Muscles.  [\[PDF\]](https://arxiv.org/pdf/2202.04533)
_Yuwei Li, Longwen Zhang, Zesong Qiu, Yingwenqi Jiang, Yuyao Zhang, Nianyi Li, Yuexin Ma, Lan Xu, Jingyi Yu_

##### • [\[arXiv:2201.09548\]](https://arxiv.org/abs/2201.09548) Consistent 3D Hand Reconstruction in Video via self-supervised Learning.  [\[PDF\]](https://arxiv.org/pdf/2201.09548)
_Zhigang Tu, Zhisheng Huang, Yujin Chen, Di Kang, Linchao Bao, Bisheng Yang, Junsong Yuan_

##### • [\[arXiv:2111.06500\]](https://arxiv.org/abs/2111.06500) Dynamic Iterative Refinement for Efficient 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2111.06500)
_John Yang, Yash Bhalgat, Simyung Chang, Fatih Porikli, Nojun Kwak_

##### • [\[arXiv:2109.14744\]](https://arxiv.org/abs/2109.14744) The Object at Hand: Automated Editing for Mixed Reality Video Guidance from Hand-Object Interactions. [\[PDF\]](https://arxiv.org/pdf/2109.14744)
_Yao Lu, Walterio W. Mayol-Cuevas_

##### • [\[arXiv:2109.14657\]](https://arxiv.org/abs/2109.14657) Understanding Egocentric Hand-Object Interactions from Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2109.14657)
_Yao Lu, Walterio W. Mayol-Cuevas_

##### • [\[arXiv:2109.11747\]](https://arxiv.org/abs/2109.11747) A Multi-View Video-Based 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2109.11747)
_Leyla Khaleghi, Alireza Sepas Moghaddam, Joshua Marshall, Ali Etemad_

##### • [\[arXiv:2108.13995\]](https://arxiv.org/abs/2108.13995) Realistic Hands: A Hybrid Model for 3D Hand Reconstruction. [\[PDF\]](https://arxiv.org/pdf/2108.13995) [\[Project\]](https://hassony2.github.io/homan.html)
_Michael Seeber, Martin R. Oswald, Roi Poranne_

##### • [\[arXiv:2108.07044\]](https://arxiv.org/abs/2108.07044) Towards unconstrained joint hand-object reconstruction from RGB videos. [\[PDF\]](https://arxiv.org/pdf/2108.07044) [\[Project\]](https://hassony2.github.io/homan.html)  [\[Code\]](https://github.com/hassony2/homan)
_Yana Hasson, Gül Varol, Ivan Laptev, Cordelia Schmid_

##### • [\[arXiv:2107.00887\]](https://arxiv.org/abs/2107.00887) HO-3D_v3: Improving the Accuracy of Hand-Object Annotations of the HO-3D Dataset. [\[PDF\]](https://arxiv.org/abs/2107.00887)
_Shreyas Hampali, Sayan Deb Sarkar, Vincent Lepetit_

##### • [\[arXiv:2106.05954\]](https://arxiv.org/abs/2106.05954) Adversarial Motion Modelling helps Semi-supervised Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2106.05954)
_Adrian Spurr, Pavlo Molchanov, Umar Iqbal, Jan Kautz, Otmar Hilliges_

##### • [\[arXiv:2106.04324\]](https://arxiv.org/abs/2106.04324) Contrastive Representation Learning for Hand Shape Estimation. [\[PDF\]](https://arxiv.org/pdf/2106.04324)  [\[Project\]](https://lmb.informatik.uni-freiburg.de/projects/contra-hand/)  [\[Code\]](https://github.com/lmb-freiburg/contra-hand)  [\[Data\]](https://lmb.informatik.uni-freiburg.de/resources/datasets/HanCo.en.html)
_Christian Zimmermann, Max Argus, Thomas Brox_

##### • [\[arXiv:2104.14639\]](https://arxiv.org/abs/2104.14639) HandsFormer: Keypoint Transformer for Monocular 3D Pose Estimation ofHands and Object in Interaction. [\[PDF\]](https://arxiv.org/pdf/2104.14639)
_Shreyas Hampali, Sayan Deb Sarkar, Mahdi Rad, Vincent Lepetit_

##### • [\[arXiv:2102.07067\]](https://arxiv.org/abs/2102.07067) FastHand: Fast Hand Pose Estimation From A Monocular Camera. [\[PDF\]](https://arxiv.org/pdf/2102.07067)
_Shan An, Xiajie Zhang, Dong Wei, Haogang Zhu, Jianyu Yang, Konstantinos A. Tsintotas_

##### • [\[arXiv:2012.11260\]](https://arxiv.org/abs/2012.11260) Unsupervised Domain Adaptation with Temporal-Consistent Self-Training for 3D Hand-Object Joint Reconstruction. [\[PDF\]](https://arxiv.org/pdf/2012.11260.pdf)
_Mengshi Qi, Edoardo Remelli, Mathieu Salzmann, Pascal Fua_

##### • [\[arXiv:2008.08324\]](https://arxiv.org/abs/2008.08324) FrankMocap: Fast Monocular 3D Hand and Body Motion Capture by Regression and Integration. [\[PDF\]](https://arxiv.org/pdf/2008.08324.pdf)  [\[Project\]](https://penincillin.github.io/frank_mocap)
_Yu Rong, Takaaki Shiratori, Hanbyul Joo_

##### • [\[arXiv:2006.05927\]](https://arxiv.org/abs/2006.05927) Recent Advances in 3D Object and Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2006.05927.pdf)
_Vincent Lepetit_

##### • [\[arXiv:2001.08047\]](https://arxiv.org/abs/2001.08047) Attention! A Lightweight 2D Hand Pose Estimation Approach. [\[PDF\]](https://arxiv.org/pdf/2001.08047.pdf)
_Nicholas Santavas, Ioannis Kansizoglou, Loukas Bampis, Evangelos Karakasis, Antonios Gasteratos_

##### • [\[arXiv:2001.00702\]](https://arxiv.org/abs/2001.00702) HandAugment: A Simple Data Augmentation Method for Depth-Based 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2001.00702.pdf) [\[Code\]](https://github.com/wozhangzhaohui/HandAugment)
_Zhaohui Zhang, Shipeng Xie, Mingxiu Chen, Haichao Zhu_

##### • [\[arXiv:1912.12436\]](https://arxiv.org/abs/1912.12436) Silhouette-Net: 3D Hand Pose Estimation from Silhouettes. [\[PDF\]](https://arxiv.org/pdf/1912.12436.pdf)
_Kuo-Wei Lee, Shih-Hung Liu, Hwann-Tzong Chen, Koichi Ito_

##### • [\[arXiv:1911.12501\]](https://arxiv.org/abs/1911.12501) An End-to-end Framework for Unconstrained Monocular 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1911.12501.pdf)
_Sanjeev Sharma, Shaoli Huang, Dacheng Tao_

##### • [\[arXiv:1912.01875\]](https://arxiv.org/abs/1912.01875) GraphPoseGAN: 3D Hand Pose Estimation from a Monocular RGB Image via Adversarial Learning on Graphs. [\[PDF\]](https://arxiv.org/pdf/1912.01875.pdf)
_Yiming He, Wei Hu, Siyuan Yang, Xiaochao Qu, Pengfei Wan, Zongming Guo_

##### • [\[arXiv:1911.07424\]](https://arxiv.org/abs/1911.07424) Capturing Hand Articulations using Recurrent Neural Network for 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1911.07424.pdf)
_Cheol-hwan Yoo, Seung-wook Kim, Seo-won Ji, Yong-goo Shin, Sung-jea Ko_

##### • [\[arXiv:1807.00898\]](https://arxiv.org/abs/1807.00898) Model-based Hand Pose Estimation for Generalized Hand Shape with Appearance Normalization. [\[PDF\]](https://arxiv.org/pdf/1807.00898.pdf)
_Jan Wöhlke, Shile Li, Dongheui Lee_

##### • [\[arXiv:1705.09606\]](https://arxiv.org/abs/1705.09606) End-to-end Global to Local CNN Learning for Hand Pose Recovery in Depth data. [\[PDF\]](https://arxiv.org/pdf/1705.09606.pdf)
_Meysam Madadi, Sergio Escalera, Xavier Baro, Jordi Gonzalez_

##### • [\[arXiv:1704.02224\]](https://arxiv.org/abs/1704.02224) Hand3D: Hand Pose Estimation using 3D Neural Network. [\[PDF\]](https://arxiv.org/pdf/1704.02224.pdf)  [\[Project\]](http://www.idengxm.com/hand3d/index.html)
_Xiaoming Deng\*, Shuo Yang\*, Yinda Zhang\*, Ping Tan, Liang Chang, Hongan Wang_

##### • [\[arXiv:1612.00596\]](https://arxiv.org/abs/1612.00596) Learning to Search on Manifolds for 3D Pose Estimation of Articulated Objects. [\[PDF\]](https://arxiv.org/pdf/1612.00596.pdf)
*Yu Zhang, Chi Xu, Li Cheng*

[\[back to top\]](#contents)

## Journal Papers

### TPAMI / IJCV

##### • \[2022 TPAMI\] Recurrent 3D Hand Pose Estimation Using Cascaded Pose-guided 3D Alignments. [\[PDF\]](https://ieeexplore.ieee.org/document/9736619/)
_Xiaoming Deng, Dexin Zuo, Yinda Zhang, Zhaopeng Cui, Jian Cheng, Ping Tan, Liang Chang, Marc Pollefeys, Sean Fanello, Hongan Wang_

##### • \[2021 TPAMI\] HandVoxNet++: 3D Hand Shape and Pose Estimation using Voxel-Based Neural Networks. [\[PDF\]](https://arxiv.org/abs/2107.01205)
_Jameel Malik, Soshi Shimada, Ahmed Elhayek, Sk Aziz Ali, Christian Theobalt, Vladislav Golyanik, Didier Stricker_

##### • \[2020 TPAMI\] 3D Hand Pose Estimation Using Synthetic Data and Weakly Labeled RGB Images. [\[PDF\]](https://ieeexplore.ieee.org/document/9091090)
_Yujun Cai, Liuhao Ge, Jianfei Cai, Nadia Magnenat-Thalmann, Junsong Yuan_

##### • \[2019 TPAMI\] Generalized Feedback Loop for Joint Hand-Object Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1903.10883) [\[Project\]](https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/joint-3d-hand-object-pose-estimation/)
_Markus Oberweger, Paul Wohlhart, Vincent Lepetit_

##### • \[2019 TPAMI\] Feature Boosting Network For 3D Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/document/8621059)
_Jun Liu, Henghui Ding, Amir Shahroudy, Ling-Yu Duan, Xudong Jiang, Gang Wang, Alex C. Kot_

##### • \[2018 TPAMI\] Opening the Black Box: Hierarchical Sampling Optimization for Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8386667)
_Danhang Tang\*, Qi Ye\*, Shanxin Yuan, Jonathan Taylor, Pushmeet Kohli, Cem Keskin, Tae-Kyun Kim, Jamie Shotton_

##### • \[2018 IJCV\] Depth-Based Hand Pose Estimation: Methods, Data, and Challenges. [\[PDF\]](https://link.springer.com/content/pdf/10.1007%2Fs11263-018-1081-7.pdf)  [\[Project\]](http://arrummzen.net/#HandData) [\[Code\]](https://github.com/jsupancic/deep_hand_pose)
*James Steven Supančič III, Grégory Rogez, Yi Yang, Jamie Shotton, Deva Ramanan*

##### • \[2018 TPAMI\] Real-time 3D Hand Pose Estimation with 3D Convolutional Neural Networks. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8338122)
_Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann_

##### • \[2016 IJCV\] Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups. [\[PDF\]](https://arxiv.org/pdf/1609.03773.pdf) [\[Project\]](https://web.bii.a-star.edu.sg/archive/machine_learning/Projects/behaviorAnalysis/Lie-X/Lie-X.html)
*Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, Li Cheng*

##### • \[2016 TPAMI\] Latent Regression Forest: Structured Estimation of 3D Hand Poses. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7539555)
*Danhang Tang, Hyung Chang, Alykhan Tejani, Tae-Kyun Kim*

##### • \[2016 IJCV\] Capturing Hands in Action using Discriminative Salient Points and Physics Simulation. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf) [\[Project\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/)
*Dimitrios Tzionas, Luca Ballan, Abhilash Srikantha, Pablo Aponte, Marc Pollefeys, Juergen Gall*

##### • \[2015 IJCV\] Estimate Hand Poses Efficiently from Single Depth Images. [\[PDF\]](https://web.bii.a-star.edu.sg/~xuchi/pdf/XuEtAl_IJCV15.pdf) [\[Project\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)  [\[Code\]](https://github.com/lzddzh/HandPoseEstimation)
*Chi Xu, Ashwin Nanjappa, Xiaowei Zhang, Li Cheng*

[\[back to top\]](#contents)

### Other Journals

##### • \[2022 Technologies\] A Survey on GAN-Based Data Augmentation for Hand Pose Estimation Problem. [\[PDF\]](https://www.mdpi.com/2227-7080/10/2/43/pdf?version=1647826385)
_Farnaz Farahanipad, Mohammad Rezaei, Mohammad Sadegh Nasr, Farhad Kamangar, Vassilis Athitsos_

##### • \[2022 TCSVT\] 3D Hand Pose Estimation from Monocular RGB with Feature Interaction Module. [\[PDF\]](https://ieeexplore.ieee.org/document/9680673/)
_Shaoxiang Guo, Eric Rigall, Yakun Ju, Junyu Dong_

##### • \[2021 TIP\] Hand Pose Understanding with Large-Scale Photo-Realistic Rendering Dataset. [\[PDF\]](https://ieeexplore.ieee.org/document/9398571)
_Xiaoming Deng, Yinda Zhang, Jian Shi, Yuying Zhu, Dachuan Cheng, Dexin Zuo, Zhaopeng Cui, Ping Tan, Liang Chang, Hongan Wang_

##### • \[2021 TIP\] Joint Hand-object 3D Reconstruction from a Single Image with Cross-branch Feature Fusion. [\[PDF\]](https://arxiv.org/pdf/2006.15561.pdf)
_Yujin Chen, Zhigang Tu, Di Kang, Ruizhi Chen, Linchao Bao, Zhengyou Zhang, Junsong Yuan_

##### • \[2021 Neurocomputing\] Spatial-aware Stacked Regression Network for Real-time 3D Hand Pose Estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/abs/pii/S0925231221000667)
_Pengfei Ren, Haifeng Sun, Weiting Huang, Jiachang hao, Daixuan Cheng, Qi Qi, Jingyu Wang, Jianxin Liao_


##### • \[2021 TMM\] Differentiable Spatial Regression: A Novel Method for 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1905.02085.pdf) [\[Code\]](https://github.com/IcarusWizard/PixelwiseRegression)
_Xingyuan Zhang, Fuhai Zhang_

##### • \[2020 TIP\] Weakly-supervised Learning for Single Depth based Hand Shape Recovery. [\[PDF\]](https://ieeexplore.ieee.org/document/9262071)
_Xiaoming Deng, Yuying Zhu, Yinda Zhang, Zhaopeng Cui, Ping Tan, Wentian Qu, Cuixia Ma, Hongan Wang_

##### • \[2020 Signal Process Image Commun\] Accurate 3D Hand Pose Estimation Network Utilizing Joints Information. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0923596520301831)
_Xiongquan Zhang; Shiliang Huang; Zhongfu Ye_

##### • \[2020 TCSVT\] Improve Regression Network on Depth Hand Pose Estimation with Auxiliary Variable. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/9085372)
_Lu Xu, Chen Hu, Ji’an Tao, Jianru Xue, Kuizhi Mei_

##### • \[2020 TVCG\] 3D Hand Tracking in the Presence of Excessive Motion Blur. [\[PDF\]](https://ieeexplore.ieee.org/document/8998145)
_Gabyong Park, Antonis Argyros, Juyoung Lee, Woontack Woo_

##### • \[2019 Computers & Graphics\] Simple and effective deep hand shape and pose regression from a single depth image. [\[PDF\]](https://www.sciencedirect.com/science/article/abs/pii/S0097849319301591)
_Jameel Malik, Ahmed Elhayek, Fabrizio Nunnari, Didier Stricker_

##### • \[2019 TIP\] SRHandNet: Real-time 2D Hand Pose Estimation with Simultaneous Region Localization. [\[PDF\]](https://yangangwang.com/papers/WANG-SRH-2019-11.pdf) [\[Project\]](https://yangangwang.com/papers/WANG-SRH-2019-07.html)
_Yangang Wang, Baowen Zhang, Cong Peng_

##### • \[2019 Sensors\] WHSP-Net: A Weakly-Supervised Approach for 3D Hand Shape and Pose Recovery from a Single Depth Image. [\[PDF\]](https://www.mdpi.com/1424-8220/19/17/3784)
_Jameel Malik\*, Ahmed Elhayek\*, Didier Stricker_

##### • \[2019 [RA-L](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=7083369)\] Variational Object-aware 3D Hand Pose from a Single RGB Image. [\[PDF\]](https://www.researchgate.net/profile/Yida_Wang/publication/334639748_Variational_Object-aware_3D_Hand_Pose_from_a_Single_RGB_Image/links/5d3a1a41a6fdcc370a6048df/Variational-Object-aware-3D-Hand-Pose-from-a-Single-RGB-Image.pdf)  [\[Code\]](https://github.com/wangyida/VO-handpose)
_Yafei Gao\*, Yida Wang\*, Pietro Falco, Nassir Navab, Federico Tombari_

##### • \[2018 PR\] A Survey on 3D Hand Pose Estimation: Cameras, Methods, and Datasets. [\[PDF\]](https://www.sciencedirect.com/science/article/abs/pii/S0031320319301724)
_Rui Li, Zhenyu Liu, Jianrong Tan_

##### • \[2018 Neurocomputing\] A CRNN module for hand pose estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0925231218315273#!)
_Zhongxu Hu, Youmin Hu, Jie Liu, Bo Wu, Dongmin Han, Thomas Kurfess_

##### • \[2018 IVC\] Large-scale Multiview 3D Hand Pose Dataset. [\[PDF\]](https://arxiv.org/pdf/1707.03742.pdf)  [\[Project\]](http://www.rovit.ua.es/dataset/mhpdataset/)
_Francisco Gomez-Donoso, Sergio Orts-Escolano and Miguel Cazorla_

##### • \[2018 TCSVT\] Mask-pose Cascaded CNN for 2D Hand Pose Estimation from Single Color Image. [\[PDF\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.pdf)  [\[Project\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.html)  [\[Code\]](https://www.yangangwang.com/papers/WANG-MCC-2018-10.html)
_Yangang Wang, Cong Peng and Yebin Liu_

##### • \[2018 IVC\] Top-down model fitting for hand pose recovery in sequences of depth images. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0262885618301513#aep-article-footnote-id1)
_Meysam Madadi, Sergio Escalera, Alex Carruesco, Carlos Andujar, Xavier Baró, Jordi Gonzàlez_

##### • \[2018 TCYB\] Context-Aware Deep Spatio-Temporal Network for Hand Pose Estimation from Depth Images. [\[PDF\]](https://arxiv.org/pdf/1810.02994.pdf)
_Yiming Wu, Wei Ji, Xi Li, Gang Wang, Jianwei Yin, Fei Wu_

##### • \[2018 IEEE Access\] SHPR-Net: Deep Semantic Hand Pose Regression From Point Clouds. [\[PDF\]](https://ieeexplore.ieee.org/document/8425735/)  [\[Project\]](https://sites.google.com/view/xinghaochen/projects/SHPR-Net)
_Xinghao Chen, Guijin Wang, Cairong Zhang, Tae-Kyun Kim, Xiangyang Ji_

##### • \[2018 Neurocomputing\]  Pose Guided Structured Region Ensemble Network for Cascaded Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1708.03416.pdf)  [\[Project\]](https://sites.google.com/view/xinghaochen/projects/Pose-REN)  [\[Code\]](https://github.com/xinghaochen/Pose-REN)
_Xinghao Chen, Guijin Wang, Hengkai Guo, Cairong Zhang_

##### • \[2018 PR\]  Learning a deep network with spherical part model for 3D hand pose estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S0031320318300839)
_Tzu-Yang Chen, Pai-Wen Ting, Min-Yu Wu, Li-Chen Fu_

##### • \[2018 TIP\] Robust 3D Hand Pose Estimation from Single Depth Images using Multi-View CNNs. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8357595)
_Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann_

##### • \[2018 JVCI\] Region Ensemble Network: Towards Good Practices for Deep 3D Hand Pose Estimation. [\[PDF\]](https://www.sciencedirect.com/science/article/pii/S1047320318300816) [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
_Guijin Wang, Xinghao Chen\*, Hengkai Guo\*, Cairong Zhang_

##### • \[2017 TCYB\] Hough Forest with Optimized Leaves for Global Hand Pose Estimation with Arbitrary Postures. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8237190)
*Hui Liang, Junsong Yuan, J. Lee, Liuhao Ge and Daniel Thalmann*

##### • \[2017 TCSVT\] Robust RGB-D Hand Tracking Using Deep Learning Priors. [\[PDF\]](http://ieeexplore.ieee.org/abstract/document/7955084/)
*Jordi Sanchez-Riera, Kathiravan Srinivasan, Kai-Lung Hua, Wen-Huang Cheng, M. Anwar Hossain, and Mohammed F. Alhamid*

##### • [2017 CVIU] Hand Pose Estimation through Semi-Supervised and Weakly-Supervised Learning. [\[PDF\]](https://arxiv.org/pdf/1511.06728.pdf)
*Natalia Neverova, Christian Wolf, Florian Nebout, Graham Taylor*

##### • \[2017 Neurocomputing\] Multi-task, Multi-domain Learning: application to semantic segmentation and pose regression. [\[PDF\]](http://liris.cnrs.fr/christian.wolf/papers/neurocomputing2017.pdf)
*Damien Foururea, Rémi Emonet, Elisa Fromont, Damien Muselet, Natalia Neverova, Alain Trémeaua, Christian Wolf*

##### • \[2016 CVIU\] Guided Optimisation through Classification and Regression for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/1-s2.0-s107731421630193x-main.pdf) [\[Project\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### • \[2015 TCSVT\] Resolving Ambiguous Hand Pose Predictions by Exploiting Part Correlations. [\[PDF\]](https://ieeexplore.ieee.org/document/6926804/)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

##### • \[2014 TMM\] Parsing the Hand in Depth Images. [\[PDF\]](https://ieeexplore.ieee.org/document/6740010) [\[Project\]](https://sites.google.com/site/seraphlh/projects)  [\[Code\]](https://github.com/shrekei/RandomDecisionForest)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

[\[back to top\]](#contents)

## Conference Papers

### 2022 ECCV

##### • Domain Adaptive Hand Keypoint and Pixel Localization in the Wild. [\[PDF\]](https://arxiv.org/pdf/2203.08344.pdf) [\[Project\]](https://tkhkaeio.github.io/projects/22-hand-ps-da/)
_Takehiko Ohkawa, Yu-Jhe Li, Qichen Fu, Ryosuke Furuta, Kris M. Kitani, and Yoichi Sato_

##### • 3D Interacting Hand Pose Estimation by Hand De-occlusion and Removal. [\[PDF\]](https://arxiv.org/abs/2207.11061) [\[Project\]](https://menghao666.github.io/HDR/)[\[Dataset\]](https://connecthkuhk-my.sharepoint.com/personal/js20_connect_hku_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjs20%5Fconnect%5Fhku%5Fhk%2FDocuments%2FAIH%5Fdataset&ga=1)
Hao Meng, Sheng Jin, Wentao Liu, Chen Qian, Mengxiang Lin, Wanli Ouyang, Ping Luo

### 2022 CVPR

##### • What's in your hands? 3D Reconstruction of Generic Objects in Hands. [\[PDF\]](https://arxiv.org/pdf/2204.07153.pdf) [\[Project\]](https://judyye.github.io/ihoi/) [\[Code\]](https://github.com/JudyYe/ihoi)
_Yufei Ye, Abhinav Gupta, Shubham Tulsiani_

##### • Mining Multi-View Information: A Strong Self-Supervised Framework for Depth-based 3D Hand Pose and Mesh Estimation. \[PDF\]
_Pengfei Ren, Haifeng Sun, Jiachang Hao, Jingyu Wang, Qi Qi,Jianxin Liao_

##### • HandOccNet: Occlusion-Robust 3D Hand Mesh Estimation Network. [\[PDF\]](https://arxiv.org/pdf/2203.14564) [\[Code\]](https://github.com/namepllet/HandOccNet)
_JoonKyu Park, Yeonguk Oh, Gyeongsik Moon, Hongsuk Choi, Kyoung Mu Lee_

##### • Keypoint Transformer: Solving Joint Identification in Challenging Hands and Object Interactions for Accurate 3D Pose Estimation. \[PDF\]
_Shreyas Hampali, Sayan Deb Sarkar, Mahdi Rad, Vincent Lepetit_

##### • Collaborative Learning for Hand and Object Reconstruction with Attention-guided Graph Convolution. \[PDF\] [\[Project\]](https://eldentse.github.io/collab-hand-object/)
_Tze Ho Elden Tse, Kwang In Kim, Ales Leonardis, and Hyung Jin Chang_

##### • Spatial-Temporal Parallel Transformer for Arm-Hand Dynamic Estimation. [\[PDF\]](https://arxiv.org/pdf/2203.16202.pdf)
_Shuying Liu, Wenbin Wu, Jiaxian Wu, Yue Lin_

##### • D-Grasp: Physically Plausible Dynamic Grasp Synthesis for Hand-Object Interactions. [\[PDF\]](https://arxiv.org/pdf/2112.03028.pdf) [\[Project\]](https://eth-ait.github.io/d-grasp/)
_Sammy Christen, Muhammed Kocabas, Emre Aksan, Jemin Hwangbo, Jie Song, Otmar Hilliges_

##### • GOAL: Generating 4D Whole-Body Motion for Hand-Object Grasping. [\[PDF\]](https://arxiv.org/pdf/2112.11454.pdf) [\[Project\]](https://goal.is.tuebingen.mpg.de/)
_Omid Taheri, Vasileios Choutas, Michael J. Black, Dimitrios Tzionas_

##### • OakInk: A Large-scale Knowledge Repository for Understanding Hand-Object Interaction. [\[PDF\]](https://arxiv.org/pdf/2203.15709) [\[Code\]](https://github.com/lixiny/OakInk)
_Lixin Yang, Kailin Li Xinyu Zhan, Fei Wu, Anran Xu, Liu Liu, Cewu Lu_

##### • ArtiBoost: Boosting Articulated 3D Hand-Object Pose Estimation via Online Exploration and Synthesis. [\[PDF\]](https://arxiv.org/pdf/2109.05488) [\[Code\]](https://github.com/MVIG-SJTU/ArtiBoost)
_Kailin Li, Lixin Yang, Xinyu Zhan, Jun Lv, Wenqiang Xu, Jiefeng Li, Cewu Lu_

##### • Interacting Attention Graph for Single Image Two-Hand Reconstruction. [\[PDF\]](https://arxiv.org/pdf/2203.09364)  [\[Project\]](http://www.liuyebin.com/IntagHand/Intaghand.html)  [\[Code\]](https://github.com/Dw1010/IntagHand)
_Mengcheng Li，Liang An, Hongwen Zhang, Lianpeng Wu, Feng Chen, Tao Yu, Yebin Liu_

##### • MobRecon: Mobile-Friendly Hand Mesh Reconstruction from Monocular Image.  [\[PDF\]](https://arxiv.org/pdf/2112.02753) [\[Code\]](https://github.com/SeanChenxy/HandMesh)
_Xingyu Chen, Yufeng Liu, Yajiao Dong, Xiong Zhang, Chongyang Ma, Yanmin Xiong, Yuan Zhang, Xiaoyan Guo_

##### • LISA: Learning Implicit Shape and Appearance of Hands.  [\[PDF\]](https://arxiv.org/pdf/2204.01695) [\[Project\]](http://www.iri.upc.edu/people/ecorona/lisa/)
_Enric Corona, Tomas Hodan, Minh Vo, Francesc Moreno-Noguer, Chris Sweeney, Richard Newcombe, Lingni Ma_


### 2022 Others

##### • [2022 AAAI] Efficient Virtual View Selection for 3D Hand Pose Estimation. [\[PDF\]](https://me495.github.io/handpose-virtualview/resources/paper.pdf) [\[Project\]](https://me495.github.io/handpose-virtualview/) [\[Code\]](https://github.com/iscas3dv/handpose-virtualview) 
_Jian Cheng, Yanguang Wan, Dexin Zuo, Cuixia Ma, Jian Gu, Ping Tan, Hongan Wang, Xiaoming Deng, Yinda Zhang_

### 2021 ICCV

##### • Toward Human-Like Grasp: Dexterous Grasping via Semantic Representation of Object-Hand. [\[PDF\]](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhu_Toward_Human-Like_Grasp_Dexterous_Grasping_via_Semantic_Representation_of_Object-Hand_ICCV_2021_paper.pdf)
_Tianqiang Zhu, Rina Wu, Xiangbo Lin, Yi Sun_

##### • Self-Supervised Transfer Learning for Hand Mesh Recovery From Binocular Images. [\[PDF\]](https://openaccess.thecvf.com/content/ICCV2021/papers/Chen_Self-Supervised_Transfer_Learning_for_Hand_Mesh_Recovery_From_Binocular_Images_ICCV_2021_paper.pdf)
_Zheng Chen, Sihan Wang, Yi Sun, Xiaohong Ma_

##### • Self-Supervised 3D Hand Pose Estimation from monocular RGB via Contrastive Learning. [\[PDF\]](https://arxiv.org/pdf/2106.05953) [\[Code\]](https://github.com/dahiyaaneesh/peclr) (Oral)
_Adrian Spurr, Aneesh Dahiya, Xucong Zhang, Xi Wang, Otmar Hilliges_

##### • Towards Accurate Alignment in Real-time 3D Hand-Mesh Reconstruction. [\[PDF\]](https://arxiv.org/pdf/2109.01723.pdf)  [\[Code\]](https://github.com/wbstx/handAR)
_Xiao Tang, Tianyu Wang, Chi-Wing Fu_

##### • EventHands: Real-Time Neural 3D Hand Reconstruction from an Event Stream. [\[PDF\]](https://arxiv.org/pdf/2012.06475.pdf)  [\[Project\]](https://gvv.mpi-inf.mpg.de/projects/EventHands/)
_Viktor Rudnev, Vladislav Golyanik, Jiayi Wang, Hans-Peter Seidel, Franziska Mueller, Mohamed Elgharib, Christian Theobalt_

##### • Reconstructing Hand-Object Interactions in the Wild. [\[PDF\]](https://arxiv.org/pdf/2012.09856.pdf)  [\[Project\]](https://people.eecs.berkeley.edu/~zhecao/rhoi/)
_Zhe Cao*, Ilija Radosavovic*, Angjoo Kanazawa, Jitendra Malik_

##### • HandFoldingNet: A 3D Hand Pose Estimation Network Using Multiscale-Feature Guided Folding of a 2D Hand Skeleton. [\[PDF\]](https://arxiv.org/pdf/2108.05545) [\[Code\]](https://github.com/cwc1260/HandFold)
_Wencan Cheng, Jae Hyun Park, Jong Hwan Ko_

##### • H2O: Two Hands Manipulating Objects for First Person Interaction Recognition. [\[PDF\]](https://arxiv.org/pdf/2104.11181)  [\[Project\]](https://www.taeinkwon.com/projects/h2o)  [\[Code\]](https://github.com/taeinkwon/h2odataset)
_Taein Kwon, Bugra Tekin, Jan Stuhmer, Federica Bogo, Marc Pollefeys_

##### • I2UV-HandNet: Image-to-UV Prediction Network for Accurate and High-fidelity 3D Hand Mesh Modeling. [\[PDF\]](https://arxiv.org/pdf/2102.03725)
_Ping Chen, Yujin Chen, Dong Yang, Fangyin Wu, Qin Li, Qingpei Xia, Yong Tan_

##### • SemiHand: Semi-supervised Hand Pose Estimation with Consistency. [\[PDF\]](https://www.mu4yang.com/files/project/semihand/semihand.pdf)
_Linlin Yang, Shicheng Chen, Angela Yao_

##### • End-to-End Detection and Pose Estimation of Two Interacting Hands. [\[PDF\]](https://openaccess.thecvf.com/content/ICCV2021/papers/Kim_End-to-End_Detection_and_Pose_Estimation_of_Two_Interacting_Hands_ICCV_2021_paper.pdf)
_Donguk Kim, Kwang In Kim, Seungryul Baek_

##### • Hand-Object Contact Consistency Reasoning for Human Grasps Generation. [\[PDF\]](https://arxiv.org/pdf/2104.03304) [\[Project\]](https://hwjiang1510.github.io/GraspTTA/) *(Oral)*
_Hanwen Jiang, Shaowei Liu, Jiashun Wang, Xiaolong Wang_

##### • Hand Image Understanding via Deep Multi-Task Learning. [\[PDF\]](https://arxiv.org/pdf/2107.11646) [\[Code\]](https://github.com/MandyMo/HIU-DMTL)
_Xiong Zhang, Hongsheng Huang, Jianchao Tan, Hongmin Xu, Cheng Yang, Guozhu Peng, Lei Wang, Ji Liu_

##### • CPF: Learning a Contact Potential Field to Model the Hand-object Interaction. [\[PDF\]](https://arxiv.org/pdf/2012.00924.pdf)  [\[Code\]](https://github.com/lixiny/CPF)
_Lixin Yang, Xinyu Zhan, Kailin Li, Wenqiang Xu, Jiefeng Li, Cewu Lu_

##### • TravelNet: Self-supervised Physically Plausible Hand Motion Learning from Monocular Color Images.  [\[PDF\]](https://www.yangangwang.com/papers/ZHAO-TRAVEL-2021-08.pdf)
_Zimeng Zhao, Xi Zhao and Yangang Wang_

##### • Interacting Two-Hand 3D Pose and Shape Reconstruction from Single Color Image.  [\[PDF\]](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Interacting_Two-Hand_3D_Pose_and_Shape_Reconstruction_From_Single_Color_ICCV_2021_paper.pdf) [\[Project\]](https://baowenz.github.io/Intershape/) [\[Code\]](https://github.com/BaowenZ/Two-Hand-Shape-Pose)
_Baowen Zhang, Yangang Wang, Xiaoming Deng, Yinda Zhang, Ping Tan, Cuixia Ma and Hongan Wang_


##### • Removing the Bias of Integral Pose Regression. [\[PDF\]](https://www.mu4yang.com/files/papers/Removing%20the%20Bias%20of%20Integral%20Pose%20Regression.pdf)
_Kerui Gu, Linlin Yang, Angela Yao_

[\[back to top\]](#contents)

### 2021 CVPR

##### • Monocular Real-time Full Body Capture with Inter-part Correlations. [\[PDF\]](https://arxiv.org/pdf/2012.06087)
_Yuxiao Zhou, Marc Habermann, Ikhsanul Habibie, Ayush Tewari, Christian Theobalt, Feng Xu_

##### • End-to-End Human Pose and Mesh Reconstruction with Transformers. [\[PDF\]](https://arxiv.org/pdf/2012.09760.pdf) [\[Code\]](https://github.com/microsoft/MeshTransformer)
_Kevin Lin, Lijuan Wang, Zicheng Liu_

##### • DexYCB: A Benchmark for Capturing Hand Grasping of Objects. [\[PDF\]](https://arxiv.org/pdf/2104.04631.pdf) [\[Project\]](https://dex-ycb.github.io/) [\[Code\]](https://github.com/NVlabs/dex-ycb-toolkit)
_Yu-Wei Chao, Wei Yang, Yu Xiang, Pavlo Molchanov, Ankur Handa, Jonathan Tremblay, Yashraj S. Narang, Karl Van Wyk, Umar Iqbal, Stan Birchfield, Jan Kautz, Dieter Fox_

##### • Body2Hands: Learning to Infer 3D Hands from Conversational Gesture Body Dynamics. [\[PDF\]](https://arxiv.org/pdf/2007.12287.pdf) [\[Project\]](http://people.eecs.berkeley.edu/~evonne_ng/projects/body2hands/)
_Evonne Ng, Hanbyul Joo, Shiry Ginosar, Trevor Darrell_

##### • Camera-Space Hand Mesh Recovery via Semantic Aggregation and Adaptive 2D-1D Registration. [\[PDF\]](https://arxiv.org/pdf/2103.02845.pdf)
_Xingyu Chen, Yufeng Liu, Chongyang Ma, Jianlong Chang, Huayan Wang, Tian Chen, Xiaoyan Guo, Pengfei Wan, Wen Zheng_

##### • Model-based 3D Hand Reconstruction via Self-Supervised Learning. [\[PDF\]](https://arxiv.org/pdf/2103.11703)
_Yujin Chen, Zhigang Tu, Di Kang, Linchao Bao, Ying Zhang, Xuefei Zhe, Ruizhi Chen, Junsong Yuan_

##### • Semi-Supervised 3D Hand-Object Poses Estimation with Interactions in Time. [\[PDF\]](https://arxiv.org/pdf/2106.05266.pdf) [\[Project\]](https://stevenlsw.github.io/Semi-Hand-Object/) [\[Code\]](https://github.com/stevenlsw/Semi-Hand-Object)
_Shaowei Liu*, Hanwen Jiang*, Jiarui Xu, Sifei Liu, Xiaolong Wang_

[\[back to top\]](#contents)

### 2021 Others

##### • [2021 3DV] A Skeleton-Driven Neural Occupancy Representation for Articulated Hands. [\[PDF\]](https://arxiv.org/pdf/2109.11399) [\[Project\]](https://korrawe.github.io/HALO/HALO.html) [\[Code\]](https://github.com/korrawe/halo) *(Oral)*
_Korrawe Karunratanakul, Adrian Spurr, Zicong Fan, Otmar Hilliges, Siyu Tang_

##### • [2021 3DV] Learning to Disambiguate Strongly Interacting Hands via Probabilistic Per-pixel Part Segmentation. [\[PDF\]](https://arxiv.org/abs/2107.00434) [\[Project\]](https://zc-alexfan.github.io/digit) [\[Code\]](https://github.com/zc-alexfan/digit-interacting) *(Oral)*
_Zicong Fan, Adrian Spurr, Muhammed Kocabas, Siyu Tang, Michael J. Black, Otmar Hilliges_

##### • [2021 DICTA] Semi-Supervised 3D Hand Shape and Pose Estimation with Label Propagation. [\[PDF\]](https://arxiv.org/pdf/2111.15199)
_Samira Kaviani, Amir Rahimi, Richard Hartley_

##### • [2021 BMVC] Joint-Aware Regression: Rethinking Regression-Based Method for 3D Hand Pose Estimation. \[PDF\]
_Xiaozheng Zheng, Pengfei Ren, Haifeng Sun, Jingyu Wang, Qi Qi and Jianxin Liao_

##### • [2021 BMVC] Local and Global Point Cloud Reconstruction for 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2112.06389.pdf) [\[Data\]](https://github.com/ShichengChen/multiviewDataset)
_Ziwei Yu, Linlin Yang, Shicheng Chen and Angela Yao_

##### • [2021 BMVC] HandTailor: Towards High-Precision Monocular 3D Hand Recovery. [\[PDF\]](https://arxiv.org/pdf/2102.09244) [\[Code\]](https://github.com/LyuJ1998/HandTailor)
_Jun Lv, Wenqiang Xu, Lixin Yang, Sucheng Qian, Chongzhao Mao, Cewu Lu_

##### • [2021 BMVC] Multi-view Image-based Hand Geometry Refinement using Differentiable Monte Carlo Ray Tracing. [\[PDF\]](https://arxiv.org/pdf/2107.05509)
_Giorgos Karvounas, Nikolaos Kyriazis, Iason Oikonomidis, Aggeliki Tsoli, Antonis A. Argyros_

##### • [2021 SIGGRAPH] ManipNet: Neural Manipulation Synthesis with a Hand-Object Spatial Representation. [\[PDF\]](http://www.ipab.inf.ed.ac.uk/cgvu/zhang2021.pdf)  [\[Code\]](https://github.com/cghezhang/ManipNet)
_He Zhang, Yuting Ye, Takaaki Shiratori, Taku Komura_

##### • [2021 SIGGRAPH] Single Depth View-Based Real-time Reconstruction of Hand-object Interactions. [\[PDF\]](http://xufeng.site/publications/2021/Single%20Depth%20View%20Based%20Real-time%20Reconstruction%20of%20Hand-objectInteractions.pdf)
_Hao Zhang, Yuxiao Zhou, Yifei Tian, Jun-Hai Yong, Feng Xu_

##### • [2021 IROS] Dynamic Modeling of Hand-Object Interactions via Tactile Sensing. [\[PDF\]](https://arxiv.org/pdf/2109.04378)  [\[Project\]](http://phystouch.csail.mit.edu/)
_Qiang Zhang, Yunzhu Li, Yiyue Luo, Wan Shou, Michael Foshey, Junchi Yan, Joshua B. Tenenbaum, Wojciech Matusik, Antonio Torralba_

##### • [2021 AAAI] Exploiting Learnable Joint Groups for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2012.09496)  [\[Code\]](https://github.com/moranli-aca/LearnableGroups-Hand)
_Moran Li, Yuan Gao, Nong Sang_

##### • [2021 WACV] Active Learning for Bayesian 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2010.00694)  [\[Code\]](https://github.com/razvancaramalau/al_bhpe)
_Razvan Caramalau, Binod Bhattarai, Tae-Kyun Kim_

##### • [2021 WACV] Two-hand Global 3D Pose Estimation Using Monocular RGB. [\[PDF\]](https://arxiv.org/pdf/2006.01320.pdf)  [\[Code\]](https://github.com/AlextheEngineer/Ego3DHands)
_Fanqing Lin, Connor Wilhelm, Tony Martinez_

##### • [2021 WACV] MVHM: A Large-Scale Multi-View Hand Mesh Benchmark for Accurate 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/abs/2012.03206)
_Liangjian Chen, Shih-Yao Lin, Yusheng Xie, Yen-Yu Lin, Xiaohui Xie_

##### • [2021 WACV] Temporal-Aware Self-Supervised Learning for 3D Hand Pose and Mesh Estimation in Videos. [\[PDF\]](https://arxiv.org/abs/2012.03205)
_Liangjian Chen, Shih-Yao Lin, Yusheng Xie, Yen-Yu Lin, Xiaohui Xie_

##### • [2021 PETRA] Weakly-supervised hand part segmentation from depth images. [\[PDF\]](https://dl.acm.org/doi/10.1145/3453892.3453902)
_Mohammad Rezaei, Farnaz Farahanipad, Alex Dillhoff, Ramez Elmasri, Vassilis Athitsos_

##### • [2021 PETRA] A Pipeline for Hand 2-D Keypoint Localization Using Unpaired Image to Image Translation. [\[PDF\]](https://dl.acm.org/doi/10.1145/3453892.3453904)
_Farnaz Farahanipad, Mohammad Rezaei, Alex Dillhoff, Farhad Kamangar, Vassilis Athitsos_


[\[back to top\]](#contents)

### 2020 ECCV

##### • GRAB: A Dataset of Whole-Body Human Grasping of Objects. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490562.pdf) [\[Project\]](https://grab.is.tue.mpg.de/) [\[Code\]](https://github.com/otaheri/GrabNet)
_Omid Taheri, Nima Ghorbani, Michael J. Black, Dimitrios Tzionas_

##### • Monocular Expressive Body Regression through Body-Driven Attention. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123550018.pdf) [\[Project\]](https://expose.is.tue.mpg.de/en) [\[Code\]](https://github.com/vchoutas/expose)
_Vasileios Choutas, Georgios Pavlakos, Timo Bolkart, Dimitrios Tzionas , Michael J. Black_

##### • The Phong Surface: Efficient 3D Model Fitting using Lifted Optimization. [\[PDF\]](https://arxiv.org/pdf/2007.04940) *(Oral)*
_Jingjing Shen, Thomas J. Cashman, Qi Ye, Tim Hutton, Toby Sharp, Federica Bogo, Andrew William Fitzgibbon, Jamie Shotton_

##### • Whole-Body Human Pose Estimation in the Wild. [\[PDF\]](https://arxiv.org/pdf/2007.11858.pdf) [\[Code\]](https://github.com/jin-s13/COCO-WholeBody)
_Sheng Jin, Lumin Xu, Jin Xu, Can Wang, Wentao Liu, Chen Qian, Wanli Ouyang, Ping Luo_

##### • Dual Grid Net: hand mesh vertex regression from single depth maps. [\[PDF\]](https://arxiv.org/pdf/1907.10695.pdf)
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### • Hand-Transformer: Non-Autoregressive Structured Modeling for 3D Hand Pose Estimation. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123700018.pdf)
_Lin Huang, Jianchao Tan, Ji Liu, and Junsong Yuan_

##### • ContactPose: A Dataset of Grasps with Object Contact and Hand Pose. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123580358.pdf)  [\[Project\]](https://contactpose.cc.gatech.edu/) [\[Code\]](https://github.com/facebookresearch/ContactPose)
_Samarth Brahmbhatt, Chengcheng Tang, Chris Twigg, Charles C. Kemp, and James Hays_

##### • SeqHAND: RGB-Sequence-Based 3D Hand Pose and Shape Estimation. [\[PDF\]](http://arxiv.org/pdf/2007.05168)
_John Yang, Hyung Jin Chang, Seungeui Lee, Nojun Kwak_

##### • HTML: A Parametric Hand Texture Model for 3D Hand Reconstruction and Personalizationm. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123560052.pdf) [\[Project\]](https://handtracker.mpi-inf.mpg.de/projects/HandTextureModel/)
_Neng Qian, Jiayi Wang, Franziska Mueller, Florian Bernard, Vladislav Golyanik, Christian Theobalt_

##### • JGR-P2O: Joint Graph Reasoning based Pixel-to-Offset Prediction Network for 3D Hand Pose Estimation from a Single Depth Image. [\[PDF\]](https://arxiv.org/pdf/2007.04646)  [\[Code\]](https://github.com/fanglinpu/JGR-P2O) *(Spotlight)*
_Linpu Fang, Xingyan Liu, Li Liu, Hang Xu, Wenxiong Kang_

##### • Adaptive Computationally Efficient Network for Monocular 3D Hand Pose Estimation. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123490120.pdf) *(Spotlight)*
_Zhipeng Fan, Jun Liu, Yao Wang_

##### • Collaborative Learning of Gesture Recognition and 3D Hand Pose Estimation with Multi-Order Feature Analysis.  [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123480766.pdf) *(Spotlight)*
_Siyuan Yang, Jun Liu, Shijian Lu, Meng Hwa Er, Alex C. Kot_

##### • DeepHandMesh: Weakly-supervised Deep Encoder-Decoder Framework for High-fidelity Hand Mesh Modeling from a Single RGB Image. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123470426.pdf) [\[Project\]](https://mks0601.github.io/DeepHandMesh/) *(Oral)*
_Gyeongsik Moon, Takaaki Shiratori, Kyoung Mu Lee_

##### • InterHand2.6M: A New Large-scale Dataset and Baseline for 3D Single and Interacting Hand Pose Estimation from a Single RGB Image. [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650545.pdf) [\[Project\]](https://mks0601.github.io/InterHand2.6M/) \[[Code\]](https://github.com/facebookresearch/InterHand2.6M)
_Gyeongsik Moon, Shoou-i Yu, He Wen, Takaaki Shiratori, Kyoung Mu Lee_

##### • I2L-MeshNet: Image-to-Lixel Prediction Network for Accurate 3D Human Pose and Mesh Estimation from a Single RGB Image. [\[PDF\]](https://arxiv.org/abs/2008.03713) \[[Code\]](https://github.com/mks0601/I2L-MeshNet_RELEASE)
_Gyeongsik Moon, Kyoung Mu Lee_

##### • Weakly-Supervised 3D Hand Pose Estimation via Biomechanical Constraints. [\[PDF\]](https://arxiv.org/pdf/2003.09282.pdf)
_Adrian Spurr, Umar Iqbal, Pavlo Molchanov, Otmar Hilliges, Jan Kautz_

##### • Measuring Generalisation to Unseen Viewpoints, Articulations, Shapes and Objects for 3D Hand Pose Estimation under Hand-Object Interaction. [\[PDF\]](https://arxiv.org/pdf/2003.13764.pdf) \[[Code\]](https://github.com/anilarmagan/HANDS19-Challenge-Toolbox)
_Anil Armagan, Guillermo Garcia-Hernando, Seungryul Baek, Shreyas Hampali, Mahdi Rad, Zhaohui Zhang, Shipeng Xie, MingXiu Chen, Boshen Zhang, Fu Xiong, Yang Xiao, Zhiguo Cao, Junsong Yuan, Pengfei Ren, Weiting Huang, Haifeng Sun, Marek Hrúz, Jakub Kanis, Zdeněk Krňoul, Qingfu Wan, Shile Li, Linlin Yang, Dongheui Lee, Angela Yao, Weiguo Zhou, Sijia Mei, Yunhui Liu, Adrian Spurr, Umar Iqbal, Pavlo Molchanov, Philippe Weinzaepfel, Romain Brégier, Gregory Rogez, Vincent Lepetit, Tae-Kyun Kim_

[\[back to top\]](#contents)

### 2020 CVPR

##### • Weakly-Supervised Mesh-Convolutional Hand Reconstruction in the Wild. [\[PDF\]](https://arxiv.org/pdf/2004.01946.pdf) [\[Project\]](https://www.arielai.com/mesh_hands/)  *(Oral)* *([Paper Award Nominees](http://cvpr2020.thecvf.com/node/817))*
_Dominik Kulon, Riza Alp Güler, Iasonas Kokkinos, Michael Bronstein, Stefanos Zafeiriou_

##### • Weakly-supervised Domain Adaptation via GAN and Mesh Model for Estimating 3D Hand Poses Interacting Objects.  [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2020/papers/Baek_Weakly-Supervised_Domain_Adaptation_via_GAN_and_Mesh_Model_for_Estimating_CVPR_2020_paper.pdf) [\[Code\]](https://github.com/bsrvision/weak_da_hands) *(Oral)* *([Paper Award Nominees](http://cvpr2020.thecvf.com/node/817))*
_Seungryul Baek, Kwang In Kim, Tae-Kyun Kim_

##### • GanHand: Predicting Human Grasp Affordances in Multi-Object Scenes. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2020/papers/Corona_GanHand_Predicting_Human_Grasp_Affordances_in_Multi-Object_Scenes_CVPR_2020_paper.pdf)
_Enric Corona, Albert Pumarola, Guillem Alenya, Francesc Moreno-Noguer, Gregory Rogez_

##### • Cross-Modal Variational Alignment of Latent Spaces. [\[PDF\]](http://openaccess.thecvf.com/content_CVPRW_2020/papers/w56/Theodoridis_Cross-Modal_Variational_Alignment_of_Latent_Spaces_CVPRW_2020_paper.pdf)
_Thomas Theodoridis, Theocharis Chatzis, Vassilios Solachidis, Kosmas Dimitropoulos, Petros Daras_

##### • HUMBI: A Large Multiview Dataset of Human Body Expressions. [\[PDF\]](https://arxiv.org/pdf/1812.00281.pdf) [\[Project\]](https://humbi-data.net/hand/)
_Zhixuan Yu\*, Jae Shin Yoon\*, Prashanth Venkatesh, Jaesik Park, Jihun Yu, Hyun Soo Park_

##### • Epipolar Transformers. [\[PDF\]](https://arxiv.org/pdf/2005.04551.pdf) [\[Code\]](https://github.com/yihui-he/epipolar-transformers)
_Yihui He\*, Rui Yan\*, Shoou-I Yu, Katerina Fragkiadaki_

##### • HandVoxNet: Deep Voxel-Based Network for 3D Hand Shape and Pose Estimation from a Single Depth Map. [\[PDF\]](https://arxiv.org/pdf/2004.01588.pdf)
_Jameel Malik, Ibrahim Abdelaziz, Ahmed Elhayek, Soshi Shimada, Sk Aziz Ali, Vladislav Golyanik, Christian Theobalt, Didier Stricker_

##### • Knowledge as Priors: Cross-Modal Knowledge Generalization for Datasets without Superior Knowledge. [\[PDF\]](https://arxiv.org/pdf/2004.00176.pdf)
_Long Zhao, Xi Peng, Yuxiao Chen, Mubbasir Kapadia, Dimitris N. Metaxas_

##### • Leveraging Photometric Consistency over Time for Sparsely Supervised Hand-Object Reconstruction. [\[PDF\]](http://arxiv.org/pdf/2004.13449.pdf) [\[Project\]](https://hassony2.github.io/handobjectconsist.html) [\[Code\]](https://github.com/hassony2/handobjectconsist)
_Yana Hasson, Bugra Tekin, Federica Bogo, Ivan Laptev, Marc Pollefeys, Cordelia Schmid_

##### • Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data. [\[PDF\]](https://arxiv.org/pdf/2003.09572.pdf) [\[Project\]](https://calciferzh.github.io/publications/zhou2020monocular) [\[Code\]](https://github.com/CalciferZh/minimal-hand)
_Yuxiao Zhou, Marc Habermann, Weipeng Xu, Ikhsanul Habibie, Christian Theobalt, Feng Xu_

##### • HOPE-Net: A Graph-based Model for Hand-Object Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2020/papers/Doosti_HOPE-Net_A_Graph-Based_Model_for_Hand-Object_Pose_Estimation_CVPR_2020_paper.pdf) [\[Code\]](https://github.com/bardiadoosti/HOPE)
_Bardia Doosti, Shujon Naha, David Crandall, Majid Mirbagheri_

##### • HOnnotate: A method for 3D Annotation of Hand and Objects Poses. [\[PDF\]](https://arxiv.org/pdf/1907.01481.pdf) [\[Project\]](https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/hand-object-3d-pose-annotation/) [\[Code\]](https://github.com/shreyashampali/ho3d)
_Shreyas Hampali, Mahdi Rad, Markus Oberweger, Vincent Lepetit_

[\[back to top\]](#contents)

### 2020 Others

##### • [2020 ICRA] Robust, Occlusion-aware Pose Estimation for Objects Grasped by Adaptive Hands . [\[PDF\]](https://arxiv.org/pdf/2003.03518.pdf) [\[Code\]](https://github.com/wenbowen123/icra20-hand-object-pose)
_Bowen Wen, Chaitanya Mitash, Sruthi Soorian, Andrew Kimmel, Avishai Sintov, Kostas E. Bekris_

##### • [2020 CVPRW] MediaPipe Hands: On-device Real-time Hand Tracking. [\[PDF\]](https://arxiv.org/pdf/2006.10214.pdf)
_Fan Zhang, Valentin Bazarevsky, Andrey Vakunov, Andrei Tkachenka, George Sung, Chuo-Ling Chang, Matthias Grundmann_

##### • [2020 ISMAR] 3D Hand Pose Estimation with a Single Infrared Camera via Domain Transfer Learning. [\[PDF\]](https://drive.google.com/file/d/1rBmsblA2YY4qDUxY4GRgrLQ0EyA3wbFs/view)
_Gabyong Park, Tae-Kyun Kim, Woontack Woo_

##### • [2020 ISMAR] Bare-hand Depth Inpainting for 3D Tracking of Hand Interacting with Object. [\[PDF\]](https://drive.google.com/file/d/1hwOATe-2Sr5CdQD98SlIYlpCAGRQ109N/view)
_Woojin Cho, Gabyong Park, Woontack Woo_

##### • [2020 3DV] Grasping Field: Learning Implicit Representations for Human Grasps. [\[PDF\]](https://arxiv.org/pdf/2008.04451.pdf) [\[Code\]](https://github.com/korrawe/grasping_field) *(Best Paper Award)*
_Korrawe Karunratanakul, Jinlong Yang, Yan Zhang, Michael Black, Krikamol Muandet, Siyu Tang_

##### • [2020 UIST] DeepFisheye: Near-Surface Multi-Finger Tracking Technology Using Fisheye Camera. [\[PDF\]](https://dl.acm.org/doi/abs/10.1145/3379337.3415818)  [\[Project\]](http://kwpark.io/deepfisheye) [\[Code\]](https://github.com/KAIST-HCIL/DeepFisheyeNet)
_Keunwoo Park, Sunbum Kim, Youngwoo Yoon, Tae-Kyun Kim, Geehyuk Lee_

##### • [2020 SIGGRAPH Asia] Constraining Dense Hand Surface Tracking With Elasticity. [\[PDF\]](https://research.fb.com/wp-content/uploads/2020/11/Constraining-Dense-Hand-Surface-Tracking-with-Elasticity.pdf)  [\[Project\]](https://research.fb.com/publications/constraining-dense-hand-surface-tracking-with-elasticity/)
_Breannan Smith, Chenglei Wu, He Wen, Patrick Peluse, Yaser Sheikh, Jessica Hodgins, Takaaki Shiratori_

##### • [2020 SIGGRAPH Asia] RGB2Hands: Real-Time Tracking of 3D Hand Interactions from Monocular RGB Video. [\[PDF\]](https://handtracker.mpi-inf.mpg.de/projects/RGB2Hands/content/RGB2Hands_author_version.pdf)  [\[Project\]](https://handtracker.mpi-inf.mpg.de/projects/RGB2Hands/)
_Jiayi Wang, Franziska Mueller, Florian Bernard, Suzanne Sorli, Oleksandr Sotnychenko, Neng Qian, Miguel A. Otaduy, Dan Casas, and Christian Theobalt_

##### • [2020 SIGGRAPH] MEgATrack: Monochrome Egocentric Articulated Hand-Tracking for Virtual Reality. [\[PDF\]](https://dl.acm.org/doi/abs/10.1145/3386569.3392452)
_Shangchen Han, Beibei Liu, Randi Cabezas, Christopher D. Twigg, Peizhao Zhang, Jeff Petkau, Tsz-Ho Yu, Chun-Jung Tai, Muzaffer Akbay, Zheng Wang, Asaf Nitzan, Gang Dong, Yuting Ye, Lingling Tao, Chengde Wan, Robert Wang_

##### • [2020 MM] MM-Hand: 3D-Aware Multi-Modal Guided Hand Generation for 3D Hand Pose Synthesis. [\[PDF\]](http://vllab.cs.nctu.edu.tw/images/paper/mm-wu20.pdf) [\[Code\]](https://github.com/ScottHoang/mm-hand)
_Zhenyu Wu, Duc Hoang, Shih-Yao Lin, Yusheng Xie, Liangjian Chen, Yen-Yu Lin, Zhangyang Wang, Wei Fan_

##### • [2020 MM] Adaptive Wasserstein Hourglass for Weakly Supervised Hand Pose Estimation from Monocular RGB. [\[PDF\]](https://arxiv.org/pdf/1909.05666.pdf)
_Yumeng Zhang, Li Chen, Yufeng Liu, Junhai Yong, Wen Zheng_

##### • [2020 MM] HOT-Net: Non-Autoregressive Transformer for 3D Hand-Object Pose Estimation. [\[PDF\]](https://cse.buffalo.edu/~jsyuan/papers/2020/lin_mm20.pdf)
_Lin Huang, Jianchao Tan, Jingjing Meng, Ji Liu, and Junsong Yuan_

##### • [2020 BMVC] PMD-Net: Privileged Modality Distillation Network for 3D Hand Pose Estimation from a Single RGB Image. [\[PDF\]](https://www.bmvc2020-conference.com/assets/papers/0413.pdf)
_Kewen Wang and Xilin Chen_

##### • [2020 BMVC] SIA-GCN: A Spatial Information Aware Graph Neural Network with 2D Convolutions for Hand Pose Estimation. [\[PDF\]](https://www.bmvc2020-conference.com/assets/papers/0066.pdf)
_Deying Kong, Haoyu Ma and Xiaohui Xie_

##### • [2020 BMVC] Explicit Knowledge Distillation for 3D Hand Pose Estimation from Monocular RGB. [\[PDF\]](https://www.bmvc2020-conference.com/assets/papers/0242.pdf)
_Yumeng Zhang, Li Chen, Yufeng Liu, Wen Zheng and JunHai Yong_

##### • [2020 BMVC] BiHand: Recovering Hand Mesh with Multi-stage Bisected Hourglass Networks. [\[PDF\]](https://arxiv.org/pdf/2008.05079.pdf) [\[Code\]](https://github.com/lixiny/bihand)
_Lixin Yang, Jiasen Li, Wenqiang Xu, Yiqun Diao, Cewu Lu_

##### • [2020 Ubicomp] FingerTrak: Continuous 3D Hand Pose Tracking by Deep Learning Hand Silhouettes Captured by Miniature Thermal Cameras on Wrist. [\[PDF\]](https://dl.acm.org/doi/10.1145/3397306) (*ECCV 2020 Demo Award Nominee*)
_Fang Hu, Peng He, Songlin Xu, Yin Li, Cheng Zhang_

##### • [2020 FG] Hand tracking from monocular RGB with dense semantic labels. [\[PDF\]](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1kecISCOYgw/pdf)
_Peter Thompson, Aphrodite Galata_

##### • [2020 FG] Generative Model-Based Loss to the Rescue: A Method to Overcome Annotation Errors for Depth-Based Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2007.03073.pdf)
_Jiayi Wang, Franziska Mueller, Florian Bernard, Christian Theobalt_

##### • [2020 IROS] Physics-Based Dexterous Manipulations with Estimated Hand Poses and Residual Reinforcement Learning. [\[PDF\]](https://arxiv.org/pdf/2008.03285)
_Guillermo Garcia-Hernando, Edward Johns, Tae-Kyun Kim_

##### • [2020 CHI] Evaluation of Machine Learning Techniques for Hand Pose Estimation on Handheld Device with Proximity Sensor. [\[PDF\]](https://dl.acm.org/doi/pdf/10.1145/3313831.3376712)
_Kazuyuki Arimatsu, Hideki Mori_

##### • [2020 AAAI] AWR: Adaptive Weighting Regression for 3D Hand Pose Estimation. [\[PDF\]](https://www.aaai.org//Papers//AAAI//2020GB//AAAI-HuangW.4059.pdf)  [\[Code\]](https://github.com/Elody-07/AWR-Adaptive-Weighting-Regression)
_Weiting Huang, Pengfei Ren, Jingyu Wang, Qi Qi, Haifeng Sun_

##### • [2020 WACV] Nonparametric Structure Regularization Machine for 2D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/2001.08869.pdf) [\[Code\]](https://github.com/HowieMa/NSRMhand)
_Yifei Chen\*, Haoyu Ma\*, Deying Kong, Xiangyi Yan, Jianbao Wu, Wei Fan, Xiaohui Xie_

##### • [2020 WACV] 3D Hand Pose Estimation with Disentangled Cross-Modal Latent Space. [\[PDF\]](http://openaccess.thecvf.com/content_WACV_2020/papers/Gu_3D_Hand_Pose_Estimation_with_Disentangled_Cross-Modal_Latent_Space_WACV_2020_paper.pdf)
_Jiajun Gu, Zhiyong Wang, Wanli Ouyang, Weichen Zhang, Jiafeng Li, Li Zhuo_

##### • [2020 WACV] DGGAN: Depth-image Guided Generative Adversarial Networks for Disentangling RGB and Depth Images in 3D Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_WACV_2020/papers/Chen_DGGAN_Depth-image_Guided_Generative_Adversarial_Networks_forDisentangling_RGB_and_Depth_WACV_2020_paper.pdf)
_Liangjian Chen, Shih-Yao Lin, Yusheng Xie, Yen-Yu Lin, Wei Fan, Xiaohui Xie_

##### • [2020 WACV] Rotation-invariant Mixed Graphical Model Network for 2D Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_WACV_2020/papers/Kong_Rotation-invariant_Mixed_Graphical_Model_Network_for_2D_Hand_Pose_Estimation_WACV_2020_paper.pdf)
_Deying Kong, Haoyu Ma, Yifei Chen, Xiaohui Xie_

##### • [2020 ICASSP] Weakly Supervised Segmentation Guided Hand Pose Estimation During Interaction With Unknown Objects. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/9053082)
_Cairong Zhang, Guijin Wang, Xinghao Chen, Pengwei Xie, Toshihiko Yamasaki_

##### • [2020 ICASSP] Hand-3D-Studio: A New Multi-view System for 3D Hand Reconstruction. [\[PDF\]](https://www.yangangwang.com/papers/ZHAO-H3D-2020-02.pdf) [\[Project\]](https://www.yangangwang.com/papers/ZHAO-H3S-2020-02.html)
_Zhengyi Zhao, Tianyao Wang, Siyu Xia, Yangang Wang_

[\[back to top\]](#contents)

### 2019 ICCV

##### • FreiHAND: A Dataset for Markerless Capture of Hand Pose and Shape from Single RGB Images. [\[PDF\]](https://arxiv.org/pdf/1909.04349.pdf)  [\[Project\]](https://lmb.informatik.uni-freiburg.de/projects/freihand/) [\[Code\]](https://github.com/lmb-freiburg/freihand)
_Christian Zimmermann, Duygu Ceylan, Jimei Yang, Bryan Russell, Max Argus, Thomas Brox_

##### • A2J: Anchor-to-Joint Regression Network for 3D Articulated Pose Estimation from a Single Depth Image. [\[PDF\]](https://cse.buffalo.edu/~jsyuan/papers/2019/A2J.pdf) [\[Code\]](https://github.com/zhangboshen/A2J)
_Fu Xiong\*, Boshen Zhang\*, Yang Xiao, Zhiguo Cao, Taidong Yu, Joey Tianyi Zhou, and Junsong Yuan_

##### • Exploiting Spatial-temporal Relationships for 3D Pose Estimation via Graph Convolutional Networks. [\[PDF\]](https://cse.buffalo.edu/~jsyuan/papers/2019/Exploiting_Spatial-temporal_Relationships_for_3D_Pose_Estimation_via_Graph_Convolutional_Networks.pdf)
_Yujun Cai, Liuhao Ge, Jun Liu, Jianfei Cai, Tat-Jen Cham, Junsong Yuan, and Nadia Magnenat Thalmann_

##### • Resolving 3D Human Pose Ambiguities with 3D Scene Constraints. [\[PDF\]](https://ps.is.tuebingen.mpg.de/uploads_file/attachment/attachment/530/ICCV_2019___PROX.pdf)  [\[Project\]](https://prox.is.tue.mpg.de/)
_Mohamed Hassan, Vasileios Choutas, Dimitrios Tzionas and Michael J. Black_

##### • SO-HandNet: Self-Organizing Network for 3D Hand Pose Estimation with Semi-supervised Learning. [\[PDF\]](https://drive.google.com/file/d/11GJzouV6jt_aOpvrJ8l3J5x_R_-m-Lg8/view)  [\[Code\]](https://github.com/TerenceCYJ/SO-HandNet)
_Yujin Chen, Zhigang Tu, Liuhao Ge, Dejun Zhang, Ruizhi Chen, Junsong Yuan_

##### • End-to-end Hand Mesh Recovery from a Monocular RGB Image. [\[PDF\]](https://arxiv.org/pdf/1902.09305.pdf)  [\[Code\]](https://github.com/MandyMo/HAMR)
_Xiong Zhang\*, Qiang Li\*, Wenbo Zhang, Wen Zheng_

##### • Aligning Latent Spaces for 3D Hand Pose Estimation. [\[PDF\]](https://www.mu4yang.com/files/papers/Aligning%20Latent%20Spaces%20for%203D%20Hand%20Pose%20Estimation.pdf)
_Linlin Yang\*, Shile Li\*, Dongheui Lee, Angela Yao_

##### • [HANDS19 Workshop] Disentangling Pose from Appearance in Monochrome Hand Images. [\[PDF\]](https://arxiv.org/pdf/1904.07528.pdf)
_Yikang Li, Chris Twigg, Yuting Ye, Lingling Tao, Xiaogang Wang_

##### • [HANDS19 Workshop] RGB-based 3D Hand Pose Estimation via Privileged Learning with Depth Images. [\[PDF\]](https://arxiv.org/pdf/1811.07376.pdf)
_Shanxin Yuan, Bjorn Stenger, Tae-Kyun Kim_

##### • [HANDS19 Workshop] Explicit Pose Deformation Learning for Tracking Human Poses. [\[PDF\]](https://arxiv.org/pdf/1811.07123.pdf)
_Xiao Sun, Chuankang Li, Stephen Lin_

##### • [HANDS19 Workshop] Hand Pose Ensemble Learning based on Grouping Features of Hand Point Sets. \[PDF\]
_Tianqiang Zhu, Yi Sun, Xiaohong Ma, Xiangbo Lin_

### 2019 CVPR

##### • Disentangling Latent Hands for Image Synthesis and Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Yang_Disentangling_Latent_Hands_for_Image_Synthesis_and_Pose_Estimation_CVPR_2019_paper.pdf)
_Linlin Yang, Angela Yao_

##### • Point-to-Pose Voting based Hand Pose Estimation using Residual Permutation Equivariant Layer. [\[PDF\]](https://arxiv.org/pdf/1812.02050.pdf)
_Shile Li, Dongheui Lee_

##### • H•O: Unified Egocentric Recognition of 3D Hand-Object Poses and Interactions. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Tekin_HO_Unified_Egocentric_Recognition_of_3D_Hand-Object_Poses_and_Interactions_CVPR_2019_paper.pdf)  *(Oral)*
_Bugra Tekin, Federica Bogo, Marc Pollefeys_

##### • Self supervised 3D hand pose estimation. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Wan_Self-Supervised_3D_Hand_Pose_Estimation_Through_Training_by_Fitting_CVPR_2019_paper.pdf) [\[Code\]](https://github.com/melonwan/sphereHand) *(Oral)* *([Best Paper Finalists](http://cvpr2019.thecvf.com/files/CVPR%202019%20-%20Welcome%20Slides%20Final.pdf))*
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### • CrossInfoNet: Multi-Task Information Sharing Based Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Du_CrossInfoNet_Multi-Task_Information_Sharing_Based_Hand_Pose_Estimation_CVPR_2019_paper.pdf) [\[Code\]](https://github.com/dumyy/handpose)
_Kuo Du, Xiangbo Lin, Yi Sun, Xiaohong Ma_

##### • Expressive Body Capture: 3D Hands, Face, and Body from a Single Image.  [\[PDF\]](https://arxiv.org/pdf/1904.05866)  [\[Project\]](https://smpl-x.is.tue.mpg.de/)  [\[Code\]](https://github.com/vchoutas/smplify-x) *(Oral)*
_Georgios Pavlakos\*, Vasileios Choutas\*, Nima Ghorbani, Timo Bolkart, Ahmed A. A. Osman, Dimitrios Tzionas, Michael J. Black_

##### • Learning joint reconstruction of hands and manipulated objects. [\[PDF\]](https://arxiv.org/pdf/1904.05767.pdf) [\[Code\]](https://github.com/hassony2/manopth) [\[Code\]](https://github.com/hassony2/obman_train) [\[Project\]](https://www.di.ens.fr/willow/research/obman/)
_Yana Hasson, Gül Varol, Dimitris Tzionas, Igor Kalevatykh, Michael J. Black, Ivan Laptev, and Cordelia Schmid_

##### • 3D Hand Shape and Pose Estimation from a Single RGB Image. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Ge_3D_Hand_Shape_and_Pose_Estimation_From_a_Single_RGB_CVPR_2019_paper.pdf) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2019) [\[Code\]](https://github.com/3d-hand-shape/hand-graph-cnn) *(Oral)*
_Liuhao Ge, Zhou Ren, Yuncheng Li, Zehao Xue, Yingying Wang, Jianfei Cai, Junsong Yuan_

##### • 3D Hand Shape and Pose from Images in the Wild. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Boukhayma_3D_Hand_Shape_and_Pose_From_Images_in_the_Wild_CVPR_2019_paper.pdf)  [\[Code\]](https://github.com/boukhayma/3dhand) *(Oral)*
_Adnane Boukhayma, Rodrigo de Bem, Philip H.S. Torr_

##### • Pushing the Envelope for RGB-based Dense 3D Hand Pose Estimation via Neural Rendering. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Baek_Pushing_the_Envelope_for_RGB-Based_Dense_3D_Hand_Pose_Estimation_CVPR_2019_paper.pdf)
_Seungryul Baek, Kwang In Kim, Tae-Kyun Kim_

##### • Monocular Total Capture: Posing Face, Body, and Hands in the Wild. [\[PDF\]](http://openaccess.thecvf.com/content_CVPR_2019/papers/Xiang_Monocular_Total_Capture_Posing_Face_Body_and_Hands_in_the_CVPR_2019_paper.pdf) [\[Project\]](http://domedb.perception.cs.cmu.edu/monototalcapture.html) [\[Code\]](https://github.com/CMU-Perceptual-Computing-Lab/MonocularTotalCapture) *(Oral)*
_Donglai Xiang, Hanbyul Joo, Yaser Sheikh_

[\[back to top\]](#contents)

### 2019 Others

##### • [2019 SIGGRAPH] Interactive Hand Pose Estimation using a Stretch-Sensing Soft Glove. [\[PDF\]](https://cims.nyu.edu/gcl/papers/2019-Capacitive.pdf)  [\[Project\]](https://igl.ethz.ch/projects/stretch-glove/)
_Oliver Glauser, Shihao Wu, Daniele Panozzo, Otmar Hilliges, Olga Sorkine-Hornung_

##### • [2019 SIGGRAPH] InteractionFusion: Real-time Reconstruction of Hand Poses and Deformable Objects in Hand-object Interactions. [\[PDF\]](https://dl.acm.org/citation.cfm?id=3322998)
_Hao Zhang, Zi-Hao Bo, Jun-Hai Yong, Feng Xu_

##### • [2019 SIGGRAPH] Real-time pose and shape reconstruction of two interacting hands with a single depth camera. [\[PDF\]](https://handtracker.mpi-inf.mpg.de/projects/TwoHands/content/TwoHands_SIGGRAPH2019.pdf) [\[Project\]](https://handtracker.mpi-inf.mpg.de/projects/TwoHands/)
_Franziska Mueller, Micah Davis, Florian Bernard, Oleksandr Sotnychenko, Mickeal Verschoor, Miguel A. Otaduy, Dan Casas, Christian Theobalt_

##### • [2019 FG] Deep Conditional Variational Estimation for Depth-Based Hand Poses. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8756559)
_Lu Xu, Chen Hu, Yinqi Li, Ji’an Tao, Jianru Xue, Kuizhi Mei_

##### • [2019 BMVC] Unified 2D and 3D Hand Pose Estimation from a Single Visible or X-ray Image. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0931-paper.pdf)
_Akila Pemasiri, Kien Nguyen Thanh, Sridha Sridharan, Clinton Fookes_

##### • [2019 BMVC] TAGAN: Tonality Aligned Generative Adversarial Networks for Realistic HandPose Synthesis. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0408-paper.pdf)
_Liangjian Chen, Shih-Yao Lin, Yusheng Xie, Hui Tang, Yufan Xue, Xiaohui Xie, Yen-Yu Lin, Wei Fan_

##### • [2019 BMVC] Single Image 3D Hand Reconstruction with Mesh Convolutions. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0653-paper.pdf) [\[Code\]](https://github.com/dkulon/hand-reconstruction)
_Dominik Kulon, Haoyang Wang, Riza Alp Güler, Michael Bronstein, Stefanos Zafeiriou_

##### • [2019 BMVC] Adaptive Graphical Model Network for 2D Handpose Estimation. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0907-paper.pdf)
_Deying Kong, Yifei Chen, Haoyu Ma, Xiangyi Yan, Xiaohui Xie_

##### • [2019 BMVC] SRN: Stacked Regression Network for Real-time 3D Hand Pose Estimation. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0918-paper.pdf)
_Pengfei Ren, Haifeng Sun, Jingyu Wang, Qi Qi, Weiting Huang_

##### • [2019 BMVC] End-to-End 3D Hand Pose Estimation from Stereo Cameras. [\[PDF\]](https://bmvc2019.org/wp-content/uploads/papers/0219-paper.pdf)  *(Oral)*
_Yuncheng Li, Zehao Xue, Yingying Wang, Liuhao Ge, Zhou Ren, Jonathan Rodriguez_

##### • [2019 ACCV] Hand Pose Estimation Based on 3D Residual Network with Data Padding and Skeleton Steadying. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-20873-8_19)
_Pai-Wen Ting, En-Te Chou, Ya-Hui Tang, Li-Chen Fu_

##### • [2019 ICASSP] Cascaded Point Network for 3D Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8683356)
_Yikun Dou, Xuguang Wang, Yuying Zhu, Xiaoming Deng, Cuixia Ma, Liang Chang, Hongan Wang_

##### • [2019 ICASSP] A Novel Framework of Hand Localization and Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8682382)
_Yunlong Che, Yuxiang Song, Yue Qi_

##### • [2019 ICRA] Vision-based Teleoperation of Shadow Dexterous Hand using End-to-End Deep Neural Network. [\[PDF\]](https://arxiv.org/pdf/1809.06268.pdf) [\[Code\]](https://github.com/TAMS-Group/TeachNet_Teleoperation)
_Shuang Li\*, Xiaojian Ma\*, Hongzhuo Liang, Michael Görner, Philipp Ruppel, Bing Fang, Fuchun Sun, Jianwei Zhang_

##### • [2019 WACV] MURAUER: Mapping Unlabeled Real Data for Label AUstERity. [\[PDF\]](https://poier.github.io/murauer/documents/poier2019wacv_selfpublishing.pdf) [\[Project\]](https://poier.github.io/murauer/) [\[Code\]](https://github.com/poier/murauer)
_Georg Poier, Michael Opitz, David Schinagl and Horst Bischof_

[\[back to top\]](#contents)

### 2018 ECCV

##### • HandMap: Robust Hand Pose Estimation via Intermediate Dense Guidance Map Supervision. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Xiaokun_Wu_HandMap_Robust_Hand_ECCV_2018_paper.pdf)  [\[Project\]](https://xkunwu.github.io/research/18HandPose/18HandPose)  [\[Code\]](https://github.com/xkunwu/depth-hand)
_Xiaokun Wu, Daniel Finnegan, Eamonn O'Neill, Yongliang Yang_

##### • HBE: Hand Branch Ensemble network for real time 3D hand pose estimation.  [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Yidan_Zhou_HBE_Hand_Branch_ECCV_2018_paper.pdf)
_Yidan Zhou, Jian Lu, Kuo Du, Xiangbo Lin, Yi Sun, Xiaohong Ma_

##### • Point-to-Point Regression PointNet for 3D Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Liuhao_Ge_Point-to-Point_Regression_PointNet_ECCV_2018_paper.pdf)
_Liuhao Ge, Zhou Ren, Junsong Yuan_

##### • Weakly-supervised 3D Hand Pose Estimation from Monocular RGB Images. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Yujun_Cai_Weakly-supervised_3D_Hand_ECCV_2018_paper.pdf) *(Oral)*
_Yujun Cai, Liuhao Ge, Jianfei Cai, Junsong Yuan_

##### • Joint 3D tracking of a deformable object in interaction with a hand. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Aggeliki_Tsoli_Joint_3D_tracking_ECCV_2018_paper.pdf)  [\[Project\]](https://www.ics.forth.gr/cvrl/deformable_interaction/)
_Aggeliki Tsoli, Antonis A. Argyros_

##### • Occlusion-aware Hand Pose Estimation Using Hierarchical Mixture Density Network. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Qi_Ye_Occlusion-aware_Hand_Pose_ECCV_2018_paper.pdf)  *(Oral)*
_Qi Ye, Tae-Kyun Kim_

##### • Hand Pose Estimation via Latent 2.5D Heatmap Regression. [\[PDF\]](http://openaccess.thecvf.com/content_ECCV_2018/papers/Umar_Iqbal_Hand_Pose_Estimation_ECCV_2018_paper.pdf)
_Umar Iqbal, Pavlo Molchanov, Thomas Breuel, Juergen Gall, Jan Kautz_

##### • [Hands18 Workshop] Adapting Egocentric Visual Hand Pose Estimation Towards a Robot-Controlled Exoskeleton. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-11024-6_16)
_Gerald Baulig, Thomas Gulde, Cristobal Curio_

##### • [Hands18 Workshop] Estimating 2D Multi-Hand Poses From Single Depth Images. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-11024-6_17)
_Le Duan, Minmin Shen, Song Cui, Zhexiao Guo, Oliver Deussen_

##### • [Hands18 Workshop] Task-Oriented Hand Motion Retargeting for Dexterous Manipulation Imitation. [\[PDF\]](https://arxiv.org/pdf/1810.01845.pdf) [\[Project\]](https://daphneantotsiou.github.io/task-oriented-retargeting.html)
_Dafni Antotsiou, Guillermo Garcia-Hernando, Tae-Kyun Kim_

[\[back to top\]](#contents)

### 2018 CVPR

##### • First-Person Hand Action Benchmark with RGB-D Videos and 3D Hand Pose Annotations. [\[PDF\]](https://arxiv.org/pdf/1704.02463.pdf) [\[Project\]](https://guiggh.github.io/publications/first-person-hands/)  [\[Code\]](https://github.com/guiggh/hand_pose_action)
*Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, Tae-Kyun Kim*


##### • Learning Pose Specific Representations by Predicting Different Views. [\[PDF\]](https://arxiv.org/pdf/1804.03390.pdf)  [\[Project\]](https://poier.github.io/PreView/)  [\[Code\]](https://github.com/poier/PreView)
_Georg Poier, David Schinagl, Horst Bischof_

##### • Hand PointNet: 3D Hand Pose Estimation using Point Sets. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Ge_Hand_PointNet_3D_CVPR_2018_paper.pdf)  [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2018) [\[Code\]](https://sites.google.com/site/geliuhaontu/HandPointNet.zip?attredirects=0&d=1) *(Spotlight)*
_Liuhao Ge, Yujun Cai, Junwu Weng, Junsong Yuan_

##### • Dense 3D Regression for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1711.08996.pdf)  [\[Code\]](https://github.com/melonwan/denseReg)
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### • Cross-modal Deep Variational Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1803.11404) [\[Project\]](https://ait.ethz.ch/projects/2018/vae_hands/) [\[Code\]](https://github.com/spurra/vae-hands-3d) *(Spotlight)*
_Adrian Spurr, Jie Song, Seonwook Park, Otmar Hilliges_

##### • Feature Mapping for Learning Fast and Accurate 3D Pose Inference from Synthetic Images. [\[PDF\]](https://arxiv.org/pdf/1712.03904.pdf)  [\[Project\]](https://www.tugraz.at/institute/icg/research/team-lepetit/research-projects/feature-mapping/)
_Mahdi Rad, Markus Oberweger, Vincent Lepetit_

##### • GANerated Hands for Real-Time 3D Hand Tracking from Monocular RGB. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018.pdf) [\[Supp\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018_Supp.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/) *(Spotlight)*
_Franziska Mueller, Florian Bernard, Oleksandr Sotnychenko, Dushyant Mehta, Srinath Sridhar, Dan Casas, Christian Theobalt_


##### • V2V-PoseNet: Voxel-to-Voxel Prediction Network for Accurate 3D Hand and Human Pose Estimation from a Single Depth Map. [\[PDF\]](https://arxiv.org/pdf/1711.07399.pdf) [\[Code\]](https://github.com/mks0601/V2V-PoseNet_RELEASE)
_Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee_

##### • Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals. [\[PDF\]](https://arxiv.org/pdf/1712.03917.pdf) *(Spotlight)*
_Shanxin Yuan, Guillermo Garcia-Hernando, Bjorn Stenger, Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee, Pavlo Molchanov, Jan Kautz, Sina Honari, Liuhao Ge, Junsong Yuan, Xinghao Chen, Guijin Wang, Fan Yang, Kai Akiyama, Yang Wu, Qingfu Wan, Meysam Madadi, Sergio Escalera, Shile Li, Dongheui Lee, Iason Oikonomidis, Antonis Argyros, Tae-Kyun Kim_

##### • Augmented skeleton space transfer for depth-based hand pose estimation. [\[PDF\]](https://arxiv.org/pdf/1805.04497.pdf) *(Oral)*
_Seungryul Baek, Kwang In Kim, Tae-Kyun Kim_

##### • [\[3D HUMANS Workshop\]](https://project.inria.fr/humans2018/) Monocular RGB Hand Pose Inference From Unsupervised Refinable Nets. [\[PDF\]](http://openaccess.thecvf.com/CVPR2018_workshops/content_CVPR_2018/papers/w17/Dibra_Monocular_RGB_Hand_CVPR_2018_paper.pdf)
_Endri Dibra, Silvan Melchior, Ali Balkis, Thomas Wolf, Cengiz Oztireli, Markus Gross_

[\[back to top\]](#contents)

### 2018 Others

##### • [2018 ISMAR] Hybrid 3D Hand Articulations Tracking Guided by Classification and Search Space Adaptation. [\[PDF\]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8613751)
_Gabyong Park, Woontack Woo_

##### • [2018 ACCV] Hand Pose Estimation based on 3D Residual Network with Data Padding and Skeleton Steadying. \[PDF\]
_Pai-Wen Ting, En-Te Chou, Ya-Hui Tang, Li-Chen Fu_

##### • [2018 ACCV] Partially Occluded Hands: A challenging new dataset for single-image hand pose estimation. [\[PDF\]](https://cbmm.mit.edu/sites/default/files/publications/partially-occluded-hands-6.pdf) [\[Project\]](http://occludedhands.com/)  *(Oral)*
_Battushig Myanganbayar, Cristina Mata, Gil Dekel, Boris Katz, Guy Ben-Yosef, Andrei Barbu_

##### • [2018 ACCV] Domain Transfer for 3D Pose Estimation from Color Images without Manual Annotations. [\[PDF\]](https://arxiv.org/pdf/1810.03707.pdf)  *(Oral)*
_Mahdi Rad, Markus Oberweger, Vincent Lepetit_

##### • [2018 PCM] Hand Pose Estimation with Attention-and-Sequence Network. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_51)
_Tianping Hu\*, Wenhai Wang\*, Tong Lu_

##### • [2018 PCM] Mutiple Transfer Net with Region Ensemble for Deep Hand Pose Estimation. [\[PDF\]](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_58)
_Haoqian Wang, Da Li, Xingzheng Wang_

##### • [2018 ICPR] Local Regression Based Hourglass Network for Hand Pose Estimation from a Single Depth Image. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8545460)
_Jia Li, Zengfu Wang_

##### • [2018 ICPR] Dynamic Projected Segmentation Networks for Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8546330)
_Yunlong Che, Yue Qi_

##### • [2018 3DV] DeepHPS: End-to-end Estimation of 3D Hand Pose and Shape by Learning from Synthetic Depth. [\[PDF\]](https://arxiv.org/pdf/1808.09208.pdf)
_Jameel Malik, Ahmed Elhayek, Fabrizio Nunnari, Kiran Varanasi, Kiarash Tamaddon, Alexis Heloir, Didier Stricker_

##### • [2018 ICIP] Networks Effectively Utilizing 2D Spatial Information for Accurate 3D Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8451509/)
_Baoen Liu, Shiliang Huang, Zhongfu Ye_

##### • [2018 ICIP] On the Fusion of RGB and Depth Information For Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/document/8451022/) [\[Code\]](https://github.com/ekazakos/fusenet-hand-pose)
_Evangelos Kazakos, Christophoros Nikou, Ioannis Kakadiaris_

##### • [2018 ICIP] Fast Lifting for 3D Hand Pose Estimation in AR/VR Applications. [\[PDF\]](https://drive.google.com/file/d/1kbNSb0ySAkhpQ6ntxPhs0wPvFDbsGu8v/view)
_Onur Guleryuz, Christine Kaeser-Chen_

##### • [2018 BMVC] Structure-Aware 3D Hourglass Network for Hand Pose Estimation from Single Depth Image. [\[PDF\]](http://bmvc2018.org/papers/1133.pdf)
_Fuyang Huang, Ailing Zeng, Minhao Liu, Jing Qin, Qiang Xu_

##### • [2018 BMVC] 3D Hand Pose Estimation using Simulation and Partial-Supervision with a Shared Latent Space. [\[PDF\]](https://arxiv.org/pdf/1807.05380.pdf) [\[Code\]](https://github.com/masabdi/LSPS) *(Oral)*
_Masoud Abdi, Ehsan Abbasnejad, Chee Peng Lim, Saeid Nahavandi_

##### • [2018 FG] Kinematic Constrained Cascaded Autoencoder for Real-time Hand Pose Estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/8373810/)
_Yushun Lin, Xiujuan Chai, Xilin Chen_

##### • [2018 WACV] Using a single RGB frame for real time 3D hand pose estimation in the wild. [\[PDF\]](https://arxiv.org/pdf/1712.03866.pdf)  [\[Project\]](http://users.ics.forth.gr/~argyros/res_rgbmonohand.html) [\[Code\]](https://github.com/FORTH-ModelBasedTracker/MonocularRGB_3D_Handpose_WACV18)
_Paschalis Panteleris, Iason Oikonomidis, Antonis Argyros_

[\[back to top\]](#contents)

### 2017 ICCV
##### • Learning to Estimate 3D Hand Pose from Single RGB Images. [\[PDF\]](https://arxiv.org/pdf/1705.01389.pdf)  [\[Project\]](https://lmb.informatik.uni-freiburg.de/projects/hand3d/)   [\[Code\]](https://github.com/lmb-freiburg/hand3d)
_Christian Zimmermann, Thomas Brox_

##### • Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/)
*Franziska Mueller, Dushyant Mehta, Oleksandr Sotnychenko, Srinath Sridhar, Dan Casas, Christian Theobalt*

##### • Robust Hand Pose Estimation during the Interaction with an Unknown Object. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Robust_Hand_Pose_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Robust_Hand_Pose_ICCV_2017_supplemental.pdf) [\[Project\]](https://engineering.purdue.edu/cdesign/wp/robust-hand-pose-estimation-during-the-interaction-with-an-unknown-object/)
*Chiho Choi, Sang Ho Yoon, Chin-Ning Chen, Karthik Ramani*

##### • Learning Hand Articulations by Hallucinating Heat Distribution. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Learning_Hand_Articulations_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Learning_Hand_Articulations_ICCV_2017_supplemental.pdf)  [\[Project\]](https://engineering.purdue.edu/cdesign/wp/learning-hand-articulations-by-hallucinating-heat-distribution/)
*Chiho Choi, Sangpil Kim, Karthik Ramani*

##### • Low-Dimensionality Calibration through Local Anisotropic Scaling for Robust Hand Model Personalization. [\[PDF\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/index.php) [\[Code\]](https://github.com/edoRemelli/hadjust)
_Edoardo Remelli*, Anastasia Tkach*, Andrea Tagliasacchi, Mark Pauly_

##### • [Hands17 Workshop] Back to RGB: 3D tracking of hands and hand-object interactions based on short-baseline stereo. [\[PDF\]](https://arxiv.org/pdf/1705.05301.pdf)
_Paschalis Panteleris, Antonis Argyros_

##### • [Hands17 Workshop] DeepPrior++: Improving Fast and Accurate 3D Hand Pose Estimation. [\[PDF\]](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_lepetit/publications/oberweger_iccvw17.pdf) [\[Project\]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) [\[Code\]](https://github.com/moberweger/deep-prior-pp)
*Markus Oberweger and Vincent Lepetit*

##### • [Hands17 Workshop] Hand Pose Estimation Using Deep Stereovision and Markov-chain Monte Carlo. [\[PDF\]](http://openaccess.city.ac.uk/18087/1/BasaruICCVW2017_MCMC.pdf)
*Rilwan Remilekun Basaru, Chris Child, Eduardo Alonso, Greg Slabaugh*

[\[back to top\]](#contents)

### 2017 CVPR
##### • Hand Keypoint Detection in Single Images using Multiview Bootstrapping. [\[PDF\]](https://arxiv.org/pdf/1704.07809) [\[Project\]](http://www.cs.cmu.edu/~tsimon/projects/mvbs.html) [\[Code\]](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
*Tomas Simon, Hanbyul Joo, Iain Matthews, Yaser Sheikh*

##### • Crossing Nets: Combining GANs and VAEs with a Shared Latent Space for Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wan_Crossing_Nets_Combining_CVPR_2017_paper.pdf) [\[Code\]](https://github.com/melonwan/crossingNet)
*Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao*

##### • Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis. [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)
_Shanxin Yuan\*, Qi Ye\*, Bjorn Stenger, Siddhand Jain, Tae-Kyun Kim_

##### • 3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Ge_3D_Convolutional_Neural_CVPR_2017_paper.pdf) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2017)
*Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann*

[\[back to top\]](#contents)

### 2017 Others

##### • [2017 3DV] Simultaneous Hand Pose and Skeleton Bone-Lengths Estimation from a Single Depth Image. [\[PDF\]](https://arxiv.org/pdf/1712.03121.pdf)
_Jameel Malik, Ahmed Elhayek, Didier Stricker_

##### • [2017 3DV] How to Refine 3D Hand Pose Estimation from Unlabelled Depth Data? [\[PDF\]](https://graphics.ethz.ch/~edibra/Publications/How%20to%20Refine%203D%20Hand%20Pose%20Estimation%20from%20Unlabelled%20Depth%20Data.pdf)
_Endri Dibra\*, Thomas Wolf\*, Cengiz Öztireli, Markus Gross_

##### • [2017 ICIP] Region Ensemble Network: Improving Convolutional Network for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1702.02447.pdf)  [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
*Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang, Fei Qiao, Huazhong Yang*

##### • [2017 ICIP] A Hand Pose Tracking Benchmark from Stereo Matching. [\[PDF\]](http://www.cs.cityu.edu.hk/~jianbjiao2/pdfs/icip.pdf)  [\[Project\]](https://sites.google.com/site/zhjw1988/)
*Jiawei Zhang, Jianbo Jiao, Mingliang Chen, Liangqiong Qu, Xiaobin Xu, and Qingxiong Yang*

##### • [2017 SIGGRAPH Asia] Articulated distance fields for ultra-fast tracking of hands interacting. [\[PDF\]](https://dl.acm.org/citation.cfm?id=3130853)
_Jonathan Taylor\*, Vladimir Tankovich\*, Danhang Tang\*, Cem Keskin\*, David Kim, Philip Davidson, Adarsh Kowdle, Shahram Izadi_

##### • [2017 SIGGRAPH Asia] Online Generative Model Personalization for Hand Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2017/HOnline/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2017/HOnline/index.php)
_Anastasia Tkach\*, Andrea Tagliasacchi\*, Edoardo Remelli, Mark Pauly, Andrew Fitzgibbon_

##### • [2017 SIGGRAPH Asia] Embodied Hands: Modeling and Capturing Hands and Bodies Together. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/392/Embodied_Hands_SiggraphAsia2017.pdf)  [\[Project\]](http://ps.is.tue.mpg.de/publications/embodiedhands)
_Javier Romero\*, Dimitrios Tzionas\* and Michael J. Black_

##### • [2017 BMVC] Hand Pose Learning: Combining Deep Learning and Hierarchical Refinement for 3D Hand Pose Estimation. [\[PDF\]](https://www.dropbox.com/s/3y96pnutxum3p4v/0569.pdf?dl=1)
*Min-Yu Wu, Ya Hui Tang, Pai-Wei Ting and Li-Chen Fu*

##### • [2017 BMVC] Generative 3D Hand Tracking with Spatially Constrained Pose Sampling. [\[PDF\]](http://users.ics.forth.gr/~argyros/mypapers/2017_09_BMVC_RDSRoditak.pdf) [\[Project\]](http://users.ics.forth.gr/~argyros/res_handRDS.html)
*Konstantinos Roditakis, Alexandros Makris and Antonis Argyros*

##### • [2017 ICRA] Learning a deep network with spherical part model for 3D hand pose estimation. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7989303)
*Tzu-Yang Chen, Pai-Wen Ting, Min-Yu Wu, Li-Chen Fu*

##### • [2017 FG] Occlusion aware hand pose recovery from sequences of depth images. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961746) [\[Slide\]](http://sergioescalera.com/wp-content/uploads/2017/06/FG2017Hand.pdf)
*Meysam Madadi, Sergio Escalera, Alex Carruesco Llorens, Carlos Andujar, Xavier Baro, Jordi Gonzalez*

##### • [2017 FG] 3D Hand-Object Pose Estimation from Depth with Convolutional Neural Networks. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961770) [\[Project\]](http://www.cs.man.ac.uk/~goudied/research.html)
*Duncan Goudie, Aphrodite Galata*

[\[back to top\]](#contents)

### 2016 ECCV
##### • Spatial Attention Deep Net with Partial PSO for Hierarchical Hybrid Hand Pose Estimation. [\[PDF\]](https://labicvl.github.io/docs/pubs/Qi_Shanxin_ECCV_2016.pdf) [\[Project\]](https://sites.google.com/site/qiyeincv/home/eccv2016)
_Qi Ye\*, Shanxin Yuan\*, Tae-Kyun Kim_

##### • Hand Pose Estimation from Local Surface Normals. [\[PDF\]](http://www.vision.ee.ethz.ch/~yaoa/pdfs/wan_eccv16.pdf)
*Chengde Wan, Angela Yao, and Luc Van Gool*

##### • Real-time Joint Tracking of a Hand Manipulating an Object from RGB-D Input. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/content/RealtimeHO_ECCV2016.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/)
*Srinath Sridhar, Franziska Mueller, Michael Zollhöfer, Dan Casas, Antti Oulasvirta, Christian Theobalt*

[\[back to top\]](#contents)

### 2016 CVPR
##### • Robust 3D Hand Pose Estimation in Single Depth Images: From Single-View CNN to Multi-View CNNs. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2016/papers/Ge_Robust_3D_Hand_CVPR_2016_paper.pdf) [\[Project\]](https://sites.google.com/site/geliuhaontu/home/cvpr2016) [\[Code\]](https://github.com/geliuhao/CVPR2016_HandPoseEstimation)
*Liuhao Ge, Hui Liang, Junsong Yuan, Daniel Thalmann*

##### • DeepHand: Robust Hand Pose Estimation by Completing a Matrix Imputed With Deep Features.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Sinha_DeepHand_Robust_Hand_CVPR_2016_paper.pdf)[\[Project\]](https://engineering.purdue.edu/cdesign/wp/deephand-robust-hand-pose-estimation/)
_Ayan Sinha\*, Chiho Choi\*, Karthik Ramani_

##### • Efficiently Creating 3D Training Data for Fine Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvpr16.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/semi-auto-anno)
*Markus Oberweger, Gernot Riegler, Paul Wohlhart, Vincent Lepetit*

##### • Fits Like a Glove: Rapid and Reliable Hand Shape Personalization.  [\[PDF\]](http://www.samehkhamis.com/tan-cvpr2016.pdf) [\[Project\]](http://campar.in.tum.de/Main/DavidTan)
*David Joseph Tan, Thomas Cashman, Jonathan Taylor, Andrew Fitzgibbon, Daniel Tarlow, Sameh Khamis, Shahram Izadi, Jamie Shotton*

[\[back to top\]](#contents)

### 2016 Others

##### • [2016 NIPS] DISCO Nets : Dissimilarity Coefficient Networks. [\[PDF\]](http://www.robots.ox.ac.uk/~diane/DISCONET_camera_ready.pdf) [\[Project\]](http://www.robots.ox.ac.uk/~diane/DiscoNets.html) [\[Code\]](https://github.com/oval-group/DISCONets)
*Diane Bouchacourt, M. Pawan Kumar, Sebastian Nowozin*

##### • \[2016 ACCV\] Hand Pose Regression via A Classification-guided Approach. [\[PDF\]](http://staff.ustc.edu.cn/~juyong/Papers/HandTracking-2016.pdf)
*Hongwei Yang, Juyong Zhang*

##### • \[2016 ICPR\] Deep learning for integrated hand detection and pose estimation. [\[PDF\]](https://ieeexplore.ieee.org/abstract/document/7899702/)
*Tzu-Yang Chen, Min-Yu Wu, Yu-Hsun Hsieh, Li-Chen Fu*

##### • \[2016 ICPR\] Depth-based 3D hand pose tracking. [\[PDF\]](http://ieeexplore.ieee.org/abstract/document/7900051)
*Kha Gia Quach, Chi Nhan Duong, Khoa Luu, and Tien D. Bui.*

##### • \[2016 IJCAI\] Model-based Deep Hand Pose Estimation. [\[PDF\]](http://xingyizhou.xyz/zhou2016model.pdf) [\[Project\]](http://xingyizhou.xyz/) [\[Code\]](https://github.com/tenstep/DeepModel)
*Xingyi Zhou, Qingfu Wan, Wei Zhang, Xiangyang Xue, Yichen Wei*

##### • \[2016 SIGGRAPH\] Efficient and precise interactive hand tracking through joint, continuous optimization of pose and correspondences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/SIGGRAPH2016-SmoothHandTracking.pdf)
*Jonathan Taylor et al.*

##### • \[2016 SIGGRAPH Asia\] Sphere-Meshes for Real-Time Hand Modeling and Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2016/HModel/paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2016/HModel/index.php) [\[Code\]](https://github.com/OpenGP/hmodel)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

[\[back to top\]](#contents)

### 2015 ICCV
##### • Training a Feedback Loop for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_iccv15.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### • Opening the Black Box: Hierarchical Sampling Optimization for Estimating Human Hand Pose.  [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_ICCV_2015.pdf)
*Danhang Tang, Jonathan Taylor, Pushmeet Kohli, Cem Keskin, Tae-Kyun Kim, Jamie Shotton*

##### • Depth-based hand pose estimation: data, methods, and challenges. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Supancic_Depth-Based_Hand_Pose_ICCV_2015_paper.pdf) [\[Project\]](http://arrummzen.net/#HandData) [\[Code\]](https://github.com/jsupancic/deep_hand_pose)
*James Supancic III, Deva Ramanan, Gregory Rogez, Yi Yang, Jamie Shotton*

##### • 3D Hand Pose Estimation Using Randomized Decision Forest with Segmentation Index Points. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Li_3D_Hand_Pose_ICCV_2015_paper.pdf)
*Peiyi Li, Haibin Ling*

##### • A collaborative filtering approach to real-time hand pose estimation. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2015/08/iccv_2015_hand_pose_estimation.pdf) [\[Project\]](https://engineering.purdue.edu/cdesign/wp/a-collaborative-filtering-approach-to-real-time-hand-pose-estimation/)
*Chiho Choi, Ayan Sinha, Joon Hee Choi, Sujin Jang, Karthik Ramani*

##### • Lending A Hand: Detecting Hands and Recognizing Activities in Complex Egocentric Interactions. [\[PDF\]](http://homes.sice.indiana.edu/sbambach/papers/iccv-egohands.pdf)
*Sven Bambach, Stefan Lee, David Crandall, Chen Yu*

##### • Understanding Everyday Hands in Action from RGB-D Images. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Rogez_Understanding_Everyday_Hands_ICCV_2015_paper.pdf)
*Gregory Rogez, James Supancic III, Deva Ramanan*

[\[back to top\]](#contents)

### 2015 CVPR
##### • Cascaded Hand Pose Regression.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf)
*Xiao Sun, Yichen Wei, Shuang Liang, Xiaoou Tang, and Jian Sun*

##### • Fast and Robust Hand Tracking Using Detection-Guided Optimization. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/content/FastHandTracker_CVPR2015.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/)
*Srinath Sridhar, Franziska Mueller, Antti Oulasvirta, Christian Theobalt*

##### • Learning an Efficient Model of Hand Shape Variation from Depth Images. [\[PDF\]](http://www.samehkhamis.com/khamis-cvpr2015.pdf)
*Sameh Khamis, Jonathan Taylor, Jamie Shotton, Cem Keskin, Shahram Izadi, Andrew Fitzgibbon*

[\[back to top\]](#contents)

### 2015 Others

##### • \[2015 BMVC\] Hybrid One-Shot 3D Hand Pose Estimation by Exploiting Uncertainties. [\[PDF\]](https://arxiv.org/pdf/1510.08039.pdf) [\[Project\]](https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/hybridhpe/)
*Georg Poier, Konstantinos Roditakis, Samuel Schulter, Damien Michel, Horst Bischof and Antonis A. Argyros*

##### • \[2015 BMVC\] Rule of Thumb: Deep Derotation for Improved Fingertip Detection. [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf) [\[Project\]](http://www.cs.technion.ac.il/~twerd/HandNet/)
*Aaron Wetzler, Ron Slossberg and Ron Kimmel*

##### • \[2015 CHI\] Accurate, Robust, and Flexible Real-time Hand Tracking. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/publication/accurate-robust-and-flexible-real-time-hand-tracking/)
*Toby Sharp, Cem Keskin, Duncan Robertson, Jonathan Taylor, Jamie Shotton, David Kim, Christoph Rhemann, Ido Leichter, Alon Vinnikov, Yichen Wei, Daniel Freedman, Pushmeet Kohli, Eyal Krupka, Andrew Fitzgibbon, Shahram Izadi*

##### • \[2015 CVWW\] Hands Deep in Deep Learning for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvww15.pdf) [\[Project\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/deep-prior)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### • \[2015 FG\] Combining Discriminative and Model Based Approaches for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/final_fg2015.pdf) [\[Project\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### • \[2015 SGP\] Robust Articulated-ICP for Real-Time Hand Tracking. [\[PDF\]](http://gfx.uvic.ca/pubs/2015/htrack//paper.pdf)  [\[Project\]](http://lgg.epfl.ch/publications/2015/Htrack_ICP/index.php) [\[Code\]](https://github.com/OpenGP/htrack)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

[\[back to top\]](#contents)

### 2014 CVPR
##### • Realtime and robust hand tracking from depth. [\[PDF\]](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/yichenw-cvpr14_handtracking.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/people/yichenw/)
*Chen Qian, Xiao Sun, Yichen Wei, Xiaoou Tang and Jian Sun*

##### • Latent regression forest: Structured estimation of 3d articulated hand posture. [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_CVPR_2014.pdf) [\[Project\]](https://labicvl.github.io/hand.html)
*Danhang Tang, Hyung Jin Chang, Alykhan Tejani, T-K. Kim*

##### • User-specific hand modeling from monocular depth sequences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CVPR2014-UserSpecificHandModeling.pdf) [\[Project\]](https://www.microsoft.com/en-us/research/publication/user-specific-hand-modeling-from-monocular-depth-sequences/)
*Jonathan Taylor, Richard Stebbing, Varun Ramakrishna, Cem Keskin, Jamie Shotton, Shahram Izadi, Aaron Hertzmann, Andrew Fitzgibbon*

##### • Evolutionary Quasi-random Search for Hand Articulations Tracking. [\[PDF\]](https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Oikonomidis_Evolutionary_Quasi-random_Search_2014_CVPR_paper.pdf) [\[Project\]](http://users.ics.forth.gr/~oikonom/pb/publications)
*Iason Oikonomidis, Manolis IA Lourakis, Antonis A Argyros*

[\[back to top\]](#contents)

### 2014 Others & Before
##### • \[2014 SIGGRAPH\] Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks. [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf) [\[Project\]](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm)
*Jonathan Tompson, Murphy Stein, Yann Lecun and Ken Perlin*

##### • \[2013 ICCV\] Real-time Articulated Hand Pose Estimation using Semi-supervised Transductive Regression Forests. [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_ICCV_2013.pdf) [\[Project\]](https://labicvl.github.io/hand.html)
*Danhang Tang, Tsz Ho Yu and T-K. Kim*

##### • \[2013 ICCV\] Interactive Markerless Articulated Hand Motion Tracking Using RGB and Depth Data. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf) [\[Project\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/)
*Srinath Sridhar, Antti Oulasvirta, Christian Theobalt*

##### • \[2013 ICCV\] Efficient Hand Pose Estimation from a Single Depth Image. [\[PDF\]](http://web.bii.a-star.edu.sg/~xuchi/pdf/iccv2013.pdf) [\[Project\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)
*Chi Xu, Li Cheng*

##### • \[2012 ECCV\] Motion Capture of Hands in Action using Discriminative Salient Points. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/76/jgall_handcapture_eccv12.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/btgg12)
*Ballan, L. and Taneja, A. and Gall, J. and van Gool, L. and Pollefeys, M.*

##### • \[2012 ECCV\] Hand pose estimation and hand shape classification using multi-layered randomized decision forests.
*Cem KeskinFurkan, KıraçYunus Emre, KaraLale Akarun*

##### • \[2011 CVPRW\] Real Time Hand Pose Estimation using Depth Sensors. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf)
*Cem Keskin, Furkan Kırac, Yunus Emre Kara, Lale Akarun*

##### • \[2011 BMVC\] Efficient Model-based 3D Tracking of Hand Articulations using Kinect. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf) [\[Project\]](http://users.ics.forth.gr/~argyros/research/kinecthandtracking.htm) [\[Code\]](https://github.com/FORTH-ModelBasedTracker/HandTracker)
*Iason Oikonomidis, Nikolaos Kyriazis, Antonis A. Argyros*

[\[back to top\]](#contents)

## Theses

##### • \[2020\] Learning without Labeling for 3D Hand Pose Estimation. [\[PDF\]](https://diglib.tugraz.at/learning-without-labeling-for-3d-hand-pose-estimation-2020)
*[Georg Poier](https://poier.github.io/), Graz University of Technology*

##### • \[2018\] Computational Learning for Hand Pose Estimation. [\[PDF\]](https://docs.lib.purdue.edu/dissertations/AAI10743663/)
*[Chiho Choi](http://www.chihochoi.me/), Purdue University*

##### • \[2018\] 3D hand pose estimation: methods, datasets, and challenges. [\[PDF\]](https://spiral.imperial.ac.uk/handle/10044/1/70791)
*[Shanxin Yuan](https://sites.google.com/site/shanxinyuan/), Imperial College London*

##### • \[2018\] 3D hand pose estimation using convolutional neural networks. [\[PDF\]](https://spiral.imperial.ac.uk/bitstream/10044/1/68489/1/Ye-Q-2019-PhD-thesis.pdf)
*[Qi Ye](https://sites.google.com/site/qiyeincv/), Imperial College London*

##### • \[2018\] 3D Hand Pose Estimation from Images for Interactive Applications. [\[PDF\]](http://diglib.tugraz.at/download.php?id=5c4a489d042d4&location=aleph)
*[Markus Oberweger](https://moberweger.github.io/), Graz University of Technology*

##### • \[2018\] Articulated Human Pose Estimation in Unconstrained Images and Videos. [\[PDF\]](http://hss.ulb.uni-bonn.de/2018/5292/5292.pdf)
*[Umar Iqbal](http://www.umariqbal.info/), University of Bonn*

##### • \[2018\] Real-Time Generative Hand Modeling and Tracking. [\[PDF\]](https://infoscience.epfl.ch/record/256674/files/EPFL_TH8573.pdf)
*Anastasia Tkach, EPFL*

##### • \[2018\] Recovery of the 3D Virtual Human: Monocular Estimation of 3D Shape and Pose with Data Driven Priors. [\[PDF\]](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/266852/Endri_Dibra_Thesis_Final.pdf?sequence=3&isAllowed=y)  [\[Project\]](https://www.research-collection.ethz.ch/handle/20.500.11850/266852)
*[Endri Dibra](https://graphics.ethz.ch/~edibra/), ETH Zürich*

##### • \[2017\] Human Segmentation, Pose Estimation and Applications. [\[PDF\]](http://sergioescalera.com/wp-content/uploads/2017/10/MeysamPhDv2.pdf) [\[Slides\]](http://sergioescalera.com/wp-content/uploads/2017/10/Thesis-presentation.pdf)
*Meysam Madadi, Universitat Autònoma de Barcelonato*

##### • \[2017\] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/tzionas-thesis-phd)
*[Dimitrios Tzionas](http://ps.is.tue.mpg.de/person/dtzionas), University of Bonn*

##### • \[2016\] Tracking Hands in Action for Gesture-based Computer Input. [\[PDF\]](http://cs.stanford.edu/people/ssrinath/pubs/Dissertation_SrinathSridhar.pdf)
*[Srinath Sridhar](http://cs.stanford.edu/people/ssrinath/),  Max Planck Institute for Informatics*

##### • \[2016\] 3D hand pose regression with variants of decision forests. [\[PDF\]](https://spiral.imperial.ac.uk/bitstream/10044/1/31531/1/Tang-D-2016-PhD-Thesis.pdf) [\[Project\]](https://spiral.imperial.ac.uk/handle/10044/1/31531)
*[Danhang Tang](http://www.iis.ee.ic.ac.uk/dtang/), Imperial College London*

##### • \[2016\] Deep Learning for Human Motion Analysis. [\[PDF\]](https://tel.archives-ouvertes.fr/tel-01470466v1/document) [\[Project\]](https://tel.archives-ouvertes.fr/tel-01470466v1)
*[Natalia Neverova](https://nneverova.github.io/), National Institut of Applied Science (INSA de Lyon), France*

##### • \[2016\] Real time hand pose estimation for human computer interaction. [\[PDF\]](http://epubs.surrey.ac.uk/809973/1/thesis.pdf) [\[Project\]](http://epubs.surrey.ac.uk/809973/)
*[Philip Krejov](http://www.krejov.com/), University of Surrey*

##### • \[2015\] Efficient Tracking of the 3D Articulated Motion of Human Hands. [\[PDF\]](http://users.ics.forth.gr/~oikonom/pb/oikonomidisPhDthesis.pdf)
*[Iason Oikonomidis](http://users.ics.forth.gr/~oikonom/pb/), University of Crete*

##### • \[2015\] Vision-based hand pose estimation and gesture recognition. [\[PDF\]](https://repository.ntu.edu.sg/bitstream/handle/10356/65842/ThesisMain.pdf?sequence=1&isAllowed=y)
*[Hui Liang](https://sites.google.com/site/seraphlh/home), Nanyang Technological University*

##### • \[2015\] Localization of Humans in Images Using Convolutional Networks. [\[PDF\]](http://www.cims.nyu.edu/~tompson/others/thesis.pdf)
*[Jonathan Tompson](http://cims.nyu.edu/~tompson/), New York University*

[\[back to top\]](#contents)

## Datasets

- S/R: Synthetic (S) or Real (R) or Both (B)
- C/D: Color (RGB) or Depth (D)
- Obj: Interaction with objects or not
- #J:  No. of joints or Mesh (M)
- V: view (3rd or egocentric)
- #S: No. of subjects
- #F: No. of frames (train/test)
- Mesh: Mesh annotations

### Depth

|Dataset|Year|S/R|Mesh|Obj|#J|V|#S|#F|Paper|
|------|------|------|------|------|------|------|------|------|----------------|
|[NYU](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm) | 2014 | R |❌|❌| 36 | 3rd | 2 | 72k/8k | SIGGRAPH 2014 [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf)|
|[ICVL](https://labicvl.github.io/hand.html) | 2014 | R |❌|❌|  16 | 3rd  |  10 | 331k/1.5k | CVPR 2014 [\[PDF\]](https://labicvl.github.io/docs/pubs/Danny_CVPR_2014.pdf)|
|[MSRA15](https://github.com/geliuhao/CVPR2016_HandPoseEstimation/issues/4) | 2015 | R |❌|❌|  21 | 3rd  |  9 | 76,375 | CVPR 2015 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf)|
|[BigHand2.2M](http://icvl.ee.ic.ac.uk/hands17/challenge/) | 2017 | R |❌|❌|  21 | 3rd  |  10 | 2.2M | CVPR 2017 [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)|
|[SynHandEgo](https://bit.ly/2WMWM5u) | 2019 | R |✅|❌| - | ego | - | - | Computers & Graphics 2019 [\[PDF\]](https://www.dfki.de/fileadmin/user_upload/import/10684_CAG_Jameel.pdf)|
|[FHAD](https://guiggh.github.io/publications/first-person-hands/) | 2018 | R |❌| ✅ |  21 | ego  |  6 | 100k | CVPR 2018 [\[PDF\]](https://arxiv.org/pdf/1704.02463)|
|[SynHand5M](https://cloud.dfki.de/owncloud/index.php/s/iCMRF7a5FkXrdpn) | 2018 | S | - |❌|  M | 3rd  |  - | 5M | 3DV 2018 [\[PDF\]](https://arxiv.org/pdf/1808.09208.pdf)|
|[MSRC (FingerPaint)](https://www.microsoft.com/en-us/download/details.aspx?id=52288)  | 2015| S |❌|❌|  21 | both  |  1 | 100k | CHI 2015 [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf)|
|[HandNet](http://www.cs.technion.ac.il/~twerd/HandNet/) | 2015 | R |❌|❌|  6 | 3rd  |  10 | 202k/10k  | BMVC 2015 [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf)|
|[Hands in Action](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/) | 2014 | R | - | ✅ |  - | 3rd  |  - | - | IJCV 2016 [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf)|
|[MSRA14](https://jimmysuen.github.io/) | 2014|  R |❌|❌|  21 | 3rd  |  6 | 2,400 | CVPR 2014 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Qian_Realtime_and_Robust_2014_CVPR_paper.pdf)|
|[ASTAR](http://hpes.bii.a-star.edu.sg/) | 2013 | R | - |❌|  20 | 3rd  |  30 | 870 | ICCV 2013 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_iccv_2013/papers/Xu_Efficient_Hand_Pose_2013_ICCV_paper.pdf)|


### RGB+Depth

|Dataset|Year|S/R|Mesh|Obj|#J|V|#S|#F|Paper|
|------|------|------|------|------|------|------|------|------|----------------|
|[ContactPose](https://contactpose.cc.gatech.edu/) | 2020 | R | ✅ | ✅ | 21 | 3rd | 50 | 2.9M | ECCV 2020 [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123580358.pdf)|
|[Ego3DHands](https://github.com/AlextheEngineer/Ego3DHands) | 2020 | S | - |❌| 21 | ego | 1 | 50k/5k | arXiv 2020 [\[PDF\]](https://arxiv.org/pdf/2006.01320.pdf)|
|[ObMan](https://www.di.ens.fr/willow/research/obman/data/) | 2019 | S | ✅ |✅| - | - | - | 150k | CVPR 2019 [\[PDF\]](https://openaccess.thecvf.com/content_CVPR_2019/papers/Hasson_Learning_Joint_Reconstruction_of_Hands_and_Manipulated_Objects_CVPR_2019_paper.pdf)|
|[EgoDexter](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm) | 2017 | R | - | ✅ |  5 | ego  |  4 | 1485 | ICCV 2017 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf)|
|[SynthHands](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/SynthHands.htm) | 2017 | S | - | Both |  21 | ego  |  2 | 63,530  | ICCV 2017 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf)|
|[RHD](https://lmb.informatik.uni-freiburg.de/resources/datasets/RenderedHandposeDataset.en.html) | 2017 | S | - |❌|  21 | 3rd  |  20 | 41k/2.7k  |ICCV 2017 [\[PDF\]](https://arxiv.org/pdf/1705.01389.pdf)|
|[STB](https://sites.google.com/site/zhjw1988/) | 2017 | R | - |❌|  21 | 3rd |  1 | 18k | ICIP 2017 [\[PDF\]](http://www.cs.cityu.edu.hk/~jianbjiao2/pdfs/icip.pdf)|
|[Dexter+Object](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/dexter+object.htm) | 2016 | R | - | ✅ |  5 | 3rd  |  2 | 3,014 | ECCV 2016 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/content/RealtimeHO_ECCV2016.pdf)|
|[UCI-EGO](http://pascal.inrialpes.fr/data2/grogez/UCI-EGO/UCI-EGO.tar.gz) | 2014 | R |-|❌|  26 | ego  |  2 | 400 | ECCVW 2014 [\[PDF\]](https://www.cs.cmu.edu/~deva/papers/egocentric_depth_workshop.pdf)|
|[Dexter1](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/dexter1.htm) | 2013 | R |- |❌|  6 | 3rd |  1 | 2,137 | ICCV 2013 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf)|

### RGB

|Dataset|Year|S/R|Mesh|Obj|#J|V|#S|#F|Paper|
|------|------|------|------|------|------|------|------|------|----------------|
|[HIU-DMTL-Data](https://github.com/MandyMo/HIU-DMTL/) | 2021 | R | ❌ | ❌ | 21 | 3rd/ego | 200 | 40,000 | ICCV 2021 [\[PDF\]](https://openaccess.thecvf.com/content/ICCV2021/papers/Zhang_Hand_Image_Understanding_via_Deep_Multi-Task_Learning_ICCV_2021_paper.pdf)|
|[InterHand2.6M](https://mks0601.github.io/InterHand2.6M/) | 2020 | R | ❌ | ❌ | 21 | 3rd | 27 | 2.6M | ECCV 2020 [\[PDF\]](http://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650545.pdf)|
|[YouTube 3D Hands](https://github.com/arielai/youtube_3d_hands) | 2020 | R | ✅ | ✅ | - | 3rd | - | 47,125/1525/1525 | CVPR 2020 [\[PDF\]](https://openaccess.thecvf.com/content_CVPR_2020/papers/Kulon_Weakly-Supervised_Mesh-Convolutional_Hand_Reconstruction_in_the_Wild_CVPR_2020_paper.pdf)|
|[OneHand10K](https://yangangwang.com/papers/WANG-MCC-2018-10.html) | 2019 | R | - |❌| 21 | 3rd | 1 | 10k/1.3k | TCSVT 2019 [\[PDF\]](https://yangangwang.com/papers/WANG-MCC-2018-10.pdf)|
|[FreiHAND](https://lmb.informatik.uni-freiburg.de/resources/datasets/FreihandDataset.en.html) | 2019 | R | - | ✅ |  21 | 3rd  |  - | 130k/3960  | ICCV 2019 [\[PDF\]](https://arxiv.org/pdf/1909.04349.pdf)|
|[GANerated Hands](https://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/GANeratedDataset.htm) | 2018 | S | - | Both |  21 | ego  |  - | 330k | CVPR 2018 [\[PDF\]](https://handtracker.mpi-inf.mpg.de/projects/GANeratedHands/content/GANeratedHands_CVPR2018.pdf)|
|[CMU Panoptic HandDB](http://domedb.perception.cs.cmu.edu/handdb.html) | 2017 | B | - |❌|  21 | 3rd  |  - | 14,817 | CVPR 2017 [\[PDF\]](https://arxiv.org/pdf/1704.07809)|
|[MHP](http://www.rovit.ua.es/dataset/mhpdataset/) | 2017 | R | - | ❌  | 21 | 3rd | 9 | 80k | IVC 2017 [\[PDF\]](https://arxiv.org/pdf/1707.03742.pdf)  |

**Credits:**
- [1] Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis, CVPR 2017 [\[PDF\]](https://labicvl.github.io/docs/pubs/Shanxin_CVPR_2017.pdf)
- [2] Depth-based hand pose estimation: methods, data, and challenges, ICCV 2015  [Link](http://arrummzen.net/#HandData)
- [3] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects, IJCV 2016 [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf)
- [4] [MPI Hand Tracking Central](http://handtracker.mpi-inf.mpg.de/)

[\[back to top\]](#contents)

## Workshops

#### [1] *Workshops on Observing and Understanding Hands in Action:*
##### • [HANDS 2019](https://sites.google.com/view/hands2019/), In conjunction with ICCV 2019

##### • [HANDS 2018](https://sites.google.com/view/hands2018/), In conjunction with ECCV 2018
  - HANDS18: Methods, Techniques and Applications for Hand Observation. [\[PDF\]](https://arxiv.org/abs/1810.10818)

##### • [HANDS 2017](http://icvl.ee.ic.ac.uk/hands17/), In conjunction with ICCV 2017
  - Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Yuan_Depth-Based_3D_Hand_CVPR_2018_paper.pdf)

##### • [HANDS 2016](https://labicvl.github.io/hand/Hands2016/), In conjunction with CVPR 2016
##### • [HANDS 2015](http://www.ics.uci.edu/~jsupanci/HANDS-2015/), In conjunction with CVPR 2015

#### [2] *Workshops on Capturing and modeling human bodies, faces and hands:*

##### • [PeopleCap 2018](https://peoplecap2018.weebly.com/), In conjunction with ECCV 2018
##### • [PeopleCap 2017](http://peoplecap.weebly.com/), In conjunction with ICCV 2017

[\[back to top\]](#contents)

## Challenges

#### [1] [HANDS19 Challenge](https://sites.google.com/view/hands2019/challenge)
*[HANDS 2019](https://sites.google.com/view/hands2019/), [ICCV 2019](http://iccv2019.thecvf.com/)*
- Submission Website: [Depth-Based Task](https://competitions.codalab.org/competitions/20913), [Depth-Based Hand-Object Task](https://competitions.codalab.org/competitions/20449), [RGB-Based Hand-Object Task](https://competitions.codalab.org/competitions/21116)
- Documents
    - [Measuring Generalisation to Unseen Viewpoints, Articulations, Shapes and Objects for 3D Hand Pose Estimation under Hand-Object Interaction](https://arxiv.org/pdf/2003.13764.pdf), ECCV 2020

#### [2] [The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation](http://icvl.ee.ic.ac.uk/hands17/challenge/)
*[HANDS 2017](http://icvl.ee.ic.ac.uk/hands17/), [ICCV 2017](http://iccv2017.thecvf.com/)*
- Submission Website: [Frame and Tracking Task](https://competitions.codalab.org/competitions/17356#results), [Hand-Object Task](https://competitions.codalab.org/competitions/17452#results)
- Documents
    - [The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation](https://arxiv.org/pdf/1707.02237.pdf), arXiv 2017
    - [Depth-Based 3D Hand Pose Estimation: From Current Achievements to Future Goals.](https://arxiv.org/pdf/1712.03917.pdf), CVPR 2018

[\[back to top\]](#contents)

## Other Related Papers

##### • [\[arXiv 2011.07252\]](https://arxiv.org/abs/2011.07252) Ego2Hands: A Dataset for Egocentric Two-hand Segmentation and Detection. [\[PDF\]](https://arxiv.org/pdf/2011.07252.pdf) [\[Code\]](https://github.com/AlextheEngineer/Ego2Hands)
_Fanqing Lin, Tony Martinez_

##### • \[2020 IJCV\] Learning Multi-Human Optical Flow. [\[PDF\]](https://link.springer.com/content/pdf/10.1007/s11263-019-01279-w.pdf) [\[Project\]](https://humanflow.is.tue.mpg.de/) [\[Code\]](https://github.com/anuragranj/humanflow2)
_Anurag Ranjan, David T. Hoffmann, Dimitrios Tzionas, Siyu Tang, Javier Romero, and Michael J. Black_

##### • \[2019 ICCV\] Contextual Attention for Hand Detection in the Wild. [\[PDF\]](https://arxiv.org/pdf/1904.04882.pdf) [\[Project\]](http://vision.cs.stonybrook.edu/~supreeth/) [\[Code\]](https://github.com/SupreethN/Hand-CNN)
_Supreeth Narasimhaswamy\*, Zhengwei Wei\*, Yang Wang, Justin Zhang, Minh Hoai_

##### • \[2018 SIGGRAPH\] Online Optical Marker-based Hand Tracking with Deep Labels. [\[PDF\]](https://research.fb.com/wp-content/uploads/2018/06/Online-Optical-Marker-based-Hand-Tracking-with-Deep-Labels.pdf) [\[Code\]](https://github.com/Beibei88/Mocap_SIG18_Data)
*Shangchen Han, Beibei Liu, Robert Wang, Yuting Ye, Christopher D. Twigg, Kenrick Kin*

##### • \[2018 CVPRW\] HandyNet: A One-stop Solution to Detect, Segment, Localize & Analyze Driver Hands. [\[PDF\]](https://arxiv.org/pdf/1804.07834.pdf) [\[Code\]](https://github.com/arangesh/HandyNet)
*Akshay Rangesh, Mohan M. Trivedi*

##### • \[2018 CVPR\] DensePose: Dense Human Pose Estimation In The Wild. [\[PDF\]](https://arxiv.org/pdf/1802.00434.pdf)  [\[Project\]](http://densepose.org/) [\[Code\]](https://github.com/facebookresearch/DensePose)
*Rıza Alp Güler, Natalia Neverova, Iasonas Kokkinos*

##### • \[2018 CVPR\] Analysis of Hand Segmentation in the Wild. [\[PDF\]](https://arxiv.org/pdf/1803.03317.pdf) [\[Code\]](https://github.com/aurooj/Hand-Segmentation-in-the-Wild)
*Aisha Urooj Khan, Ali Borji*

##### • \[2018 CVPR\] Total Capture: A 3D Deformation Model for Tracking Faces, Hands, and Bodies. [\[PDF\]](https://arxiv.org/pdf/1801.01615.pdf) [\[Project\]](http://www.cs.cmu.edu/~hanbyulj/totalcapture/) *(CVPR Best Student Paper Award)*
*Hanbyul Joo, Tomas Simon, Yaser Sheikh*

##### • \[2017 CVPR\] SurfNet: Generating 3D shape surfaces using deep residual networks. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2017/03/Sinha_CVPR17.pdf)
*Ayan Sinha, Asim Unmesh, Qixing Huang, Karthik Ramani*

##### • \[2017 CVPR\] Learning from Simulated and Unsupervised Images through Adversarial Training. [\[PDF\]](https://arxiv.org/pdf/1511.06728) [\[Project\]](https://machinelearning.apple.com/2017/07/07/GAN.html) [\[Code-Tensorflow\]](https://github.com/carpedm20/simulated-unsupervised-tensorflow) [\[Code-Keras\]](https://github.com/wayaai/SimGAN) [\[Code-Tensorflow-NYU-Hand\]](https://github.com/shinseung428/simGAN_NYU_Hand) *(CVPR Best Paper Award)*
*Ashish Shrivastava, Tomas Pfister, Oncel Tuzel, Josh Susskind, Wenda Wang, Russ Webb*

##### • \[2016 3DV\] Learning to Navigate the Energy Landscape. [\[PDF\]](http://www.robots.ox.ac.uk/~tvg/publications/2016/LNEL.pdf) [\[Project\]](http://graphics.stanford.edu/projects/reloc/)
*Julien Valentin, Angela Dai, Matthias Niessner, Pushmeet Kohli, Philip H.S. Torr, Shahram Izadi*

##### • [2015 ICCV] 3D Object Reconstruction from Hand-Object Interactions. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/In-Hand-Scanning/ICCV15_Reconstruction_from_HandObject_Interactions.pdf) [\[Project\]](http://ps.is.tue.mpg.de/publications/-886ddd69-ebde-4f83-8b77-9c41f8af1065)
*Dimitrios Tzionas and Juergen Gall*

[\[back to top\]](#contents)

## Contribute

Contributions welcome! Read the [contribution guidelines](contributing.md) first.

Please feel free to [pull requests](https://github.com/xinghaochen/awesome-hand-pose-estimation/pulls), [open an issue](https://github.com/xinghaochen/awesome-hand-pose-estimation/issues) or send me email (chenxinghaothu@gmail.com) to add awesome papers.


## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0)

To the extent possible under law, [xinghaochen](https://github.com/xinghaochen) has waived all copyright and
related or neighboring rights to this work.
