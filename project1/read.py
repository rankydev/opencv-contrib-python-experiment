import cv2 as cv


def rescale_frame(frame, scale=1.2):
    # working for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    # working for live videos
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('Videos/kitten.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
