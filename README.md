# Multicam_Calibration

**Multi camera calibration** is to find the relative pose of the cameras in a given camera system and this has numerous applications in the domain of autonomous vehicles. 
Multicamera setup has is a lot cheaper than a stereo camera setup, it has an advantage of capturing wide range and the baseline distance between the two cameras can be adjusted so that 3D points in the actual world which are far off can be captured. This multicamera setup can be used in visual odometry. 

In my camera setup, I have used 2 Logitech cameras and the same algorithm finds transformation of one camera withrespect to the other and hence it can be easily used for camera sysyem with more than 2 cameras. 
Two sets of images have to be captured using the camera system. 
1. Checkerboard pattern to compute the intrisics of the individual monocular camera
2. Image pair with a physical object of known dimensions

**Scripts:** 

**1. snaps.py** : Capture images from the 2 cameras simultaneous along with the timestaps to match the corresponding images 

**2. cameracalib.py** : Feed the images(Checkerboard pattern - Zhang Method) of each camera to get the camera intrinsics.

**3. essentialmatrix_fundamental.py** : To return the essential and fundamental matrices after finding the corresponding features between the two images from 2 cameras

**4. home.py** : Stereo rectification of the image pair from the two cameras and return the disparity map

**5. video_depth.py** : Consider an object of know dimension in the world and find the scale factor,which can further be used to triangulate to find distances of pointsin the world frame. This can be used to get online disparity and depth map (after finding the scale factor)

**6. relativepose.m** : Computes the extrinsics or the camera transforms of the two cameras call them R1 and R2

If the first camera transform is assumed to be Identity the the relative pose of other cameras can be computed.
In this case R12 = R2.inv(R1)
This way the transforms of other cameras with respect to the first camera can be computed. 

Other implementations of the multi camera calibrations:
1. https://sites.google.com/site/prclibo/toolbox
2. https://github.com/ethz-asl/kalibr
3. https://github.com/KumarRobotics/multicam_calibration





