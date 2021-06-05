import numpy as np
import cv2 as cv
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt

# Read both images and convert to grayscale
img1 = cv.imread('left_img.png', cv.IMREAD_GRAYSCALE)
img2 = cv.imread('right_img.png', cv.IMREAD_GRAYSCALE)
# img1 = cv.resize(img1, (720,720))
# img2 = cv.resize(img2, (720,720))
#PREPROCESSING

# fig, axes = plt.subplots(1, 2, figsize=(15, 10))
# axes[0].imshow(img1, cmap="gray")
# axes[1].imshow(img2, cmap="gray")
# axes[0].axhline(250)
# axes[1].axhline(250)
# axes[0].axhline(450)
# axes[1].axhline(450)
# plt.suptitle("Original images")
# plt.show()

# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
(kp1, des1) = sift.detectAndCompute(img1, None)
(kp2, des2) = sift.detectAndCompute(img2, None)
print("For image 1 : # kps: {}, descriptors: {}".format(len(kp1), des1.shape))
print("For image 2 : # kps: {}, descriptors: {}".format(len(kp2), des2.shape))

# Visualize keypoints
imgSift = cv.drawKeypoints(
    img1, kp1, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv.imshow("SIFT Keypoints", imgSift)
# cv.waitKey(0)

# Match keypoints in both images
# Based on: https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Keep good matches: calculate distinctive image features
# Lowe, D.G. Distinctive Image Features from Scale-Invariant Keypoints. International Journal of Computer Vision 60, 91–110 (2004). https://doi.org/10.1023/B:VISI.0000029664.99615.94
# https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
matchesMask = [[0, 0] for i in range(len(matches))]
good = []
pts1 = []
pts2 = []

for i, (m, n) in enumerate(matches):
    if m.distance < 0.5*n.distance:   # Larger the fraction more the number of matches 
        # Keep this keypoint pair
        matchesMask[i] = [1, 0]
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)
# Draw the keypoint matches between both pictures
# Still based on: https://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html
draw_params = dict(matchColor=(0, 255, 0),
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask[1:1500],
                   flags=cv.DrawMatchesFlags_DEFAULT)

keypoint_matches = cv.drawMatchesKnn(
    img1, kp1, img2, kp2, matches[1:1500], None, **draw_params)
#cv.imshow("Keypoint matches", keypoint_matches)
# cv.imwrite("keypoint_matches.png",keypoint_matches)
# cv.waitKey(0)

# ------------------------------------------------------------
# STEREO RECTIFICATION

# Calculate the fundamental matrix for the cameras
# https://docs.opencv.org/master/da/de9/tutorial_py_epipolar_geometry.html
pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
fundamental_matrix, inliers = cv.findFundamentalMat(pts1, pts2, cv.FM_RANSAC)

# We select only inlier points
pts1 = pts1[inliers.ravel() == 1]
pts2 = pts2[inliers.ravel() == 1]
 
print("Fundamental matrix is : ", fundamental_matrix)
# np.savetxt('fundamental_mat.txt',fundamental_matrix)

# **********************************************************************************


# Fundamental matrix is : F =
# F =

#     0.0000   -0.0000   -0.0033
#     0.0000    0.0000   -0.0627
#     0.0015    0.0612    1.0000

#  Essential Matrix is : E =

#     0.0790   -0.1921   -2.3001
#     1.6242    0.7306  -42.4071
#     1.6083   42.9364    1.9117