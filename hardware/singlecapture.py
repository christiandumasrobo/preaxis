import cv2
import numpy as np
from openni import openni2
import time
from matplotlib import pyplot as plt
from urllib.request import urlopen


openni2.initialize('C:\Program Files\OpenNI2\Samples\Bin')     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()

def depth_frame_to_image(frame, to_color=False):
    frame_data = frame.get_buffer_as_uint16()

    img = np.frombuffer(frame_data, dtype=np.uint16)
    img.shape = (1, -1, 640)
    img = np.concatenate((img, img, img), axis=0)
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 0, 1)
    if to_color:
        im_max = img.max()
        img = img / im_max
        img *= 255
    return img

def color_frame_to_image(frame):
    frame_data = frame.get_buffer_as_uint8()

    img = np.frombuffer(frame_data, dtype=np.uint8)
    print(img.shape)
    img.shape = (-1, 640, 3)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

def getimages(i):
    print('ding1')
    frame = depth_stream.read_frame()
    print('ding2')
    img = depth_frame_to_image(frame, True)
    print('ding3')
    cv2.imwrite(str(i) + '_depth.png', img)
    print('ding4')
    frame = color_stream.read_frame()
    print('ding5')
    img = color_frame_to_image(frame)
    print('ding6')
    cv2.imwrite(str(i) + '_color.png', img)

depth_stream = dev.create_depth_stream()
depth_stream.start()
color_stream = dev.create_color_stream()
color_stream.start()

getimages(1)

depth_stream.stop()
color_stream.stop()
openni2.unload()