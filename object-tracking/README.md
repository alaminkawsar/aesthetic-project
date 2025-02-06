# Object Tracking
## Single Object Tracking
Single object tracking methods are very fast. Some of them are CSRT, KCF. Deep Learning based trackers are now proved to be far more accurte than traditional trackers.

For example: (GOTURN)[https://learnopencv.com/goturn-deep-learning-based-object-tracking/]

## Multiple Object Tracking
Some Algorithms are:
1. DeepSORT
2. JDE
3. CenterTrack

# Tracking by Detection and without Detection

# Some Object Tracking Algorihtm
## Simple Online Realtime Tracking (SORT)
- Kalman Filters and Hungarian Algorithm claim to be better than many online tracker.
- SORT is made of 4 key components which are as follows:
	* Detection: Indentify the target object using detection model lie YOLO.
	* Estimation: Propagate the detections from current frame to the next frame using constrant velocity model. 
	* Data association: Target and detected bbox calculated as IOU via Hungarian algorithm. Less IOU neglected via threshold and occlusion problem solved and main tain IDs.
	* Creation and Deletion of Track Identities: This module create and delete ids using IOUmin.

SORT performs very well but generate association matrix to track IDs. DeepSORT uses a better approach based on velocity and appearance of the object.

## DeepSORT Implementation














reference: (Object Tracking-OpenCV)[https://learnopencv.com/understanding-multiple-object-tracking-using-deepsort/]

