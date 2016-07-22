# -*- coding: utf-8 -*-

import numpy as np
import cv2

# load a color image
img = cv2.imread('white.jpg', cv2.IMREAD_COLOR)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()