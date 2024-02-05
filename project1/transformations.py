import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')


# Translate image
def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)


# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, -200, 200)


# cv.imshow('translated', translated)

# Rotate image
def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rot_mat, dimensions)


rotated = rotate(img, 90)

# cv.imshow('Rotated', rotated)

# Resize image
resized = cv.resize(img, (1200, 800), interpolation=cv.INTER_AREA) # use INTER_CUBIC OR INTER_LINEAR for enlarging. INTER_AREA for shrinking
# cv.imshow('Resized', resized)

# Flip image
flipped = cv.flip(img, 1) # 1 for horizontal flip, 0 for vertical flip, -1 for flipping horizontally and vertically
# cv.imshow('Flipped', flipped)

# Crop image
cropped = img[200:400, 200:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
