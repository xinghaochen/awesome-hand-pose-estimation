# Awesome Works on Hand Pose Estimation

## Table of Contents
 - [arXiv Papers](#arxiv-papers)
 - [Conference Papers](#conference-papers)
   - [2017 ICCV](#2017-iccv)
   - [2017 CVPR](#2017-cvpr)
   - [2017 Others](#2017-others)
   - [2016 ECCV](#2016-eccv)
   - [2016 CVPR](#2016-cvpr)
   - [2016 Others](#2016-others)
   - [2015 ICCV](#2015-iccv)
   - [2015 CVPR](#2015-cvpr)
   - [2015 Others](#2015-others)
   - [2014 CVPR](#2014-cvpr)
   - [2014 Others & Before](#2014-others--before)
 - [Journal Papers](#journal-papers)
 - [Theses](#theses)
 - [Datasets](#datasets)
 - [Challenges](#challenges)
 - [Other Related Papers](#other-related-papers)

## Evaluation codes
See folder [``evaluation``](https://github.com/xinghaochen/awesome-hand-pose-estimation/tree/master/evaluation) to get more details about performance evaluation for hand pose estimation.

## arXiv Papers
##### [\[arXiv:1711.10872\]](https://arxiv.org/abs/1711.10872) Occlusion-aware Hand Pose Estimation Using Hierarchical Mixture Density Network. [\[PDF\]](https://arxiv.org/pdf/1711.10872.pdf)
_Qi Ye, Tae-Kyun Kim_

##### [\[arXiv:1711.08996\]](https://arxiv.org/abs/1711.08996) Dense 3D Regression for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1711.08996.pdf)  [\[Code\]](https://github.com/melonwan/denseReg)
_Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao_

##### [\[arXiv:1711.07399\]](https://arxiv.org/abs/1711.07399) V2V-PoseNet: Voxel-to-Voxel Prediction Network for Accurate 3D Hand and Human Pose Estimation from a Single Depth Map. [\[PDF\]](https://arxiv.org/pdf/1711.07399.pdf)
_Gyeongsik Moon, Ju Yong Chang, Kyoung Mu Lee_

##### [\[arXiv:1708.03416\]](https://arxiv.org/abs/1708.03416) Pose Guided Structured Region Ensemble Network for Cascaded Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1708.03416.pdf)
_Xinghao Chen, Guijin Wang, Hengkai Guo, Cairong Zhang_

##### [\[arXiv:1707.07248\]](https://arxiv.org/abs/1707.07248) Towards Good Practices for Deep 3D Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1707.07248.pdf) [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
_Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang_

##### [\[arXiv:1707.03742\]](https://arxiv.org/abs/1707.03742) Large-scale Multiview 3D Hand Pose Dataset. [\[PDF\]](https://arxiv.org/pdf/1707.03742.pdf)
_Francisco Gomez-Donoso, Sergio Orts-Escolano and Miguel Cazorla_

##### [\[arXiv:1705.09606\]](https://arxiv.org/abs/1705.09606) End-to-end Global to Local CNN Learning for Hand Pose Recovery in Depth data. [\[PDF\]](https://arxiv.org/pdf/1705.09606.pdf)
_Meysam Madadi, Sergio Escalera, Xavier Baro, Jordi Gonzalez_

##### [\[arXiv:1704.02224\]](https://arxiv.org/abs/1704.02224) Hand3D: Hand Pose Estimation using 3D Neural Network. [\[PDF\]](https://arxiv.org/pdf/1704.02224.pdf)  [\[Project Page\]](http://www.idengxm.com/hand3d/index.html)
_Xiaoming Deng\*, Shuo Yang\*, Yinda Zhang\*, Ping Tan, Liang Chang, Hongan Wang_

##### [\[arXiv:1612.00596\]](https://arxiv.org/abs/1612.00596) Learning to Search on Manifolds for 3D Pose Estimation of Articulated Objects. [\[PDF\]](https://arxiv.org/pdf/1612.00596.pdf)
*Yu Zhang, Chi Xu, Li Cheng*

##### [\[arXiv:1610.07214\]](https://arxiv.org/abs/1610.07214) 3D Hand Pose Tracking and Estimation Using Stereo Matching. [\[PDF\]](https://arxiv.org/pdf/1610.07214.pdf)
*Jiawei Zhang, Jianbo Jiao, Mingliang Chen, Liangqiong Qu, Xiaobin Xu, Qingxiong Yang*

## Conference Papers

### 2017 ICCV
##### Learning to Estimate 3D Hand Pose from Single RGB Images. [\[PDF\]](https://arxiv.org/pdf/1705.01389.pdf)  [\[Project Page\]](https://lmb.informatik.uni-freiburg.de/projects/hand3d/)   [\[Code\]](https://github.com/lmb-freiburg/hand3d)
_Christian Zimmermann, Thomas Brox_

##### Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/content/OccludedHands_ICCV2017.pdf) [\[Project Page\]](http://handtracker.mpi-inf.mpg.de/projects/OccludedHands/)
*Franziska Mueller, Dushyant Mehta, Oleksandr Sotnychenko, Srinath Sridhar, Dan Casas, Christian Theobalt*

##### Robust Hand Pose Estimation during the Interaction with an Unknown Object. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Robust_Hand_Pose_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Robust_Hand_Pose_ICCV_2017_supplemental.pdf) [\[Project Page\]](https://engineering.purdue.edu/cdesign/wp/robust-hand-pose-estimation-during-the-interaction-with-an-unknown-object/)
*Chiho Choi, Sang Ho Yoon, Chin-Ning Chen, Karthik Ramani*

##### Learning Hand Articulations by Hallucinating Heat Distribution. [\[PDF\]](http://openaccess.thecvf.com/content_ICCV_2017/papers/Choi_Learning_Hand_Articulations_ICCV_2017_paper.pdf) [\[Supp\]](http://openaccess.thecvf.com/content_ICCV_2017/supplemental/Choi_Learning_Hand_Articulations_ICCV_2017_supplemental.pdf)  [\[Project Page\]](https://engineering.purdue.edu/cdesign/wp/learning-hand-articulations-by-hallucinating-heat-distribution/)
*Chiho Choi, Sangpil Kim, Karthik Ramani*

##### [Hands17 Workshop] Back to RGB: 3D tracking of hands and hand-object interactions based on short-baseline stereo. [\[PDF\]](https://arxiv.org/pdf/1705.05301.pdf)
_Paschalis Panteleris, Antonis Argyros_

##### [Hands17 Workshop] DeepPrior++: Improving Fast and Accurate 3D Hand Pose Estimation. [\[PDF\]](https://www.tugraz.at/fileadmin/user_upload/Institute/ICG/Images/team_lepetit/publications/oberweger_iccvw17.pdf) [\[Project Page\]](https://www.tugraz.at/institute/icg/teams/teamlepetit/research/hand-detection-and-3d-pose-estimation/) [\[Code\]](https://github.com/moberweger/deep-prior-pp)
*Markus Oberweger and Vincent Lepetit*

##### [Hands17 Workshop] Hand Pose Estimation Using Deep Stereovision and Markov-chain Monte Carlo. [\[PDF\]](http://openaccess.city.ac.uk/18087/1/BasaruICCVW2017_MCMC.pdf)
*Rilwan Remilekun Basaru, Chris Child, Eduardo Alonso, Greg Slabaugh*

### 2017 CVPR
##### Hand Keypoint Detection in Single Images using Multiview Bootstrapping. [\[PDF\]](https://arxiv.org/pdf/1704.07809) [\[Project Page\]](http://www.cs.cmu.edu/~tsimon/projects/mvbs.html) [\[Code\]](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
*Tomas Simon, Hanbyul Joo, Iain Matthews, Yaser Sheikh*

##### Crossing Nets: Combining GANs and VAEs with a Shared Latent Space for Hand Pose Estimation. [\[PDF\]](http://openaccess.thecvf.com/content_cvpr_2017/papers/Wan_Crossing_Nets_Combining_CVPR_2017_paper.pdf)
*Chengde Wan, Thomas Probst, Luc Van Gool, Angela Yao*

##### Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis. [\[PDF\]](http://www.iis.ee.ic.ac.uk/ComputerVision/docs/pubs/Shanxin_CVPR_2017.pdf)
_Shanxin Yuan\*, Qi Ye\*, Bjorn Stenger, Siddhand Jain, Tae-Kyun Kim_

##### 3D Convolutional Neural Networks for Efficient and Robust Hand Pose Estimation from Single Depth Images.[\[PDF\]](http://eeeweba.ntu.edu.sg/computervision/Research%20Papers/2017/3D%20Convolutional%20Neural%20Networks%20for%20Efficient%20and%20Robust%20Hand%20Pose%20Estimation%20from%20Single%20Depth%20Images.pdf) [\[Project Page\]](https://sites.google.com/site/geliuhaontu/home/cvpr2017)
*Liuhao Ge, Hui Liang, Junsong Yuan and Daniel Thalmann*

### 2017 Others
##### [2017 3DV] How to Refine 3D Hand Pose Estimation from Unlabelled Depth Data? [\[PDF\]](https://graphics.ethz.ch/~edibra/Publications/How%20to%20Refine%203D%20Hand%20Pose%20Estimation%20from%20Unlabelled%20Depth%20Data.pdf)
_Endri Dibra\*, Thomas Wolf\*, Cengiz Öztireli, Markus Gross_

##### [2017 ICIP] Region Ensemble Network: Improving Convolutional Network for Hand Pose Estimation. [\[PDF\]](https://arxiv.org/pdf/1702.02447.pdf)  [\[Code\]](https://github.com/guohengkai/region-ensemble-network)
*Hengkai Guo, Guijin Wang, Xinghao Chen, Cairong Zhang, Fei Qiao, Huazhong Yang*

##### [2017 ICIP] A Hand Pose Tracking Benchmark from Stereo Matching. [\[PDF\]](http://www.cs.cityu.edu.hk/~jianbjiao2/pdfs/icip.pdf)  [\[Project Page\]](https://sites.google.com/site/zhjw1988/)
*Jiawei Zhang, Jianbo Jiao, Mingliang Chen, Liangqiong Qu, Xiaobin Xu, and Qingxiong Yang*

##### [2017 SIGGRAPH Asia] Online Generative Model Personalization for Hand Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2017/HOnline/paper.pdf)  [\[Project Page\]](http://lgg.epfl.ch/publications/2017/HOnline/index.php)
_Anastasia Tkach\*, Andrea Tagliasacchi\*, Edoardo Remelli, Mark Pauly, Andrew Fitzgibbon_

##### [2017 SIGGRAPH Asia] Embodied Hands: Modeling and Capturing Hands and Bodies Together. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/392/Embodied_Hands_SiggraphAsia2017.pdf)  [\[Project Page\]](http://ps.is.tue.mpg.de/publications/embodiedhands)
_Javier Romero\*, Dimitrios Tzionas\* and Michael J. Black_

##### [2017 BMVC] Hand Pose Learning: Combining Deep Learning and Hierarchical Refinement for 3D Hand Pose Estimation. [\[PDF\]](https://www.dropbox.com/s/3y96pnutxum3p4v/0569.pdf?dl=1)
*Min-Yu Wu, Ya Hui Tang, Pai-Wei Ting and Li-Chen Fu*

##### [2017 BMVC] Generative 3D Hand Tracking with Spatially Constrained Pose Sampling. [\[PDF\]](http://users.ics.forth.gr/~argyros/mypapers/2017_09_BMVC_RDSRoditak.pdf) [\[Project Page\]](http://users.ics.forth.gr/~argyros/res_handRDS.html)
*Konstantinos Roditakis, Alexandros Makris and Antonis Argyros*

##### [2017 ICRA] Learning a deep network with spherical part model for 3D hand pose estimation. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7989303)
*Tzu-Yang Chen, Pai-Wen Ting, Min-Yu Wu, Li-Chen Fu*

##### [2017 FG] Occlusion aware hand pose recovery from sequences of depth images. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961746) [\[Slide\]](http://sergioescalera.com/wp-content/uploads/2017/06/FG2017Hand.pdf)
*Meysam Madadi, Sergio Escalera, Alex Carruesco Llorens, Carlos Andujar, Xavier Baro, Jordi Gonzalez*

##### [2017 FG] 3D Hand-Object Pose Estimation from Depth with Convolutional Neural Networks. [\[PDF\]](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7961770) [\[Project Page\]](http://www.cs.man.ac.uk/~goudied/research.html)
*Duncan Goudie, Aphrodite Galata*

### 2016 ECCV
##### Spatial Attention Deep Net with Partial PSO for Hierarchical Hybrid Hand Pose Estimation. [\[PDF\]](http://www.iis.ee.ic.ac.uk/ComputerVision/docs/pubs/Qi_Shanxin_ECCV_2016.pdf) [\[Project Page\]](https://sites.google.com/site/qiyeincv/home/eccv2016)
_Qi Ye\*, Shanxin Yuan\*, Tae-Kyun Kim_

##### Hand Pose Estimation from Local Surface Normals. [\[PDF\]](http://www.vision.ee.ethz.ch/~yaoa/pdfs/wan_eccv16.pdf)
*Chengde Wan, Angela Yao, and Luc Van Gool*

##### Real-time Joint Tracking of a Hand Manipulating an Object from RGB-D Input. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/content/RealtimeHO_ECCV2016.pdf) [\[Project Page\]](http://handtracker.mpi-inf.mpg.de/projects/RealtimeHO/)
*Srinath Sridhar, Franziska Mueller, Michael Zollhöfer, Dan Casas, Antti Oulasvirta, Christian Theobalt*

### 2016 Others
##### \[2016 ICPR\] Depth-based 3D hand pose tracking. [\[PDF\]](http://ieeexplore.ieee.org/abstract/document/7900051)
*Kha Gia Quach, Chi Nhan Duong, Khoa Luu, and Tien D. Bui.*

##### \[2016 IJCAI\] Model-based Deep Hand Pose Estimation. [\[PDF\]](http://xingyizhou.xyz/zhou2016model.pdf) [\[Project Page\]](http://xingyizhou.xyz/) [\[Code\]](https://github.com/tenstep/DeepModel)
*Xingyi Zhou, Qingfu Wan, Wei Zhang, Xiangyang Xue, Yichen Wei*

##### \[2016 SIGGRAPH\] Efficient and precise interactive hand tracking through joint, continuous optimization of pose and correspondences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/SIGGRAPH2016-SmoothHandTracking.pdf)
*Jonathan Taylor et al.*

##### \[2016 SIGGRAPH Asia\] Sphere-Meshes for Real-Time Hand Modeling and Tracking. [\[PDF\]](http://lgg.epfl.ch/publications/2016/HModel/paper.pdf)  [\[Project Page\]](http://lgg.epfl.ch/publications/2016/HModel/index.php) [\[Code\]](https://github.com/OpenGP/hmodel)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

### 2016 CVPR
##### Robust 3D Hand Pose Estimation in Single Depth Images: From Single-View CNN to Multi-View CNNs. [\[PDF\]](http://eeeweba.ntu.edu.sg/computervision/Research%20Papers/2016/Robust%203D%20Hand%20Pose%20Estimation%20in%20Single%20Depth%20Images,%20from%20Single-View%20CNN%20to%20Multi-View%20CNNs.PDF) [\[Project Page\]](https://sites.google.com/site/geliuhaontu/home/cvpr2016) [\[Code\]](https://github.com/geliuhao/CVPR2016_HandPoseEstimation)
*Liuhao Ge, Hui Liang, Junsong Yuan, Daniel Thalmann*

##### DeepHand: Robust Hand Pose Estimation by Completing a Matrix Imputed With Deep Features.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Sinha_DeepHand_Robust_Hand_CVPR_2016_paper.PDF)[\[Project Page\]](https://engineering.purdue.edu/cdesign/wp/deephand-robust-hand-pose-estimation/)
_Ayan Sinha\*, Chiho Choi\*, Karthik Ramani_

##### Efficiently Creating 3D Training Data for Fine Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvpr16.PDF) [\[Project Page\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/semi-auto-anno)
*Markus Oberweger, Gernot Riegler, Paul Wohlhart, Vincent Lepetit*

##### Fits Like a Glove: Rapid and Reliable Hand Shape Personalization.  [\[PDF\]](http://www.samehkhamis.com/tan-cvpr2016.PDF) [\[Project Page\]](http://campar.in.tum.de/Main/DavidTan)
*David Joseph Tan, Thomas Cashman, Jonathan Taylor, Andrew Fitzgibbon, Daniel Tarlow, Sameh Khamis, Shahram Izadi, Jamie Shotton*

### 2015 ICCV
##### Training a Feedback Loop for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_iccv15.pdf) [\[Project Page\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### Opening the Black Box: Hierarchical Sampling Optimization for Estimating Human Hand Pose.  [\[PDF\]](http://www.iis.ee.ic.ac.uk/dtang/iccv_2015_camready.pdf)
*Danhang Tang, Jonathan Taylor, Pushmeet Kohli, Cem Keskin, Tae-Kyun Kim, Jamie Shotton*

##### Depth-based hand pose estimation: data, methods, and challenges. [\[PDF\]](https://arxiv.org/pdf/1504.06378) [\[Project Page\]](http://www.ics.uci.edu/~jsupanci/#HandData) [\[Code\]](https://github.com/jsupancic/deep_hand_pose)
*James Supancic III, Deva Ramanan, Gregory Rogez, Yi Yang, Jamie Shotton*

##### 3D Hand Pose Estimation Using Randomized Decision Forest with Segmentation Index Points. [\[PDF\]](https://www.google.com.sg/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwipy5fi9OvSAhUWwGMKHdSqDzoQFggeMAA&url=http%3A%2F%2Fwww.cv-foundation.org%2Fopenaccess%2Fcontent_iccv_2015%2Fpapers%2FLi_3D_Hand_Pose_ICCV_2015_paper.pdf&usg=AFQjCNGT2imZQPCrX5ggOGGDZoKmokLsAw&sig2=3U22HjWavqmtFM7eO550Fw)
*Peiyi Li, Haibin Ling*

##### A collaborative filtering approach to real-time hand pose estimation. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2015/08/iccv_2015_hand_pose_estimation.pdf) [\[Project Page\]](https://engineering.purdue.edu/cdesign/wp/a-collaborative-filtering-approach-to-real-time-hand-pose-estimation/)
*Chiho Choi, Ayan Sinha, Joon Hee Choi, Sujin Jang, Karthik Ramani*

##### Lending A Hand: Detecting Hands and Recognizing Activities in Complex Egocentric Interactions. [\[PDF\]](https://www.google.com.sg/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjWqf689evSAhVQ4mMKHd_aBCoQFggbMAA&url=http%3A%2F%2Fvision.soic.indiana.edu%2Fpapers%2Fegohands2015iccv.pdf&usg=AFQjCNEpictJfsVL4DHKGE2tm5DMe3G7-w&sig2=LFRJs92qAWwQjAZS1VNMMA)
*Sven Bambach, Stefan Lee, David Crandall, Chen Yu*

##### Understanding Everyday Hands in Action from RGB-D Images. [\[PDF\]](https://www.google.com.sg/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiowKvp9evSAhVJ5GMKHVk-B_gQFggbMAA&url=http%3A%2F%2Fwww.cv-foundation.org%2Fopenaccess%2Fcontent_iccv_2015%2Fpapers%2FRogez_Understanding_Everyday_Hands_ICCV_2015_paper.pdf&usg=AFQjCNEIzPwbdJMme10hqQzSwy0rJNDhIQ&sig2=FI8vFqqQdoVmcrGodTJ7NQ)
*Gregory Rogez, James Supancic III, Deva Ramanan*

### 2015 CVPR
##### Cascaded Hand Pose Regression.  [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.PDF)
*Xiao Sun, Yichen Wei, Shuang Liang, Xiaoou Tang, and Jian Sun*

##### Fast and Robust Hand Tracking Using Detection-Guided Optimization. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/content/FastHandTracker_CVPR2015.pdf) [\[Project Page\]](http://handtracker.mpi-inf.mpg.de/projects/FastHandTracker/)
*Srinath Sridhar, Franziska Mueller, Antti Oulasvirta, Christian Theobalt*

##### Learning an Efficient Model of Hand Shape Variation from Depth Images. [\[PDF\]](http://www.samehkhamis.com/khamis-cvpr2015.pdf)
*Sameh Khamis, Jonathan Taylor, Jamie Shotton, Cem Keskin, Shahram Izadi, Andrew Fitzgibbon*

### 2015 Others
##### \[2015 BMVC\] Rule of Thumb: Deep Derotation for Improved Fingertip Detection. [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf) [\[Project Page\]](http://www.cs.technion.ac.il/~twerd/HandNet/)
*Aaron Wetzler, Ron Slossberg and Ron Kimmel*

##### \[2015 CHI\] Accurate, Robust, and Flexible Real-time Hand Tracking. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf) [\[Project Page\]](https://www.microsoft.com/en-us/research/publication/accurate-robust-and-flexible-real-time-hand-tracking/)
*Toby Sharp, Cem Keskin, Duncan Robertson, Jonathan Taylor, Jamie Shotton, David Kim, Christoph Rhemann, Ido Leichter, Alon Vinnikov, Yichen Wei, Daniel Freedman, Pushmeet Kohli, Eyal Krupka, Andrew Fitzgibbon, Shahram Izadi*

##### \[2015 CVWW\]Hands Deep in Deep Learning for Hand Pose Estimation. [\[PDF\]](https://cvarlab.icg.tugraz.at/pubs/oberweger_cvww15.pdf) [\[Project Page\]](https://cvarlab.icg.tugraz.at/projects/hand_detection/) [\[Code\]](https://github.com/moberweger/deep-prior)
*Markus Oberweger, Paul Wohlhart, Vincent Lepetit*

##### \[2015 FG\]Combining Discriminative and Model Based Approaches for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/final_fg2015.pdf) [\[Project Page\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### \[2015 SGP\] Robust Articulated-ICP for Real-Time Hand Tracking. [\[PDF\]](http://gfx.uvic.ca/pubs/2015/htrack//paper.pdf)  [\[Project Page\]](http://lgg.epfl.ch/publications/2015/Htrack_ICP/index.php) [\[Code\]](https://github.com/OpenGP/htrack)
*Anastasia Tkach, Mark Pauly, Andrea Tagliasacchi*

### 2014 CVPR
##### Realtime and robust hand tracking from depth. [\[PDF\]](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/yichenw-cvpr14_handtracking.pdf) [\[Project Page\]](https://www.microsoft.com/en-us/research/people/yichenw/)
*Chen Qian, Xiao Sun, Yichen Wei, Xiaoou Tang and Jian Sun*

##### Latent regression forest: Structured estimation of 3d articulated hand posture. [\[PDF\]](http://www.iis.ee.ic.ac.uk/dtang/cvpr_14.pdf) [\[Project Page\]](http://www.iis.ee.ic.ac.uk/dtang/hand.html)
*Danhang Tang, Hyung Jin Chang, Alykhan Tejani, T-K. Kim*

##### User-specific hand modeling from monocular depth sequences. [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CVPR2014-UserSpecificHandModeling.pdf) [\[Project Page\]](https://www.microsoft.com/en-us/research/publication/user-specific-hand-modeling-from-monocular-depth-sequences/)
*Jonathan Taylor, Richard Stebbing, Varun Ramakrishna, Cem Keskin, Jamie Shotton, Shahram Izadi, Aaron Hertzmann, Andrew Fitzgibbon*

##### Evolutionary Quasi-random Search for Hand Articulations Tracking. [\[PDF\]](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwj5wfPQsuzTAhUMxbwKHcnBBRUQFggnMAA&url=http%3A%2F%2Fwww.cv-foundation.org%2Fopenaccess%2Fcontent_cvpr_2014%2Fpapers%2FOikonomidis_Evolutionary_Quasi-random_Search_2014_CVPR_paper.pdf&usg=AFQjCNFPvY-vHE1GyUwxg8I0_R5OUj4QAA&sig2=ZsQ-rh6U2m0eijvJXQ817A) [\[Project Page\]](http://users.ics.forth.gr/~oikonom/pb/publications)
*Iason Oikonomidis, Manolis IA Lourakis, Antonis A Argyros*

### 2014 Others & Before
##### \[2014 SIGGRAPH\] Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks. [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf) [\[Project Page\]](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm)
*Jonathan Tompson, Murphy Stein, Yann Lecun and Ken Perlin*

##### \[2013 ICCV\] Real-time Articulated Hand Pose Estimation using Semi-supervised Transductive Regression Forests. [\[PDF\]](http://www.iis.ee.ic.ac.uk/dtang/iccv_13.pdf) [\[Project Page\]](http://www.iis.ee.ic.ac.uk/dtang/hand.html)
*Danhang Tang, Tsz Ho Yu and T-K. Kim*

##### \[2013 ICCV\] Interactive Markerless Articulated Hand Motion Tracking Using RGB and Depth Data. [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf) [\[Project Page\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/)
*Srinath Sridhar, Antti Oulasvirta, Christian Theobalt*

##### \[2013 ICCV\] Efficient Hand Pose Estimation from a Single Depth Image. [\[PDF\]](http://web.bii.a-star.edu.sg/~xuchi/pdf/iccv2013.pdf) [\[Project Page\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)
*Chi Xu, Li Cheng*

##### \[2012 ECCV\] Motion Capture of Hands in Action using Discriminative Salient Points. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/76/jgall_handcapture_eccv12.pdf) [\[Project Page\]](http://ps.is.tue.mpg.de/publications/btgg12)
*Ballan, L. and Taneja, A. and Gall, J. and van Gool, L. and Pollefeys, M.*

##### \[2012 ECCV\] Hand pose estimation and hand shape classification using multi-layered randomized decision forests.
*Cem KeskinFurkan, KıraçYunus Emre, KaraLale Akarun*

##### \[2011 CVPRW\] Real Time Hand Pose Estimation using Depth Sensors. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf)
*Cem Keskin, Furkan Kırac, Yunus Emre Kara, Lale Akarun*

##### \[2011 BMVC\] Efficient Model-based 3D Tracking of Hand Articulations using Kinect. [\[PDF\]](http://www.cp.jku.at/teaching/praktika/imageproc/bodyparts_Algorithmus1.pdf) [\[Project Page\]](http://users.ics.forth.gr/~argyros/research/kinecthandtracking.htm) [\[Code\]](https://github.com/FORTH-ModelBasedTracker/HandTracker)
*Iason Oikonomidis, Nikolaos Kyriazis, Antonis A. Argyros*

## Journal Papers

##### [2017 CVIU] Hand Pose Estimation through Semi-Supervised and Weakly-Supervised Learning. [\[PDF\]](https://arxiv.org/pdf/1511.06728.pdf)
*Natalia Neverova, Christian Wolf, Florian Nebout, Graham Taylor*

##### \[2016 IJCV\] Capturing Hands in Action using Discriminative Salient Points and Physics Simulation. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf) [\[Project Page\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/)
*Tzionas, D., Ballan, L., Srikantha, A., Aponte, P., Pollefeys, M., Gall, J.*

##### \[2016 IJCV\] Lie-X: Depth Image Based Articulated Object Pose Estimation, Tracking, and Action Recognition on Lie Groups. [\[PDF\]](http://web.bii.a-star.edu.sg/~xuchi/pdf/XuEtAl_IJCV16.pdf) [\[Project Page\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)
*Chi Xu, Lakshmi Narasimhan Govindarajan, Yu Zhang, Li Cheng*

##### \[2016 TPAMI\] Latent Regression Forest: Structured Estimation of 3D Hand Poses.
*Danhang Tang, Hyung Chang, Alykhan Tejani, Tae-Kyun Kim*

##### \[2016 CVIU\] Guided Optimisation through Classification and Regression for Hand Pose Estimation. [\[PDF\]](http://www.krejov.com/uploads/2/4/0/5/24053627/1-s2.0-s107731421630193x-main.pdf) [\[Project Page\]](http://www.krejov.com/hand-pose-estimation.html)
*Philip Krejov, Andrew Gilbert, Richard Bowden*

##### \[2015 TCSVT\] Resolving Ambiguous Hand Pose Predictions by Exploiting Part Correlations. [\[PDF\]](https://fae1051c-a-62cb3a1a-s-sites.googlegroups.com/site/seraphlh/2014TCSVT_HandPoseEstimation.pdf?attachauth=ANoY7cqF4PK7sqq9tp3b6n9qdhnx-6DqQwpjMKZIqnM8G-dMWwJFDDj35udChAet0y5jNOepL2MTujtVVwKui3rx8hogCKmYCZba_xEtjyMZII5MepMLrSNMYUOL7TGgkPGFHT7wvYR_dUIw_82Ok2MCo2rFwyTErNVmvlqkXuGNAaI8orzQzsKLfv1PiwVY32NWPlIz_oWuHL1M3slA97O-jXt511socyqDDj-azzhEodhzFjtz1BI%3D&attredirects=0)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

##### \[2015 IJCV\] Estimate Hand Poses Efficiently from Single Depth Images. [\[PDF\]](https://web.bii.a-star.edu.sg/~xuchi/pdf/XuEtAl_IJCV15.pdf) [\[Project Page\]](http://web.bii.a-star.edu.sg/~xuchi/dhand.htm)  [\[Code\]](https://github.com/lzddzh/HandPoseEstimation)
*Chi Xu, Ashwin Nanjappa, Xiaowei Zhang, Li Cheng*

##### \[2014 TMM\] Parsing the Hand in Depth Images. [\[PDF\]](https://fae1051c-a-62cb3a1a-s-sites.googlegroups.com/site/seraphlh/attachments/2014TMM_HandParsing.pdf?attachauth=ANoY7crJCn_-tr0um1h8DhY3QtG8ngGn8jsllw1_S2ykaSsRGXvoeHWz7MW4DJ4KvQbXVd3nIsyWxEcs4rEn04TjtUaOTEMm7llUEP2e4renxgUj7G2DrVKDZzYg3Dbat1xhrvbz0BdjBoGrvxIniQLQ3Jyzs58UCDGSlzo-sGiOdmgMC072ZOCIR9STMP1FDpQzq3WV9fIGMUycXQRyWLja08ADLZOeV3d0eGKO1NoNH8pxN5pDD6M%3D&attredirects=0) [\[Project Page\]](https://sites.google.com/site/seraphlh/projects)  [\[Code\]](https://github.com/shrekei/RandomDecisionForest)
*Hui Liang, Junsong Yuan, Daniel Thalmann*

## Theses
##### \[2017 Thesis\] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf) [\[Project Page\]](http://ps.is.tue.mpg.de/publications/tzionas-thesis-phd)
*[Dimitrios Tzionas](http://ps.is.tue.mpg.de/person/dtzionas), University of Bonn*

##### \[2016 Thesis\] Tracking Hands in Action for Gesture-based Computer Input. [\[PDF\]](http://cs.stanford.edu/people/ssrinath/pubs/Dissertation_SrinathSridhar.pdf)
*[Srinath Sridhar](http://cs.stanford.edu/people/ssrinath/),  Max Planck Institute for Informatics*

##### \[2016 Thesis\] 3D hand pose regression with variants of decision forests. [\[PDF\]](https://spiral.imperial.ac.uk/bitstream/10044/1/31531/1/Tang-D-2016-PhD-Thesis.pdf) [\[Project Page\]](https://spiral.imperial.ac.uk/handle/10044/1/31531)
*[Danhang Tang](http://www.iis.ee.ic.ac.uk/dtang/), Imperial College London*

##### \[2016 Thesis\] Deep Learning for Human Motion Analysis. [\[PDF\]](https://tel.archives-ouvertes.fr/tel-01470466v1/document) [\[Project Page\]](https://tel.archives-ouvertes.fr/tel-01470466v1)
*[Natalia Neverova](http://liris.cnrs.fr/natalia.neverova/), National Institut of Applied Science (INSA de Lyon), France*

##### \[2016 Thesis\] Real time hand pose estimation for human computer interaction. [\[PDF\]](http://epubs.surrey.ac.uk/809973/1/thesis.pdf) [\[Project Page\]](http://epubs.surrey.ac.uk/809973/)
*[Philip Krejov](http://www.krejov.com/), University of Surrey*

##### \[2015 Thesis\] Efficient Tracking of the 3D Articulated Motion of Human Hands. [\[PDF\]](http://users.ics.forth.gr/~oikonom/pb/oikonomidisPhDthesis.pdf)
*[Iason Oikonomidis](http://users.ics.forth.gr/~oikonom/pb/), University of Crete*

##### \[2015 Thesis\] Vision-based hand pose estimation and gesture recognition. [\[PDF\]](https://repository.ntu.edu.sg/bitstream/handle/10356/65842/ThesisMain.pdf?sequence=1&isAllowed=y)
*[Hui Liang](https://sites.google.com/site/seraphlh/home), Nanyang Technological University*

##### \[2015 Thesis\] Localization of Humans in Images Using Convolutional Networks. [\[PDF\]](http://www.cims.nyu.edu/~tompson/others/thesis.pdf)
*[Jonathan Tompson](http://cims.nyu.edu/~tompson/), New York University*

## Datasets
##### NYU Hand Pose Dataset
- [Website](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm)
- [Related Paper:](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf) Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks, SIGGRAPH 2014 [\[PDF\]](http://cims.nyu.edu/~tompson/others/TOG_2014_paper_PREPRINT.pdf)

##### ICVL Dataset
- [Website](http://www.iis.ee.ic.ac.uk/dtang/hand.html)
- [Related Paper:](http://www.iis.ee.ic.ac.uk/dtang/cvpr_14.pdf) Latent regression forest: Structured estimation of 3d articulated hand posture, CVPR 2014 [\[PDF\]](http://www.iis.ee.ic.ac.uk/dtang/cvpr_14.pdf)

##### MARA15 Dataset
- [Website](https://jimmysuen.github.io/)
- [Related Paper:](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf) Cascaded Hand Pose Regression, CVPR 2015 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Sun_Cascaded_Hand_Pose_2015_CVPR_paper.pdf)

##### BigHand2.2M Benchmark
- Website
- [Related Paper:](http://www.iis.ee.ic.ac.uk/ComputerVision/docs/pubs/Shanxin_CVPR_2017.pdf) Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis, CVPR 2017 [\[PDF\]](http://www.iis.ee.ic.ac.uk/ComputerVision/docs/pubs/Shanxin_CVPR_2017.pdf)

##### MARC (FingerPaint) Dataset
- [Website](https://www.microsoft.com/en-us/download/details.aspx?id=52288)
- [Related Paper:](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf) Accurate, Robust, and Flexible Real-time Hand Tracking, CHI 2015 [\[PDF\]](http://www.cs.toronto.edu/~jtaylor/papers/CHI2015-HandTracking.pdf)

##### UCI-EGO Dataset
- [Website](http://pascal.inrialpes.fr/data2/grogez/UCI-EGO/UCI-EGO.tar.gz)
- [Related Paper:](https://www.cs.cmu.edu/~deva/papers/egocentric_depth_workshop.pdf) 3D Hand Pose Detection in Egocentric RGB-D Images, ECCVW 2014 [\[PDF\]](https://www.cs.cmu.edu/~deva/papers/egocentric_depth_workshop.pdf)

##### Hands in Action Dataset
- [Website](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/)
- [Related Paper:](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf) Capturing Hands in Action using Discriminative Salient Points and Physics Simulation, IJCV 2016 [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/Hand-Object-Capture/IJCV_Hand_Object_Capture.pdf)

##### HandNet Dataset (Fingertip)
- [Website](http://www.cs.technion.ac.il/~twerd/HandNet/)
- [Related Paper:](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf) Rule of Thumb: Deep Derotation for Improved Fingertip Detection, BMVC 2015 [\[PDF\]](http://www.cs.technion.ac.il/~twerd/WetzlerSlossbergKimmel-BMVC15.pdf)

##### MARA14 Dataset
- [Website](https://jimmysuen.github.io/)
- [Related Paper:](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Qian_Realtime_and_Robust_2014_CVPR_paper.pdf) Realtime and Robust Hand Tracking from Depth, CVPR 2014 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Qian_Realtime_and_Robust_2014_CVPR_paper.pdf)

##### Dexter 1 Dataset
- [Website](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/dexter1.htm)
- [Related Paper:](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf) Interactive Markerless Articulated Hand Motion Tracking Using RGB and Depth Data, ICCV 2013 [\[PDF\]](http://handtracker.mpi-inf.mpg.de/projects/handtracker_iccv2013/content/handtracker_iccv2013.pdf)

##### ASTAR Dataset
- [Website](http://hpes.bii.a-star.edu.sg/)
- [Related Paper:](http://www.cv-foundation.org/openaccess/content_iccv_2013/papers/Xu_Efficient_Hand_Pose_2013_ICCV_paper.pdf) Efficient hand pose estimation from a single depth image, ICCV 2013 [\[PDF\]](http://www.cv-foundation.org/openaccess/content_iccv_2013/papers/Xu_Efficient_Hand_Pose_2013_ICCV_paper.pdf)

**Credits:**
- [1] Big Hand 2.2M Benchmark: Hand Pose Data Set and State of the Art Analysis, CVPR 2017 [\[PDF\]](http://www.iis.ee.ic.ac.uk/ComputerVision/docs/pubs/Shanxin_CVPR_2017.pdf)
- [2] http://arrummzen.net/#HandData
- [3] Capturing Hand-Object Interaction and Reconstruction of Manipulated Objects. [\[PDF\]](http://ps.is.tue.mpg.de/uploads_file/attachment/attachment/340/Thesis_FINAL_online.pdf)


## Challenges

##### The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation.
*[3rd International Workshop on Observing and Understanding Hands in Action ( HANDS 2017)](http://icvl.ee.ic.ac.uk/hands17/), [ICCV 2017](http://iccv2017.thecvf.com/)*
- [Challenge Website](http://icvl.ee.ic.ac.uk/hands17/challenge/)
- Submission Website: [Frame and Tracking Task](https://competitions.codalab.org/competitions/17356#results), [Hand-Object Task](https://competitions.codalab.org/competitions/17452#results)
- [Document:](https://arxiv.org/abs/1707.02237)
The 2017 Hands in the Million Challenge on 3D Hand Pose Estimation, [arXiv:1704.02463](https://arxiv.org/pdf/1707.02237.pdf), _Shanxin Yuan, Qi Ye, Guillermo Garcia-Hernando, Tae-Kyun Kim_

## Other Related Papers
##### \[2017 ICCV\] Low-Dimensionality Calibration through Local Anisotropic Scaling for Robust Hand Model Personalization. [\[PDF\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/paper.pdf)  [\[Project Page\]](http://lgg.epfl.ch/publications/2017/LocalAnisotropicScaling/index.php) [\[Code\]](https://github.com/edoRemelli/hadjust)
_Edoardo Remelli*, Anastasia Tkach*, Andrea Tagliasacchi, Mark Pauly_

##### \[2017 Neurocomputing\] Multi-task, Multi-domain Learning: application to semantic segmentation and pose regression.
*Fourure, Damien, et al.*

##### [\[arXiv:1704.02463\]](https://arxiv.org/abs/1704.02463) First-Person Hand Action Benchmark with RGB-D Videos and 3D Hand Pose Annotations. [\[PDF\]](https://arxiv.org/pdf/1704.02463.pdf)
*Guillermo Garcia-Hernando, Shanxin Yuan, Seungryul Baek, Tae-Kyun Kim*

##### \[2017 CVPR\] SurfNet: Generating 3D shape surfaces using deep residual networks. [\[PDF\]](https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2017/03/Sinha_CVPR17.pdf)
*Ayan Sinha, Asim Unmesh, Qixing Huang, Karthik Ramani*

##### \[2017 CVPR\] Learning from Simulated and Unsupervised Images through Adversarial Training. [\[PDF\]](https://arxiv.org/pdf/1511.06728) [\[Project Page\]](https://machinelearning.apple.com/2017/07/07/GAN.html) [\[Code-Tensorflow\]](https://github.com/carpedm20/simulated-unsupervised-tensorflow) [\[Code-Keras\]](https://github.com/wayaai/SimGAN) [\[Code-Tensorflow-NYU-Hand\]](https://github.com/shinseung428/simGAN_NYU_Hand)
*Ashish Shrivastava, Tomas Pfister, Oncel Tuzel, Josh Susskind, Wenda Wang, Russ Webb*

##### \[2016 3DV\] Learning to Navigate the Energy Landscape. [\[PDF\]](http://www.robots.ox.ac.uk/~tvg/publications/2016/LNEL.pdf) [\[Project Page\]](http://graphics.stanford.edu/projects/reloc/)
*Julien Valentin, Angela Dai, Matthias Niessner, Pushmeet Kohli, Philip H.S. Torr, Shahram Izadi*

##### [2016 NIPS] DISCO Nets : Dissimilarity Coefficient Networks. [\[PDF\]](http://www.robots.ox.ac.uk/~diane/DISCONET_camera_ready.pdf) [\[Project Page\]](http://www.robots.ox.ac.uk/~diane/DiscoNets.html) [\[Code\]](http://www.robots.ox.ac.uk/~diane/DISCONETS.zip)
*Diane Bouchacourt, M. Pawan Kumar, Sebastian Nowozin*

##### [2015 ICCV] 3D Object Reconstruction from Hand-Object Interactions. [\[PDF\]](http://files.is.tue.mpg.de/dtzionas/In-Hand-Scanning/ICCV15_Reconstruction_from_HandObject_Interactions.pdf) [\[Project Page\]](http://ps.is.tue.mpg.de/publications/-886ddd69-ebde-4f83-8b77-9c41f8af1065)
*Dimitrios Tzionas and Juergen Gall*

---
\* indicates equal contribution
