import cv2
import sys


def play_video(cap):
    is_paused = False
    while (cap.isOpened()):
        if not is_paused:
            ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            key = cv2.waitKey(25)
            if key == 113:
                break
            elif key == 32:
                is_paused = not is_paused
        else:
            break
    return cap


def cleanup(cap):
    cap.release()
    cv2.destroyAllWindows()


def cap_check(path):
    print("Creating capture device at path {}".format(path))
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print("Error opening video stream or file")
    else:
        return cap


if __name__ == '__main__':
    cleanup(play_video(cap_check(sys.argv[1])))
