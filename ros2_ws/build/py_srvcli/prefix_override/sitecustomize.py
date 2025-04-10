import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/karol/Desktop/repos/ros2_tutorials/ros2_ws/install/py_srvcli'
