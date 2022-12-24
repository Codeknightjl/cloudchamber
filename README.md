# Cloudchamber
Automatic particle track detection in a cloud chamber with on OpenCV-python

This project is based on the paper "Automatic Particle Detection in Clound Chambers" by Zachary Sussman. The code detects and evaluates subatomic particle tracks in videos of functioning cloud chamber.

A few improvements have been made to the original code in the paper:
1. The join_countours function has been modified to resemble a more disjoint set union like approach. It should still run in O(n^2) time in worst case complexity where n is the number of contours but it reduces the number of calls to the find_if_close function and I had hoped that it could increase readability of the code.
2. As an improvement suggested in the paper, the line matching algorithm has been changed to linear regression on each contour instead of finding the minimum area rectangle of each contour and taking its major axis. I have imported the LinearRegression() function from the scikit-learn library as the fitLine() method from OpenCV does not use linear regression. The minimum area rectangle algorithm is still kept to determine the intensity and divergence of each track.
3. An alternate function that uses canny edge detection and probabilistic Hough Transform on each contour to obtain the lines is added. However, this method will not be able to give the intensity and divergence of the track.  
\
\
Note:
- This modified version of the code has not been tested on actual data due to lack of computational resources. 
- There might be discrepancies in delivery of angles among functions due to inconsistencies in return range of OpenCV minAreaRect function's angle and NumPy arctan function which has not been thoroughly tested.  
\
\
I would greatly appreciate any form of rectifications and suggestions to my rendering of the code.  
\
\
Reference:
1. Automatic Particle Detection in Clound Chambers by Zachary Sussman
   https://zacharysussman.com/pdf/cloud-chamber.pdf
2. Disjoint set union (union find) 
   https://cp-algorithms.com/data_structures/disjoint_set_union.html
3. Scikit-learn linear regression
   http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
4. OpenCV-python Hough Transform
   https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
