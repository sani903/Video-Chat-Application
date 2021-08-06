import sys
import cv2 as cv
import numpy as np
import os
import argparse

# define a video capture object
parser = argparse.ArgumentParser(
    description='Load a video. Press Q to quit, 1 to have default RGB video, 2 for GrayScale mode, 3 for blurred RGB mode')
parser.add_argument('video', metavar='video.mp4', nargs=1,
                    help='image to be edited')
parser.add_argument('-d', '-dimensions', metavar='', type=int, nargs=2,
                    help='custom dimensions of video, 2 values required')

args = parser.parse_args()
capture = cv.VideoCapture(sys.argv[1])
capture1 = cv.VideoCapture(0)
if capture is None:
    print("Video not found at the location")
else:
    while True:
        ret1, frameset1 = capture1.read()
        ret, frameset = capture.read()
        if ret1 == False or ret == False:
            print("could not read from cameras !")
            break

        if capture.get(1) > capture.get(7) - 2:  # video loop
            capture.set(1, 0)  # if frame count > than total frame number, next frame will be zero
        img1 = cv.resize(frameset, (700, 400), interpolation=cv.INTER_CUBIC)
        img2 = cv.resize(frameset1, (700, 400), interpolation=cv.INTER_AREA)
        both = np.concatenate((img2, img1), axis=1)

        cv.imshow("G", both)
        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    capture.release()
    cv.destroyAllWindows()

