import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/karol/Desktop/repos/ROS_Tutorials/ros2_ws/install/my_py_pkg'
