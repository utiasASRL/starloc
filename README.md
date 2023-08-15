STAR-loc: Dataset for STereo And Range-based localization
=========================================================

This reporitory contains all the data files of the STAR-localization dataset in csv format. 

This reporitory is the recommended starting point for using the dataset. For background information on the data, including setup descriptions, calibration and postprocessing procedures, and links to the raw datafiles (in ROS bag format) please refer to our [arXiv (ADD LINK!)](link-here) report. 

## Authors


## How to use

- Quick start guide
- Citation 

## Frames

NEED TO DEFINE: 

- WORLD FRAME
- RIG FRAME
- UWB TAG / CAMERA FRAME

## File description

All csv files contain the following columns:
- time_s: time since start of experiment (first Vicon measurement)
- x,y, z:  ground truth *rig* pose (translation)
- w, rot_x, rot_y, rot_z:  ground truth *rig* pose (rotation)

Ultra-Wideband measurements (`<dataset-name>/uwb.csv`):

- range: raw distance measurement in meters
- from_id: tag id (1 or 2), measurement radio on the rig
- to_id: anchor id, radios fixed in the room.
- tag_pos_x, tag_pos_y, tag_pos_z:  ground truth *tag* pose (translation)
- bias:  distance bias in meters
- gt_range:  ground truth distance from anchor to tag in meters

below are not available for Decawave measurements (s5):

- tx1, rx1, tx2, rx2, tx3, rx3, fpp1, fpp2, skew1, skew2: additional data used for calibration
- range_calib: calibrated distance measurement in meters
- bias_calib: calibrated distance bias in meters
- std: standard deviation of distance measurements in meters

IMU measurements (`<dataset-name>/imu.csv`):

CHECK BELOW WITH ZEDCAM DATASHEET

- time_s: time since start of experiment (first Vicon measurement)
- orientation_x,y,z: orientation in radiants, in rig frame
- orientation_covariance_0,...,8: elements of covariance matrix*1e9
- angular_velocity_x,y,z: velocity in rad/s, in rig frame
- angular_velocity_covariance_0,...,8: elements of covariance matrix*1e9
- linear_acceleration_x,y,z: linear acceleration in m/s^2, in rig frame
- linear_acceleration_covariance_0,...,8: elements of covariance matrix*1e9

Apriltag measurements (`<dataset-name>/apriltag.csv`):

- apriltag_id: ID of detected apriltag  
- left_u, left_v: pixel-locations of apriltag center detection in left rectified image
- right_u, right_v: pixel-locations of apriltag center detection in right rectified image

CHECK BELOW WITH CONNOR; ADD GT_LEFT_U, etc? 

- camera_pos_x, camera_pos_y, camera_pos_z:  ground truth *camera* pose (translation)
- camera_w, camera_rot_x, camera_rot_y, camera_rot_z:  ground truth *camera* pose (rotation)

Calibration data (`<dataset-name>/calib.json`): 

- fu, fv, cu, cv: instrinsic camera parameters
- b: baseline in meters
- tf_cam_imu: transform from camera frame to imu frame

ADD BELOW TO JSON FILE

- tf_cam_rig: transform from camera frame to sensor rig
- tf_tag1_rig: transform from UWB tag1 to sensor rig
- tf_tag2_rig: transform from UWB tag2 to sensor rig
